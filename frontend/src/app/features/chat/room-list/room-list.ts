import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { FormsModule } from '@angular/forms';

import { Room, RoomService } from '../../../core/services/room';

@Component({
  selector: 'app-room-list',
  imports: [FormsModule],
  templateUrl: './room-list.html',
  styleUrl: './room-list.css'
})
export class RoomList implements OnInit {
  rooms: Room[] = [];

  newRoomName = '';
  errorMessage = '';
  isLoading = false;
  isCreating = false;

  constructor(
    private roomService: RoomService,
    private router: Router
  ) {}

  ngOnInit(): void {
    this.loadRooms();
  }

  loadRooms(): void {
    this.isLoading = true;
    this.errorMessage = '';

    this.roomService.getRooms().subscribe({
      next: (rooms) => {
        this.rooms = rooms;
        this.isLoading = false;
      },
      error: () => {
        this.errorMessage = 'Failed to load rooms.';
        this.isLoading = false;
      }
    });
  }

  createRoom(): void {
    const name = this.newRoomName.trim();

    if (!name) {
      return;
    }

    this.isCreating = true;
    this.errorMessage = '';

    this.roomService.createRoom(name).subscribe({
      next: () => {
        this.newRoomName = '';
        this.isCreating = false;
        this.loadRooms();
      },
      error: (error) => {
        this.errorMessage =
          error.error?.message || 'Failed to create room.';

        this.isCreating = false;
      }
    });
  }

  joinRoom(roomId: number): void {
  this.roomService.joinRoom(roomId).subscribe({
    next: () => {
      this.router.navigate(['/rooms', roomId]);
    },
    error: (error) => {
      if (error.error?.message === 'User already joined this room') {
        this.router.navigate(['/rooms', roomId]);
        return;
      }

      this.errorMessage =
        error.error?.message || 'Failed to join room.';
    }
  });
}

  logout(): void {
    localStorage.removeItem('access_token');
    this.router.navigate(['/login']);
  }
}