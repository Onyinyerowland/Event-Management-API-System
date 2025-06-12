from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from schemas.event import Event, EventCreate
from services import event_service

router =APIRouter(prefix="/events", tags=["Events"])

@router.post("/", response_model= Event)
def create_event(data: EventCreate):
    return event_service.create_event(data)

@router.get("/", response_model=list[Event])
def list_events():
    return event_service.list_events()


@router.get("/{event_id}", response_model= Event)
def get_event(event_id:int):
    event= event_service.get_event(event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event

@router.put("/{event_id}", response_model= Event)
def update_event(event_id:int, data:EventCreate):
    event= event_service.update_event(event_id, data)
    if not event:
       raise HTTPException(status_code=404, detail="Event not found")
    return event


@router.post("/{event_id}/close", response_model=Event)
def close_event(event_id:int):
    event=event_service.close_event(event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event


@router.delete("/{event_id}", response_model=Event)
def delete_event(event_id: int):
    event = event_service.delete_event(event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event 
