from typing import Optional

from pydantic import BaseModel, Schema, EmailStr


# Shared properties
class UserBase(BaseModel):
    email: Optional[EmailStr] = Schema(None, description="Unique email of the user")
    is_active: Optional[bool] = Schema(True, description="")
    is_superuser: Optional[bool] = Schema(False, description="Gives user control over other users")
    full_name: Optional[str] = Schema(None, title="Full Name", examples="John Doe")


class UserBaseInDB(UserBase):
    id: int = None


# Properties to receive via API on creation
class UserInCreate(UserBase):
    email: EmailStr
    password: str


# Properties to receive via API on update
class UserInUpdate(UserBase):
    password: Optional[str] = None


# Additional properties to return via API
class User(UserBaseInDB):
    pass


# Additional properties stored in DB
class UserInDB(UserBaseInDB):
    hashed_password: str
