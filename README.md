# Chat Application

A real-time chat application built with **Angular**, **Flask**, **PostgreSQL**, **Cassandra**, and **Socket.IO**.

## Tech Stack

### Frontend

- Angular 21
- TypeScript
- Tailwind CSS
- Socket.IO Client

### Backend

- Python 3.12
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-JWT-Extended
- Flask-SocketIO
- PostgreSQL
- Cassandra
- Socket.IO

---

## Project Structure

```text
chatapp/
├── backend/
│   ├── migrations/
│   ├── requirements.txt
│   ├── src/
│   │   ├── api/
│   │   ├── models/
│   │   ├── repositories/
│   │   ├── schemas/
│   │   ├── services/
│   │   └── sockets/
│   ├── tests/
│   └── test_socket.py
│
├── frontend/
│   ├── src/
│   ├── package.json
│   └── angular.json
│
└── README.md
```

---

# Prerequisites

Install the following before running the application:

- Python 3.12+
- Node.js
- npm
- PostgreSQL
- Cassandra

The application uses:

| Service          | Default Port |
| ---------------- | -----------: |
| Angular Frontend |       `4200` |
| Flask Backend    |       `5000` |
| PostgreSQL       |       `5432` |
| Cassandra        |       `9042` |

---

# 1. Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd chatapp
```

---

# 2. Backend Setup

Navigate to the backend:

```bash
cd backend
```

Create/activate the Python virtual environment:

```bash
source venv/bin/activate
```

If the virtual environment does not exist, create it with:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install backend dependencies:

```bash
pip install -r requirements.txt
```

---

# 3. Backend Environment Variables

The backend supports environment variables for configuration.

Create a `.env` file inside the `backend` directory:

```env
SECRET_KEY=your-secret-key
JWT_SECRET_KEY=your-jwt-secret-key

DATABASE_URL=postgresql://chatapp:password@localhost:5432/chatapp

CASSANDRA_HOSTS=localhost
CASSANDRA_KEYSPACE=chatapp

REDIS_URL=redis://localhost:6379/0

CORS_ORIGINS=http://localhost:4200,http://127.0.0.1:4200

TEST_DATABASE_URL=postgresql://chatapp:password@localhost:5432/chatapp_test
TEST_CASSANDRA_KEYSPACE=chatapp_test

TEST_TOKEN=your-test-jwt-token
```

> Do not commit `.env` files or JWT tokens to GitHub.

The repository's `.gitignore` already excludes `.env`.

---

# 4. PostgreSQL Setup

Create a PostgreSQL database and user matching the configured `DATABASE_URL`.

For the default configuration:

```text
Database: chatapp
User: chatapp
Password: password
Host: localhost
Port: 5432
```

After PostgreSQL is running, apply the database migrations.

From the `backend` directory with the virtual environment activated:

```bash
flask --app src.app db upgrade
```

This creates the required PostgreSQL tables.

The project uses Flask-Migrate/Alembic for database migrations.

---

# 5. Cassandra Setup

The application uses Cassandra for storing chat messages.

Start Cassandra and make sure it is available on:

```text
localhost:9042
```

Create the application keyspace:

```sql
CREATE KEYSPACE IF NOT EXISTS chatapp
WITH replication = {
    'class': 'SimpleStrategy',
    'replication_factor': 1
};
```

Then create the `messages` table:

```sql
USE chatapp;

CREATE TABLE IF NOT EXISTS messages (
    room_id int,
    message_id uuid,
    user_id int,
    content text,
    created_at timestamp,
    PRIMARY KEY (room_id, created_at, message_id)
) WITH CLUSTERING ORDER BY (created_at ASC);
```

The table is designed around the application's main message query:

> Get messages for a particular room in chronological order.

The backend connects to the configured Cassandra keyspace when the Flask application starts.

---

# 6. Start the Backend

Make sure you are inside the `backend` directory and the virtual environment is activated:

```bash
cd backend
source venv/bin/activate
```

Start the backend:

```bash
python -m src.app
```

The backend will be available at:

```text
http://127.0.0.1:5000
```

The Socket.IO/WebSocket connection uses the same backend address:

```text
http://127.0.0.1:5000
```

---

# 7. Frontend Setup

Open a new terminal.

Navigate to the frontend:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start the Angular development server:

```bash
npm start
```

The frontend will be available at:

```text
http://localhost:4200
```

---

# 8. Running the Application

Start the services in the following order:

### 1. PostgreSQL

Make sure PostgreSQL is running on:

```text
localhost:5432
```

### 2. Cassandra

Make sure Cassandra is running on:

```text
localhost:9042
```

and that the `chatapp` keyspace and `messages` table have been created.

### 3. Backend

```bash
cd backend
source venv/bin/activate
python -m src.app
```

Backend:

```text
http://127.0.0.1:5000
```

### 4. Frontend

In another terminal:

```bash
cd frontend
npm install
npm start
```

Frontend:

```text
http://localhost:4200
```

---

# 9. WebSocket / Socket.IO

The application uses Socket.IO for real-time communication.

Backend Socket.IO endpoint:

```text
http://127.0.0.1:5000
```

The client authenticates the Socket.IO connection using a JWT token.

Supported real-time events include:

- `connect`
- `join_room`
- `leave_room`
- `send_message`
- `receive_message`
- `room_joined`
- `room_left`
- `disconnect`
- `error`

---

# 10. API Structure

The backend follows a layered architecture:

```text
API Routes
    ↓
Services
    ↓
Repositories
    ↓
Database
```

### API

HTTP routes are located in:

```text
backend/src/api/
```

### Services

Business logic is located in:

```text
backend/src/services/
```

### Repositories

Database access is located in:

```text
backend/src/repositories/
```

### Models

PostgreSQL models are located in:

```text
backend/src/models/
```

### WebSocket

Socket.IO event handling is located in:

```text
backend/src/sockets/
```

---

# 11. Testing

## Frontend Tests

From the `frontend` directory:

```bash
npm test
```

Build the frontend with:

```bash
npm run build
```

---

## Backend Tests

Backend tests are located under:

```text
backend/tests/
```

Run pytest with:

```bash
pytest
```

The repository also contains a manual Socket.IO test script:

```text
backend/test_socket.py
```

This can be used to manually test the real-time WebSocket functionality.

Run it with:

```bash
python test_socket.py
```

The script requires a valid JWT token supplied through the `TEST_TOKEN` environment variable.

---

# 12. Important Configuration

The backend configuration is located in:

```text
backend/src/config.py
```

Important configuration variables include:

| Variable                  | Purpose                            |
| ------------------------- | ---------------------------------- |
| `SECRET_KEY`              | Flask secret key                   |
| `JWT_SECRET_KEY`          | JWT signing key                    |
| `DATABASE_URL`            | PostgreSQL connection URL          |
| `CASSANDRA_HOSTS`         | Cassandra host(s)                  |
| `CASSANDRA_KEYSPACE`      | Cassandra keyspace                 |
| `REDIS_URL`               | Redis connection URL               |
| `CORS_ORIGINS`            | Allowed frontend origins           |
| `TEST_DATABASE_URL`       | PostgreSQL database used for tests |
| `TEST_CASSANDRA_KEYSPACE` | Cassandra keyspace used for tests  |

---

# 13. Ports

| Component  |   Port |
| ---------- | -----: |
| Angular    | `4200` |
| Flask      | `5000` |
| PostgreSQL | `5432` |
| Cassandra  | `9042` |

---

# 14. Troubleshooting

### Port 4200 already in use

Stop the existing Angular process or start Angular on another port:

```bash
ng serve --port 4201
```

### Port 5000 already in use

Stop the existing Flask process before starting another backend instance.

### Python command not found

Activate the backend virtual environment:

```bash
cd backend
source venv/bin/activate
```

Then verify:

```bash
python --version
```

### Cassandra connection error

Make sure Cassandra is running and that the configured keyspace exists:

```text
chatapp
```

### PostgreSQL connection error

Check that:

- PostgreSQL is running
- The database exists
- The configured username/password are correct
- `DATABASE_URL` points to the correct database

---

# 15. Security

Do not commit the following to GitHub:

- `.env`
- JWT tokens
- passwords
- secret keys
- virtual environments
- `node_modules`
- generated build files

Use environment variables for secrets and local configuration.

---

# 16. Quick Start

Once PostgreSQL and Cassandra are configured:

### Backend

```bash
cd backend
source venv/bin/activate
pip install -r requirements.txt
flask --app src.app db upgrade
python -m src.app
```

### Frontend

In another terminal:

```bash
cd frontend
npm install
npm start
```

Then open:

```text
http://localhost:4200
```
