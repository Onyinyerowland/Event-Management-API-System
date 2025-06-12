from schemas.registration import Registration, RegistrationCreate
from datetime import datetime
from services import user_service, event_service
from typing import Optional, List

registrations = []
registration_id_counter = 1


def register_user(data: RegistrationCreate) -> Registration:
    global registration_id_counter

    user = user_service.get_user(data.user_id)
    event = event_service.get_event(data.event_id)

    if not user or not user.is_active:
        raise ValueError("Inactive or non-existent user.")
    if not event or not event.is_open:
        raise ValueError ("Event not open or does not exist.")

    if any(r.user_id == data.user_id and r.event_id ==data.event_id for r in registrations):
       raise ValueError("Already registered.")

    reg = Registration(id=registration_id_counter, user_id=data.user_id, event_id=data.event_id, registration_date=datetime.now(),
                       attended=False)
    registrations.append(reg)
    registration_id_counter += 1
    return reg


def mark_attendance(reg_id:int)->Optional[Registration]:
    reg=next((r for r in registrations if r.id==reg_id), None)
    if reg:
        reg.attended = True
    return reg

def get_user_registrations(user_id:int) -> List [Registration]:
    return [r for r in registrations if r.user_id==user_id]

def get_all_registrations()-> List[Registration]:
    return registrations

def get_users_who_attended():
    return list (set(r.user_id for r in registrations if r.attended))
