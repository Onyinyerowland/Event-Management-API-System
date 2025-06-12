from schemas.user import User, UserCreate
from typing import Optional

users =[]
user_id_counter = 1

def create_user(user: UserCreate) -> User:
    global user_id_counter
    new_user = User(id=user_id_counter, **user.model_dump())
    users.append(new_user)
    user_id_counter += 1
    return new_user

def get_user(user_id:int):
    return next ((u for u in users if u.id==user_id), None)


def update_user(user_id: int, data: UserCreate) -> Optional[User]:
    user = get_user(user_id)
    if user:
        user.name = data.name
        user.email = data.email
    return user

def delete_user(user_id: int) -> bool:
    global users
    original_len = len(users)
    users = [u for u in users if u.id != user_id]
    return len(users) < original_len



def list_users() -> list[User]:
    return users



def deactivate_user(user_id: int) -> Optional[User]:
    user = get_user(user_id)
    if user:
        user.is_active = False
        return user
    return None
