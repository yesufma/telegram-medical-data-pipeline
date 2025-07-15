from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from . import crud, models, schemas, database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

@app.get("/api/reports/top-products", response_model=List[schemas.TopProduct])
def top_products(limit: int = 5, db: Session = Depends(database.get_db)):
    return crud.get_top_products(db, limit)

@app.get("/api/channels/{channel_name}/activity", response_model=List[schemas.ChannelActivity])
def channel_activity(channel_name: str, db: Session = Depends(database.get_db)):
    results = crud.get_channel_activity(db, channel_name)
    if not results:
        raise HTTPException(status_code=404, detail="Channel not found or no data")
    return results

@app.get("/api/search/messages", response_model=List[schemas.Message])
def search_messages(query: str, db: Session = Depends(database.get_db)):
    return crud.search_messages(db, query)
