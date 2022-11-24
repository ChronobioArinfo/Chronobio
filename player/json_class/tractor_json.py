from pydantic import BaseModel


class TractorJSON(BaseModel):
    id: int
    location: str
