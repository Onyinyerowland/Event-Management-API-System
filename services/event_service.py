from schemas.event import Event, EventCreate
from typing import Optional

events = []
event_id_counter =1


def create_event(data: EventCreate) -> Event:
    global event_id_counter
    event= Event(id=event_id_counter, **data.model_dump())
    events.append(event)
    event_id_counter += 1
    return event


def get_event(event_id:int) -> Optional[Event]:
    return next((e for e in events if e.id== event_id), None)


def update_event(event_id: int, data: EventCreate) -> Optional[Event]:
    for idx, existing_event in enumerate(events):
        if existing_event.id == event_id:
            updated_event = Event(id=event_id, **data.model_dump())
            events[idx] = updated_event
            return updated_event
    return None

def delete_event(event_id: int) -> Optional[Event]:
    global events
    event = get_event(event_id)
    if event:
        events = [e for e in events if e.id != event_id]
        return event
    return None



def list_events() -> list[Event]:
    return events


def close_event(event_id:int):
    event= get_event(event_id)
    if event:
        event.is_open = False
    return event
