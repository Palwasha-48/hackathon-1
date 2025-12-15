# Quickstart: Authentication with Personalization Fields

## Overview
This guide explains how to set up and use the authentication system with personalization fields in the Physical AI & Humanoid Robotics textbook application.

## Prerequisites
- Python 3.11+
- Node.js for Docusaurus frontend
- SQLite database

## Backend Setup

### 1. Environment Configuration
```bash
# Set up environment variables
DATABASE_PATH=/path/to/your/database.db
SECRET_KEY=your-super-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### 2. Database Initialization
The authentication system will automatically create the required database tables, including the extended users table with personalization fields.

### 3. API Endpoints
The authentication API is available at `/auth/*` endpoints:

- `POST /auth/register` - User registration with personalization
- `POST /auth/login` - User authentication
- `GET /auth/me` - Get current user info
- `PUT /auth/profile` - Update user profile/personalization
- `POST /auth/refresh` - Refresh authentication token
- `POST /auth/logout` - User logout

## Frontend Integration

### 1. Registration Flow
Users can register at `/auth/sign-up` with additional fields for:
- Software background (Novice, Python, ROS2 Expert)
- Hardware background (Simulation Only, Edge Kit, Full Robot)

### 2. Login Flow
Users can authenticate at `/auth/sign-in` with email and password.

### 3. Profile Management
Users can update their personalization data at `/auth/profile`.

## Security Features
- Passwords are hashed using bcrypt
- JWT tokens with configurable expiration
- Input validation and sanitization
- Rate limiting on authentication endpoints

## Personalization Integration
The personalization fields (software_background and hardware_background) are stored with the user profile and can be used by the content system to customize the learning experience based on the user's skill level.