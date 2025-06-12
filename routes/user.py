from fastapi import APIRouter, HTTPException
from schemas.user import User, UserCreate
from services import user_service

router = APIRouter(prefix= "/users", tags=["Users"])
@router.post("/", response_model=User)
def create_user(user: UserCreate):
    return user_service.create_user(user)


@router.get("/", response_model=list[User])
def list_users():
    return user_service.list_users()

@router.get("/{user_id}", response_model=User)
def get_user_by_id(user_id: int):
    user = user_service.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{user_id}", response_model=User)
def update_user(user_id: int, data: UserCreate):
    user = user_service.update_user(user_id, data)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.delete("/{user_id}", response_model= dict)
def delete_user(user_id: int):
    success = user_service.delete_user(user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"detail": "User deleted"}


@router.post("/{user_id}/deactivate", response_model=User)
def deactivate_user(user_id:int):
    user= user_service.deactivate_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
