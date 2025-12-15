from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str
    email: str
    name: Optional[str] = None
    software_background: str
    hardware_background: str

class UserLogin(BaseModel):
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"

class TokenData(BaseModel):
    user_id: Optional[int] = None

class UserResponse(BaseModel):
    id: int
    email: str
    name: Optional[str] = None
    software_background: str
    hardware_background: str

    class Config:
        from_attributes = True  # This allows using from_orm

class UserInDB(UserBase):
    id: int
    password_hash: str
    is_active: bool = True
    is_verified: bool = False
    name: Optional[str] = None
    software_background: str
    hardware_background: str

    class Config:
        from_attributes = True