from pydantic import BaseModel


class FieldJSON(BaseModel):
    bought: bool
    content: str
    location: str
    needed_water: int
