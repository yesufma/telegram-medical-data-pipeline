from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class TopProduct(BaseModel):
    product_name: str
    mention_count: int

class ChannelActivity(BaseModel):
    date: datetime
    message_count: int
    image_count: int

class Message(BaseModel):
    message_id: int
    channel_name: str
    date: datetime
    text: str
    has_image: bool
    detected_objects: Optional[List[str]] = []
