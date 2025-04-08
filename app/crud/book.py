from sqlmodel import Session, select
from app.models.book import Book
from uuid import UUID


def create_book(session: Session, book: Book):
    session.add(book)
    session.commit()
    session.refresh(book)
    return book


def get_book_by_id(session: Session, book_id: UUID):
    session.get(Book, book_id)
    return session.get(Book, book_id)


def get_all_books(session: Session):
    return session.exec(select(Book)).all()


def update_book_availability(session: Session, book_id: UUID, is_available: bool):
    book = get_book_by_id(session, book_id)
    if book:
        book.is_available = is_available
        session.commit()
        session.refresh(book)
    return book


def delete_book(session: Session, book_id: UUID):
    book = get_book_by_id(session, book_id)
    if book:
        session.delete(book)
        session.commit()
    return book
