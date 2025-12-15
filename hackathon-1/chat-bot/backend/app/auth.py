from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from typing import Optional
import os
from datetime import timedelta

from .models.auth import UserCreate, UserLogin, Token, UserResponse
from .security import authenticate_user, create_access_token, create_refresh_token, get_user_id_from_token, get_password_hash
from .db import get_connection, fetch_one, execute
from . import db

router = APIRouter(prefix="/auth", tags=["authentication"])

security = HTTPBearer()

@router.post("/register", response_model=UserResponse)
async def register(user: UserCreate):
    """Register a new user"""
    # Check if user already exists
    existing_user = await fetch_one(
        "SELECT id, email FROM users WHERE email = ?",
        user.email
    )

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exists"
        )

    # Hash the password
    password_hash = get_password_hash(user.password)

    # Create the user with personalization fields
    result = await execute(
        "INSERT INTO users (email, password_hash, name, software_background, hardware_background) VALUES (?, ?, ?, ?, ?)",
        user.email,
        password_hash,
        user.name,
        user.software_background,
        user.hardware_background
    )

    # Fetch the created user
    created_user = await fetch_one(
        "SELECT id, email, name, software_background, hardware_background FROM users WHERE email = ?",
        user.email
    )

    return created_user

@router.post("/login", response_model=Token)
async def login(user_credentials: UserLogin):
    """Authenticate user and return access token"""
    # Fetch user from database
    user = await fetch_one(
        "SELECT id, email, password_hash FROM users WHERE email = ?",
        user_credentials.email
    )

    if not user or not authenticate_user(user["password_hash"], user_credentials.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Create access and refresh tokens
    access_token_expires = timedelta(minutes=30)  # 30 minutes
    access_token = create_access_token(
        data={"sub": str(user["id"])},
        expires_delta=access_token_expires
    )
    refresh_token = create_refresh_token(data={"sub": str(user["id"])})

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }

@router.post("/refresh")
async def refresh_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """Refresh access token using refresh token"""
    token_data = get_user_id_from_token(credentials.credentials)

    if token_data is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Verify user still exists
    user = await fetch_one(
        "SELECT id, email FROM users WHERE id = ?",
        token_data["sub"]
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User no longer exists",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Create new access token
    access_token_expires = timedelta(minutes=30)
    new_access_token = create_access_token(
        data={"sub": str(user["id"])},
        expires_delta=access_token_expires
    )

    return {
        "access_token": new_access_token,
        "token_type": "bearer"
    }

@router.get("/me", response_model=UserResponse)
async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """Get current user info from token"""
    user_id = get_user_id_from_token(credentials.credentials)

    if user_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    user = await fetch_one(
        "SELECT id, email FROM users WHERE id = ?",
        user_id
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user

@router.post("/logout")
async def logout():
    """Logout user (client-side token removal is sufficient)"""
    # For JWT tokens, the server doesn't maintain session state
    # The client should remove the token from local storage/cookies
    return {"message": "Successfully logged out"}