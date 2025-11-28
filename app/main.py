from __future__ import annotations

from typing import List

from fastapi import FastAPI, HTTPException

from .schemas import Book, BookCreate, BookUpdate
from .store import BookStore

app = FastAPI(title="Book Shop CRUD API", version="0.1.0")
store = BookStore()


@app.get("/books", response_model=List[Book])
def list_books() -> List[Book]:
    """Return all books currently in the shop."""

    return list(store.list())


@app.post("/books", response_model=Book, status_code=201)
def create_book(payload: BookCreate) -> Book:
    """Add a new book to the shop."""

    return store.create(payload)


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int) -> Book:
    """Fetch a single book by its identifier."""

    book = store.get(book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, payload: BookUpdate) -> Book:
    """Replace the stored data for a book."""

    book = store.update(book_id, payload)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@app.delete("/books/{book_id}", status_code=204)
def delete_book(book_id: int) -> None:
    """Remove a book from the shop."""

    deleted = store.delete(book_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Book not found")
