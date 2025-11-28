from __future__ import annotations

from typing import Dict, Iterable, Optional

from .schemas import Book, BookCreate, BookUpdate


class BookStore:
    """In-memory store for books.

    This class is intentionally simple: it avoids external dependencies
    and is easy to swap for a database-backed implementation later.
    """

    def __init__(self) -> None:
        self._books: Dict[int, Book] = {}
        self._next_id = 1

    def list(self) -> Iterable[Book]:
        return self._books.values()

    def get(self, book_id: int) -> Optional[Book]:
        return self._books.get(book_id)

    def create(self, payload: BookCreate) -> Book:
        book = Book(id=self._next_id, **payload.dict())
        self._books[self._next_id] = book
        self._next_id += 1
        return book

    def update(self, book_id: int, payload: BookUpdate) -> Optional[Book]:
        book = self._books.get(book_id)
        if book is None:
            return None

        update_data = payload.dict(exclude_unset=True)
        updated = book.copy(update=update_data)
        self._books[book_id] = updated
        return updated

    def delete(self, book_id: int) -> bool:
        return self._books.pop(book_id, None) is not None
