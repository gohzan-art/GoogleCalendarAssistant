from pydantic import BaseModel


class User(BaseModel):
    email: str
    name: str
    access_token: str
    timestamp: str
