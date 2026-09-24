import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface Message {
  room_id: number;
  message_id: string;
  user_id: number;
  content: string;
  created_at: string;
}

@Injectable({
  providedIn: 'root'
})
export class MessageService {
  private readonly API_URL = 'http://127.0.0.1:5000/rooms';

  constructor(private http: HttpClient) {}

  getMessages(roomId: number): Observable<Message[]> {
    return this.http.get<Message[]>(
      `${this.API_URL}/${roomId}/messages`
    );
  }
}