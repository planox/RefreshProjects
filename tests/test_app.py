from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def create_sample_book(**overrides):
    payload = {
        "title": "The Pragmatic Programmer",
        "author": "Andy Hunt",
        "price": 42.0,
        "stock": 10,
    }
    payload.update(overrides)
    response = client.post("/books", json=payload)
    assert response.status_code == 201
    return response.json()


def test_create_and_get_book():
    book = create_sample_book()

    get_response = client.get(f"/books/{book['id']}")
    assert get_response.status_code == 200
    assert get_response.json() == book


def test_list_books_returns_all_books():
    create_sample_book(title="Book A", author="Author A")
    create_sample_book(title="Book B", author="Author B")

    response = client.get("/books")
    assert response.status_code == 200
    titles = {item["title"] for item in response.json()}
    assert {"Book A", "Book B"}.issubset(titles)


def test_update_book_changes_fields():
    book = create_sample_book()

    updated_response = client.put(
        f"/books/{book['id']}",
        json={"price": 50.0, "stock": 5},
    )
    assert updated_response.status_code == 200
    data = updated_response.json()
    assert data["price"] == 50.0
    assert data["stock"] == 5


def test_delete_book_removes_entry():
    book = create_sample_book()

    delete_response = client.delete(f"/books/{book['id']}")
    assert delete_response.status_code == 204

    missing_response = client.get(f"/books/{book['id']}")
    assert missing_response.status_code == 404
