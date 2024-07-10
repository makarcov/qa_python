## Автоматические тесты для класса BooksCollector

Файл **tests.py** содержит тесты, в файле **conftest.py** находятся фикстуры.

### Описание тестов

1. Тесты для метода `add_new_book`:
    - тест на добавление двух книг ***(success)***
    - тест, что у добавленной книги отсутствует жанр ***(success)***
    - тест, что при добавлении двух книг с одинаковым названием, в словарь попадет только одна запись ***(failed)***
    - параметризированный тест, что при добавлении книги с некорректным именем (пустая строка, 41 символ и 56 символов) - такая книга не будет добавлена в словарь ***(failed)***

2. Тесты для метода `set_book_genre`:
    - тест на присвоение книге корректного жанра ***(success)***
    - тест на присвоение книге корректного жанра ***(failed)***

3. Тест для метода `get_book_genre`:
    - тест на получение жанра книги по ее названию ***(success)***

4. Тест для метода `get_books_with_specific_genre`:
    - тест на вывод списка книг с определённым жанром ***(success)***

5. Тест для метода `get_books_genre`:
    - тест на вывод текущего словаря с книгами и их жанрами ***(success)***

6. Тест для метода `get_books_for_children`:
    - тест на вывод словаря с книгами, которые подходят для детей и не содержащего книг с возрастным рейтингом ***(success)***

7. Тест для метода `add_book_in_favorites`:
    - тест на добавление книги в Избранное ***(success)***

8. Тест для метода `delete_book_from_favorites`:
    - тест на удаление книги из Избранного ***(success)***

9. Тест для метода `get_list_of_favorites_books`:
    - тест на получение списка избранных книг ***(success)***