# Data Model: Authentication with Personalization Fields

## User Entity

**Table**: `users`

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | INTEGER | PRIMARY KEY, AUTOINCREMENT | Unique identifier for the user |
| email | TEXT | UNIQUE, NOT NULL | User's email address for authentication |
| password_hash | TEXT | NOT NULL | Hashed password using bcrypt |
| name | TEXT | | User's full name |
| software_background | TEXT | NOT NULL, DEFAULT 'Beginner' | User's software background level (Novice, Python, ROS2 Expert) |
| hardware_background | TEXT | NOT NULL, DEFAULT 'Beginner' | User's hardware background level (Simulation Only, Edge Kit, Full Robot) |
| created_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | When the user account was created |

### Validation Rules
- Email must be a valid email format
- Password must meet minimum security requirements (8+ characters)
- software_background must be one of: "Novice", "Python", "ROS2 Expert"
- hardware_background must be one of: "Simulation Only", "Edge Kit", "Full Robot"
- Email must be unique across all users

### Relationships
- One-to-many with `chat_history` (user_id)
- One-to-many with `user_levels` (user_id)
- One-to-many with `quiz_responses` (user_id)

## Authentication Token

**Not stored in database** - JWT tokens are stateless

| Field | Type | Description |
|-------|------|-------------|
| access_token | String | JWT token for API authentication (short-lived) |
| refresh_token | String | JWT token for refreshing access token (longer-lived) |
| token_type | String | Token type, typically "bearer" |

### Token Claims
- `sub`: User ID (subject)
- `exp`: Expiration timestamp
- `iat`: Issued at timestamp

## Personalization Profile

**Part of User Entity** - No separate table needed

The personalization profile is integrated into the User entity with dedicated fields for:
- software_background: User's software skill level for content personalization
- hardware_background: User's hardware skill level for content personalization

## State Transitions

### User Registration Flow
1. User provides registration data (email, password, name, personalization fields)
2. System validates input
3. System hashes password
4. System creates user record with provided data
5. System returns authentication tokens

### Profile Update Flow
1. Authenticated user requests profile update
2. System validates personalization field values
3. System updates user record with new personalization data
4. System returns updated profile information