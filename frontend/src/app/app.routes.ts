import { Routes } from '@angular/router';

import { Login } from './features/auth/login/login';
import { Register } from './features/auth/register/register';
import { RoomList } from './features/chat/room-list/room-list';
import { ChatRoom } from './features/chat/chat-room/chat-room';

export const routes: Routes = [
  {
    path: '',
    redirectTo: 'login',
    pathMatch: 'full',
  },
  {
    path: 'login',
    component: Login,
  },
  {
    path: 'register',
    component: Register,
  },
  {
    path: 'rooms',
    component: RoomList,
  },
  {
    path: 'rooms/:roomId',
    component: ChatRoom,
  },
  {
    path: '**',
    redirectTo: 'login',
  },
];
