import { Component, OnDestroy, OnInit } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { DatePipe } from '@angular/common';
import { ActivatedRoute } from '@angular/router';

import { Message, MessageService } from '../../../core/services/message';

import { WebSocketService } from '../../../core/services/websocket';

@Component({
  selector: 'app-chat-room',
  imports: [FormsModule,DatePipe],
  templateUrl: './chat-room.html',
  styleUrl: './chat-room.css',
})
export class ChatRoom implements OnInit, OnDestroy {
  roomId!: number;

  messages: Message[] = [];

  newMessage = '';
  isSending = false;

  constructor(
    private route: ActivatedRoute,
    private messageService: MessageService,
    private webSocketService: WebSocketService,
  ) {}

  ngOnInit(): void {
    this.roomId = Number(this.route.snapshot.paramMap.get('roomId'));

    this.loadMessages();

    this.webSocketService.connect();

    this.webSocketService.joinRoom(this.roomId);

    this.webSocketService.onMessage().subscribe({
      next: (message: Message) => {
        this.messages.push(message);
      },
    });
  }

  loadMessages(): void {
    this.messageService.getMessages(this.roomId).subscribe({
      next: (messages) => {
        this.messages = messages;
      },
      error: (error) => {
        console.error('Failed to load messages', error);
      },
    });
  }

  sendMessage(): void {
    const content = this.newMessage.trim();

    if (!content) {
      return;
    }

    this.isSending = true;

    this.webSocketService.sendMessage(this.roomId, content);

    this.newMessage = '';
    this.isSending = false;
  }

  ngOnDestroy(): void {
    this.webSocketService.leaveRoom(this.roomId);
    this.webSocketService.disconnect();
  }
}
