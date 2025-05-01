from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    @pytest.mark.parametrize("book_name, genre, expected_genre", [
        ('Гордость и предубеждение и зомби', 'Фантастика', 'Фантастика'),
        ('Что делать, если ваш кот хочет вас убить', 'Комедии', 'Комедии'),
        ('Война и мир', 'Фантастика', 'Фантастика')
    ])
    def test_set_book_genre(self, book_name, genre, expected_genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == expected_genre

    @pytest.mark.parametrize("genre, expected_books", [
        ('Фантастика', ['Гордость и предубеждение и зомби']),
        ('Комедии', ['Что делать, если ваш кот хочет вас убить']),
        ('Детективы', [])
    ])
    def test_get_books_with_specific_genre(self, genre, expected_books):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Комедии')
        books = collector.get_books_with_specific_genre(genre)
        assert books == expected_books

    @pytest.mark.parametrize("book_name, genre, expected_books_for_children", [
        ('Гордость и предубеждение и зомби', 'Фантастика', ['Гордость и предубеждение и зомби']),
        ('Что делать, если ваш кот хочет вас убить', 'Комедии', ['Что делать, если ваш кот хочет вас убить'])
    ])
    def test_get_books_for_children(self, book_name, genre, expected_books_for_children):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        books_for_children = collector.get_books_for_children()
        assert books_for_children == expected_books_for_children

    @pytest.mark.parametrize("book_name, expected_in_favorites", [
        ('Гордость и предубеждение и зомби', True),
        ('Что делать, если ваш кот хочет вас убить', False)
    ])
    def test_add_book_in_favorites(self, book_name, expected_in_favorites):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        in_favorites = book_name in collector.get_list_of_favorites_books()
        assert in_favorites == expected_in_favorites

    @pytest.mark.parametrize("book_name, expected_in_favorites", [
        ('Гордость и предубеждение и зомби', False),
        ('Что делать, если ваш кот хочет вас убить', False)
    ])
    def test_delete_book_from_favorites(self, book_name, expected_in_favorites):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')
        in_favorites = book_name in collector.get_list_of_favorites_books()
        assert in_favorites == expected_in_favorites

    def test_get_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Комедии')
        books_genre = collector.get_books_genre()
        assert books_genre == {
            'Гордость и предубеждение и зомби': 'Фантастика',
            'Что делать, если ваш кот хочет вас убить': 'Комедии'
        }

    def test_book_without_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        genre = collector.get_book_genre('Гордость и предубеждение и зомби')
        assert genre == ''

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        favorites_books = collector.get_list_of_favorites_books()
        assert 'Гордость и предубеждение и зомби' in favorites_books