import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface Room {
  id: number;
  name: string;
  created_at: string;
}

export interface CreateRoomResponse {
  message: string;
  room: Room;
}

@Injectable({
  providedIn: 'root'
})
export class RoomService {
  private readonly API_URL = 'http://127.0.0.1:5000/rooms';

  constructor(private http: HttpClient) {}

  getRooms(): Observable<Room[]> {
    return this.http.get<Room[]>(this.API_URL);
  }

  createRoom(name: string): Observable<CreateRoomResponse> {
    const token = localStorage.getItem('access_token');

    const headers = new HttpHeaders({
      Authorization: `Bearer ${token}`
    });

    return this.http.post<CreateRoomResponse>(
      `${this.API_URL}/create`,
      { name },
      { headers }
    );
  }

  joinRoom(roomId: number): Observable<{ message: string }> {
    const token = localStorage.getItem('access_token');

    const headers = new HttpHeaders({
      Authorization: `Bearer ${token}`
    });

    return this.http.post<{ message: string }>(
      `${this.API_URL}/${roomId}/join`,
      {},
      { headers }
    );
  }
}