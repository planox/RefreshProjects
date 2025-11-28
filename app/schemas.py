from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field, validator


class BookBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=200, description="Book title")
    author: str = Field(..., min_length=1, max_length=200, description="Author name")
    price: float = Field(..., gt=0, description="Retail price in dollars")
    stock: int = Field(..., ge=0, description="Number of copies available")

    @validator("title", "author")
    def strip_whitespace(cls, value: str) -> str:
        cleaned = value.strip()
        if not cleaned:
            raise ValueError("must not be empty or whitespace")
        return cleaned


class BookCreate(BookBase):
    """Schema for creating a new book."""


class BookUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    author: Optional[str] = Field(None, min_length=1, max_length=200)
    price: Optional[float] = Field(None, gt=0)
    stock: Optional[int] = Field(None, ge=0)

    @validator("title", "author")
    def strip_optional_whitespace(cls, value: Optional[str]) -> Optional[str]:
        if value is None:
            return value
        cleaned = value.strip()
        if not cleaned:
            raise ValueError("must not be empty or whitespace")
        return cleaned


class Book(BookBase):
    id: int

    class Config:
        orm_mode = True
