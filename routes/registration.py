from fastapi import APIRouter, HTTPException
from schemas.registration import RegistrationCreate, Registration
from services import registration_service

router = APIRouter(prefix="/registrations", tags=["Registrations"])


@router.post("/", response_model=Registration)
def register_user(data:RegistrationCreate):
    try:
        return registration_service.register_user(data)
    except ValueError as err:
        raise HTTPException(status_code=400, detail=str(err))

@router.post("/{reg_id}/attend", response_model= Registration)
def mark_attendance(reg_id:int):
    reg = registration_service.mark_attendance(reg_id)
    if not reg:
        raise HTTPException(status_code=404, detail="Registration not found")
    return reg

@router.get("/user/{user_id}", response_model=list[Registration])
def get_user_registrations(user_id:int):
    return registration_service.get_user_registrations(user_id)


@router.get("/", response_model=list[Registration])
def get_all():
    return registration_service.get_all_registrations()

@router.get("/attendees", response_model=list[int])
def attendees():
    return registration_service.get_users_who_attended()
