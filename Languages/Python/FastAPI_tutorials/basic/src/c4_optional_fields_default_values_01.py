from typing import Optional
from pydantic import BaseModel


class UserProfile(BaseModel):
    account: str
    location: Optional[str] = None
    subscribed_newsletter: bool = True

user = UserProfile(account="NTKL")
print(user)