import { Injectable } from '@angular/core';
import { io, Socket } from 'socket.io-client';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class WebSocketService {
  private socket: Socket | null = null;

  private readonly SOCKET_URL = 'http://127.0.0.1:5000';

  connect(): void {
    const token = localStorage.getItem('access_token');

    if (!token) {
      throw new Error('Access token not found');
    }

    this.socket = io(this.SOCKET_URL, {
      auth: {
        token
      }
    });
  }

  disconnect(): void {
    this.socket?.disconnect();
    this.socket = null;
  }

  joinRoom(roomId: number): void {
    this.socket?.emit('join_room', {
      room_id: roomId
    });
  }

  leaveRoom(roomId: number): void {
    this.socket?.emit('leave_room', {
      room_id: roomId
    });
  }

  sendMessage(roomId: number, content: string): void {
    this.socket?.emit('send_message', {
      room_id: roomId,
      content
    });
  }

  onMessage(): Observable<any> {
    return new Observable((observer) => {
      this.socket?.on('receive_message', (message) => {
        observer.next(message);
      });
    });
  }
}