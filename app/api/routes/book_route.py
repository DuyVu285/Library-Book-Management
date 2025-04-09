from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from uuid import UUID

from app.schemas.book_schema import BookCreate, BookRead
from app.models.book_model import Book
from app.db.session import get_session
from app.crud.book_crud import (
    create_book,
    delete_book,
    get_all_books,
    get_book_by_id,
    update_book_availability,
)

router = APIRouter(
    prefix="/books",
    tags=["books"],
    responses={404: {"description": "Not found"}},
)


@router.post("/", response_model=BookRead, status_code=status.HTTP_201_CREATED)
async def create_book(
    *,
    session: Session = Depends(get_session),
    book: BookCreate,
):
    existing = session.exec(select(Book).where(Book.isbn == book.isbn)).first()
    if existing:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Book with this ISBN already exists.",
        )

    db_book = Book.model_validate(book)
    create_book(session, db_book)
    return db_book


@router.get("/{book_id}", response_model=BookRead, status_code=status.HTTP_200_OK)
async def get_book(*, session: Session = Depends(get_session), book_id: UUID):
    db_book = get_book_by_id(session, book_id)
    if not db_book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book not found"
        )
    return db_book


@router.get("/", response_model=list[BookRead], status_code=status.HTTP_200_OK)
async def get_all_books(*, session: Session = Depends(get_session)):
    db_books = get_all_books(session)
    if not db_books:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Books not found"
        )
    return db_books


@router.put("/{book_id}", response_model=BookRead, status_code=status.HTTP_200_OK)
async def update_book_availability(
    *,
    session: Session = Depends(get_session),
    book_id: UUID,
    is_available: bool,
):
    db_book = update_book_availability(session, book_id, is_available)
    if not db_book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book not found"
        )
    return db_book


@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(*, session: Session = Depends(get_session), book_id: UUID):
    db_book = delete_book(session, book_id)
    if not db_book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book not found"
        )
    return
