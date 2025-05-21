from pydantic import BaseModel, Field, EmailStr

class UserBase(BaseModel):
    username: str = Field(min_length=5, max_length=22)
    email: str = EmailStr
    age: int = Field(ge=18, le=130)
    city: str = Field(max_length=60)
    
class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int