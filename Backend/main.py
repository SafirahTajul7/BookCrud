from fastapi import FastAPI, Depends, Path, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import models
from models import Books
from database import engine, SessionLocal
from typing import Annotated
from sqlalchemy.orm import Session
from pydantic import BaseModel, StrictInt, Field

app = FastAPI()

# CORS Middleware - allows frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create database tables
models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

# Pydantic model for request validation
class BookRequest(BaseModel):
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)
    published_year: int = Field(gt=0)

# GET all books
@app.get("/books")
async def read_all(db: db_dependency):
    return db.query(Books).all()

# GET single book by ID
@app.get("/books/{book_id}")
async def read_book(db: db_dependency, book_id: int = Path(gt=0)):
    book = db.query(Books).filter(Books.id == book_id).first()
    if book is not None:
        return book
    raise HTTPException(status_code=404, detail="Book not found")

# POST - Create new book
@app.post("/books")
async def create_book(db: db_dependency, book_request: BookRequest):
    book_model = Books(**book_request.dict())
    db.add(book_model)
    db.commit()
    db.refresh(book_model)
    return book_model

# PUT - Update book
@app.put("/books/{book_id}")
async def update_book(
    db: db_dependency,
    book_request: BookRequest,
    book_id: int = Path(gt=0)
):
    book_model = db.query(Books).filter(Books.id == book_id).first()
    if book_model is None:
        raise HTTPException(status_code=404, detail="Book not found")
    
    book_model.title = book_request.title
    book_model.author = book_request.author
    book_model.published_year = book_request.published_year
    
    db.commit()
    return book_model

# DELETE book
@app.delete("/books/{book_id}")
async def delete_book(db: db_dependency, book_id: int = Path(gt=0)):
    book_model = db.query(Books).filter(Books.id == book_id).first()
    if book_model is None:
        raise HTTPException(status_code=404, detail="Book not found")
    
    db.delete(book_model)
    db.commit()
    return {"message": "Book deleted successfully"}