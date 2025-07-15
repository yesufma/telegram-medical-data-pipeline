from sqlalchemy.orm import Session
from .models import FctMessage, FctImageDetection, DimChannel, DimDate
from sqlalchemy import func, and_

PRODUCTS = ["paracetamol", "ibuprofen", "aspirin"]

def get_top_products(db: Session, limit: int = 5):
    results = []
    for product in PRODUCTS:
        count = db.query(func.count(FctMessage.message_id))\
            .filter(FctMessage.text.ilike(f"%{product}%"))\
            .scalar()
        results.append({"product_name": product, "mention_count": count})
    results.sort(key=lambda x: x["mention_count"], reverse=True)
    return results[:limit]

def get_channel_activity(db: Session, channel_name: str):
    return db.query(
        DimDate.date,
        func.count(FctMessage.message_id).label("message_count"),
        func.count(FctImageDetection.detection_id).label("image_count")
    ).join(FctMessage, FctMessage.channel_id == DimChannel.channel_id)\
     .join(DimChannel, DimChannel.channel_name == channel_name)\
     .join(DimDate, FctMessage.date_id == DimDate.date_id)\
     .outerjoin(FctImageDetection, FctImageDetection.message_id == FctMessage.message_id)\
     .group_by(DimDate.date).all()

def search_messages(db: Session, query: str):
    messages = db.query(FctMessage).filter(FctMessage.text.ilike(f"%{query}%")).all()
    results = []
    for msg in messages:
        detected_objects = db.query(FctImageDetection.detected_object)\
            .filter(FctImageDetection.message_id == msg.message_id).all()
        results.append({
            "message_id": msg.message_id,
            "channel_name": msg.channel.channel_name,
            "date": msg.date.date,
            "text": msg.text,
            "has_image": msg.has_image,
            "detected_objects": [obj[0] for obj in detected_objects]
        })
    return results
