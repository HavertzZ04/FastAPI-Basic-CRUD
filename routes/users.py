from fastapi import APIRouter, HTTPException, status
from schemas import UserCreate, User
from crud import get_all_users, get_user, create_user, edit_user, delete_user


router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/", response_model=list[User])
async def get_all_users_router():
    users =  get_all_users()
    return users


@router.get("/{id}", response_model=User)
async def get_user_router(id: int):
    user = get_user(id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("/", response_model=User, status_code=201)
async def create_user_router(user: UserCreate):
    user_to_create = create_user(user)
    if not user_to_create:
        raise HTTPException(status_code=400, detail="Username already exists")
    return user_to_create
    

@router.put("/{id}", response_model=User)
async def edit_user_router(id: int, user: UserCreate):
    user_to_edit = edit_user(User(id=id, **user.model_dump()))
    if not user_to_edit:
        raise HTTPException(status_code=404, detail="User not found")
    return user_to_edit


@router.delete("/{id}", status_code=204)
async def delete_user_router(id: int):
    success = delete_user(id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return None
            