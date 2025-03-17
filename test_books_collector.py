import pytest

import data
from main import BooksCollector

class TestBooksCollector:

    @pytest.mark.parametrize('title', [data.BOOK_TITLE,
                                       'Я',
                                       'Старик, который не читал любовные романы'])
    def test_add_new_book_in_collector(self, title):
        books = BooksCollector()
        books.add_new_book(title)
        get_book = books.get_books_genre()
        assert title in get_book

    def test_get_book_genre(self, add_book):
        add_book.set_book_genre(data.BOOK_TITLE, data.GENRE)
        book_genre = add_book.get_book_genre(data.BOOK_TITLE)
        assert book_genre == data.GENRE

    def test_add_book_in_favorites(self, add_book):
        add_book.add_book_in_favorites(data.BOOK_TITLE)
        favorites = add_book.get_list_of_favorites_books()
        assert data.BOOK_TITLE in favorites

    def test_delete_book_from_favorites(self, book):
        book.add_new_book(data.BOOK_TITLE)
        book.add_book_in_favorites(data.BOOK_TITLE)
        book.delete_book_from_favorites(data.BOOK_TITLE)
        assert book.favorites == []

    def test_get_books_with_specific_genre(self, add_some_books, genre_selection):
        special_genre = add_some_books.get_books_with_specific_genre(data.GENRE)
        assert special_genre == genre_selection #решил добавить дополнительную фикстуру, чтобы не привязываться к сравнению одних и тех же книг, а в data.py легко менять тестовые данные

    def test_get_books_for_children(self, add_some_books, select_book_for_children):
        books_for_children = add_some_books.get_books_for_children()
        assert books_for_children == select_book_for_children #аналогично

    def test_add_book_twice(self, add_book):
        add_book.add_new_book(data.BOOK_TITLE)
        add_book_twice = add_book
        assert len(add_book_twice.books_genre) < 2

    def test_add_name_more_40_symbols(self, book):
        book.add_new_book('Клуб любителей книг и пирогов из картофельных очистков')
        assert len(book.books_genre) < 1

    def test_add_genre_not_in_genre_list(self, add_book):
        add_book.set_book_genre(data.BOOK_TITLE,'Приключения')
        book_genre = add_book.get_book_genre(data.BOOK_TITLE)
        assert book_genre == ''
