import pytest

name_1 = 'Гордость и предубеждение и зомби'
name_2 = 'Что делать, если ваш кот хочет вас убить'
name_3 = 'Harry Potter and Chamber of Secrets'
name_wrong_list = ['', 'Гордость и предубеждение и зомби и предуб', 'Гордость и предубеждение и зомби и предубеждение и зомби']
genre_1 = 'Фантастика'
genre_2 = 'Комедии'
genre_adult_1 = 'Ужасы'
genre_wrong_1 = 'Фильмы'


class TestBooksCollector:

    def test_add_new_book_add_two_books_success(self, collector):
        collector.add_new_book(name_1)
        collector.add_new_book(name_2)
        assert len(collector.books_genre) == 2

    def test_add_new_book_add_book_genre_is_empty_success(self, collector):
        collector.add_new_book(name_1)
        assert collector.books_genre[name_1] == ''

    def test_add_new_book_add_books_with_same_names_failed(self, collector):
        collector.add_new_book(name_1)
        collector.add_new_book(name_1)
        assert len(collector.books_genre) == 1

    @pytest.mark.parametrize('name_wrong', name_wrong_list)
    def test_add_new_book_add_book_with_incorrect_name_failed(self, collector, name_wrong):
        collector.add_new_book(name_wrong)
        assert len(collector.books_genre) == 0

    def test_set_book_genre_valid_genre_success(self, collector):
        collector.add_new_book(name_1)
        collector.set_book_genre(name_1, genre_1)
        assert collector.books_genre[name_1] == genre_1

    def test_set_book_genre_wrong_genre_failed(self, collector):
        collector.add_new_book(name_1)
        collector.set_book_genre(name_1, genre_wrong_1)
        assert not collector.books_genre.get(name_1) == genre_wrong_1

    def test_get_book_genre(self, collector):
        collector.add_new_book(name_1)
        collector.set_book_genre(name_1, genre_1)
        assert collector.books_genre.get(name_1) == genre_1

    def test_get_books_with_specific_genre_two_out_of_three_the_same_success(self, collector):
        collector.add_new_book(name_1)
        collector.set_book_genre(name_1, genre_1)
        collector.add_new_book(name_2)
        collector.set_book_genre(name_2, genre_2)
        collector.add_new_book(name_3)
        collector.set_book_genre(name_3, genre_1)
        result = collector.get_books_with_specific_genre(genre_1)
        assert (name_1 and name_3 in result) and len(result) == 2 and name_2 not in result

    def test_get_books_genre_add_book_success(self, collector):
        collector.add_new_book(name_1)
        collector.set_book_genre(name_1, genre_1)
        assert collector.get_books_genre() == {name_1: genre_1}

    def test_get_books_for_children_one_out_of_three_adult_success(self, collector):
        collector.add_new_book(name_1)
        collector.set_book_genre(name_1, genre_adult_1)
        collector.add_new_book(name_2)
        collector.set_book_genre(name_2, genre_2)
        collector.add_new_book(name_3)
        collector.set_book_genre(name_3, genre_1)
        result = collector.get_books_for_children()
        assert (name_2 and name_3 in result) and len(result) == 2 and name_1 not in result

    def test_add_book_in_favorites_add_one_book_success(self, collector):
        collector.add_new_book(name_1)
        collector.add_new_book(name_2)
        collector.add_book_in_favorites(name_1)
        assert name_1 in collector.favorites and len(collector.favorites) == 1

    def test_delete_book_from_favorites_delete_one_book_success(self, collector):
        collector.add_new_book(name_1)
        collector.add_new_book(name_2)
        collector.add_book_in_favorites(name_1)
        collector.add_book_in_favorites(name_2)
        collector.delete_book_from_favorites(name_1)
        assert name_2 in collector.favorites and name_1 not in collector.favorites and len(collector.favorites) == 1

    def test_get_list_of_favorites_books(self, collector):
        collector.add_new_book(name_1)
        collector.add_new_book(name_2)
        collector.add_book_in_favorites(name_1)
        collector.add_book_in_favorites(name_2)
        assert collector.favorites == [name_1, name_2]









