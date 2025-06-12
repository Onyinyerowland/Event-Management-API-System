from schemas.speaker import Speaker

speakers =[
    Speaker(id=1, name="Onyinye Rowland", topic="ALT Exams"),
    Speaker(id=2, name="Anna bassey", topic="frontend Mentors"),
    Speaker(id=3, name ="Peace Chuka", topic="World Tour")
]

def list_speakers():
    return speakers
