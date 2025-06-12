from fastapi import APIRouter
from services import speaker_service
from schemas.speaker import Speaker


router = APIRouter(prefix="/speakers", tags=["Speakers"])

@router.get("/", response_model=list[Speaker])
def get_speakers():
    return speaker_service.list_speakers()
