from sqlalchemy import Column, String, DateTime, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
import uuid
from datetime import datetime

Base = declarative_base()

class User(Base):
    """
    User model with personalization fields for software and hardware background
    """
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String, unique=True, nullable=False, index=True)
    password_hash = Column(String, nullable=False)  # Store hashed password
    name = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    email_verified = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)

    # Personalization fields as required by the specification
    software_background = Column(String, nullable=False)  # "Beginner", "Intermediate", "Advanced", "Expert"
    hardware_background = Column(String, nullable=False)  # "Beginner", "Intermediate", "Advanced", "Expert"

    def __repr__(self):
        return f"<User(id={self.id}, email={self.email}, name={self.name})>"