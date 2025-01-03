from pydantic import BaseModel

class User(BaseModel):
    name: str
    key: str
