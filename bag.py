from pydantic import BaseModel

class Bag(BaseModel):
    id: int
    brand: str
    capacity: int
    colour: str
