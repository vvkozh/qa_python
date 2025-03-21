import pytest

import data
from main import BooksCollector


@pytest.fixture
def book():
    book = BooksCollector()
    return book

@pytest.fixture
def add_book(book):
    book.add_new_book(data.BOOK_TITLE)
    return book

@pytest.fixture
def add_some_books(book):
    for key, value in (data.DICT_BOOKS.items()):
        book.add_new_book(key)
        book.set_book_genre(key, value)
    return book

@pytest.fixture
def genre_selection():
    select_books = []
    for key, value in (data.DICT_BOOKS.items()):
        if value == data.GENRE:
            select_books.append(key)
    return select_books

@pytest.fixture
def select_book_for_children():
    select_books = []
    for key, value in (data.DICT_BOOKS.items()):
        if value != 'Ужасы' and value != 'Детективы':
            select_books.append(key)
    return select_books

@pytest.fixture
def book_in_favorites(add_book):
    add_book.add_book_in_favorites(data.BOOK_TITLE)
    return add_book