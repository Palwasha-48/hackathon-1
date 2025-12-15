# Authentication Implementation Plan

## Phase 1: Backend Authentication Setup

### Task 1.1: Install Dependencies
- Add required packages to pyproject.toml:
  - `python-jose[cryptography]` for JWT handling
  - `passlib[bcrypt]` for password hashing
  - `python-multipart` for form handling

### Task 1.2: Create Security Utilities
- Create `app/security.py` with:
  - Password hashing functions
  - JWT token creation/validation functions
  - Password validation utilities

### Task 1.3: Create Authentication Models
- Define Pydantic models for:
  - User registration request
  - User login request
  - Token response
  - User response

### Task 1.4: Create Authentication Router
- Create `app/auth.py` with endpoints:
  - `/register` - User registration
  - `/login` - User authentication
  - `/me` - Get current user info
  - `/refresh` - Token refresh

### Task 1.5: Update Database Models
- Enhance existing users table if needed
- Create functions for user CRUD operations

## Phase 2: Frontend Authentication Components

### Task 2.1: Create Auth Context
- Create React Context for authentication state
- Implement login/logout functions
- Handle token storage and retrieval

### Task 2.2: Create Login Component
- Design login form with email/password
- Implement login functionality
- Add error handling and validation

### Task 2.3: Create Registration Component
- Design registration form
- Implement registration functionality
- Add validation and error handling

### Task 2.4: Update Chatbot Widget
- Modify to check authentication status
- Conditionally save chat history based on auth
- Add "Save to account" functionality

## Phase 3: Protected Endpoints

### Task 3.1: Create Authentication Middleware
- Implement JWT token validation middleware
- Create dependency for requiring authentication

### Task 3.2: Create User-Specific Endpoints
- `/api/chat/history` - Get user's chat history
- `/api/chat/history` - Save chat to user's history
- `/api/user/level` - Get/update user learning level

### Task 3.3: Update Existing Endpoints
- Modify RAG endpoints to optionally save to user history
- Add rate limiting for authenticated users

## Phase 4: OAuth2 Integration

### Task 4.1: GitHub OAuth Setup
- Add GitHub OAuth configuration
- Create OAuth login and callback endpoints
- Handle user creation/linking

### Task 4.2: Frontend OAuth Components
- Add GitHub login button
- Handle OAuth callback in frontend
- Link OAuth accounts to existing accounts

## Phase 5: Security Enhancements

### Task 5.1: Add Rate Limiting
- Implement rate limiting for auth endpoints
- Use in-memory or Redis-based rate limiter

### Task 5.2: Add Password Reset
- Create password reset request endpoint
- Implement password reset functionality
- Add email integration for password reset

## Implementation Order:

1. Start with backend security utilities and models
2. Implement authentication endpoints
3. Create frontend auth context and components
4. Add protected endpoints and middleware
5. Implement OAuth2 integration
6. Add security enhancements

Each phase should be tested independently before moving to the next phase.