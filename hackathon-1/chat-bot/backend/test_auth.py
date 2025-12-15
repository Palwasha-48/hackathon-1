import pytest
import asyncio
from fastapi.testclient import TestClient
from app.main import app
from app import db

# Create a test client
client = TestClient(app)

@pytest.fixture(scope="module")
def event_loop():
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()

@pytest.fixture(autouse=True)
async def setup_db():
    """Initialize the database before each test"""
    await db.init_db()

def test_register_user():
    """Test user registration endpoint with personalization fields"""
    response = client.post(
        "/api/auth/register",
        json={
            "email": "test@example.com",
            "password": "testpassword123",
            "name": "Test User",
            "software_background": "Intermediate",
            "hardware_background": "Beginner"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["email"] == "test@example.com"
    assert data["name"] == "Test User"
    assert data["software_background"] == "Intermediate"
    assert data["hardware_background"] == "Beginner"

def test_register_duplicate_user():
    """Test registering a user with an existing email"""
    # First, register a user
    client.post(
        "/api/auth/register",
        json={
            "email": "duplicate@example.com",
            "password": "testpassword123"
        }
    )

    # Try to register the same user again
    response = client.post(
        "/api/auth/register",
        json={
            "email": "duplicate@example.com",
            "password": "testpassword123"
        }
    )
    assert response.status_code == 400

def test_login_user():
    """Test user login endpoint"""
    # First register a user
    client.post(
        "/api/auth/register",
        json={
            "email": "login@example.com",
            "password": "testpassword123"
        }
    )

    # Then try to log in
    response = client.post(
        "/api/auth/login",
        json={
            "email": "login@example.com",
            "password": "testpassword123"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert "refresh_token" in data
    assert data["token_type"] == "bearer"

def test_login_invalid_credentials():
    """Test login with invalid credentials"""
    response = client.post(
        "/api/auth/login",
        json={
            "email": "nonexistent@example.com",
            "password": "wrongpassword"
        }
    )
    assert response.status_code == 401

def test_get_current_user():
    """Test getting current user info with valid token"""
    # Register and login a user
    client.post(
        "/api/auth/register",
        json={
            "email": "me@example.com",
            "password": "testpassword123"
        }
    )

    login_response = client.post(
        "/api/auth/login",
        json={
            "email": "me@example.com",
            "password": "testpassword123"
        }
    )
    assert login_response.status_code == 200
    token_data = login_response.json()
    access_token = token_data["access_token"]

    # Get user info with valid token
    response = client.get(
        "/api/auth/me",
        headers={"Authorization": f"Bearer {access_token}"}
    )
    assert response.status_code == 200
    user_data = response.json()
    assert user_data["email"] == "me@example.com"

def test_get_current_user_invalid_token():
    """Test getting current user info with invalid token"""
    response = client.get(
        "/api/auth/me",
        headers={"Authorization": "Bearer invalidtoken"}
    )
    assert response.status_code == 401