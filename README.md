# Book Shop CRUD API

A simple FastAPI application that exposes CRUD operations for managing books in a shop. Data is stored in memory for ease of use and can be swapped for a persistent backend later.

## Setup

1. Create and activate a virtual environment (optional but recommended).
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Running the API

Launch the development server with uvicorn:

```bash
uvicorn app.main:app --reload --port 8000
```

The API will be available at `http://localhost:8000`. Interactive docs are accessible at `/docs`.

## Endpoints

- `GET /books` — list all books.
- `POST /books` — create a new book.
- `GET /books/{book_id}` — fetch a book by ID.
- `PUT /books/{book_id}` — update an existing book.
- `DELETE /books/{book_id}` — remove a book.

## Running Tests

Execute the automated tests with pytest:

```bash
pytest
```
