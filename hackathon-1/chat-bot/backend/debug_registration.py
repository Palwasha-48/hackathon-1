import asyncio
from app import db
from app.main import app
from fastapi.testclient import TestClient

# Initialize the database
async def init():
    await db.init_db()

asyncio.run(init())

client = TestClient(app)

response = client.post(
    '/api/auth/register',
    json={
        'email': 'test@example.com',
        'password': 'testpassword123',
        'name': 'Test User',
        'software_background': 'Intermediate',
        'hardware_background': 'Beginner'
    }
)
print('Status code:', response.status_code)
print('Response text:', response.text)
print('Response JSON:', response.json() if response.content else 'No content')