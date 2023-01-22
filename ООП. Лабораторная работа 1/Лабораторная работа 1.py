import doctest


class Book:
    def __init__(self, material: str, pages: int):
        """
        Создание и подготовка к работе объекта "Книга"

        :param material: Материал, из которого сделана обложка книги
        :param pages: Количество страниц в книге

        Примеры:
        >>> book = Book("твердая", 500)  # инициализация экземпляра класса
        """
        if not isinstance(material, str):
            raise TypeError("Материал должен быть типа данных str")
        self.material = material

        if not isinstance(pages, int):
            raise TypeError("Количество страниц в книге должно быть типа int")
        if pages < 0:
            raise ValueError("Количество страниц в книге не может быть отрицательным числом")
        self.pages = pages

    def pages_to_read(self, readen_pages: int) -> None:
        """
        Количество прочитанных страниц.

        :param readen_pages: Количество рочитанных страниц
        :raise ValueError: Если количество прочитанных страниц превышает количество страниц в книге,
        то возвращается ошибка.

        Примеры:
        >>> book = Book("твердая", 500)
        >>> book.pages_to_read(275)
        """
        if not isinstance(readen_pages, int):
            raise TypeError("Количество прочитанных страниц в книге должно быть типа int")
        if readen_pages < 0:
            raise ValueError("Количество прочитанных страниц должно быть положительным числом")
        if readen_pages > self.pages:
            raise ValueError("Количество прочитанных страниц не может превышать общее количество страниц в книге")

        self.pages -= readen_pages


class Fridge:
    def __init__(self, height: int, width: int):
        """
        Создание и подготовка к работе объекта "Холодильник"

        :param height: Высота холодильника, мм
        :param width: Ширина холодильника, мм

        Примеры:
        >>> fridge = Fridge(2000, 500)  # инициализация экземпляра класса
        """
        if not isinstance(height, int):
            raise TypeError("Высота холодильника должна быть целочисленным значением")
        if height <= 0:
            raise ValueError("Высота холодильника должна быть положительным значением")
        self.height = height

        if not isinstance(width, int):
            raise TypeError("Ширина холодильника должна быть целочисленным значением")
        if width <= 0:
            raise ValueError("Ширина холодильника должна быть положительным значением")
        self.width = width

    def close_fridge(self) -> None:
        """
        Закрытие холодильника.

        Примеры:
        >>> fridge = Fridge(2000, 500)
        >>> fridge.close_fridge()
        """
        ...

    def fridge_is_open(self) -> bool:
        """
        Функция, которая проверяет, открыт ли холодильник.

        :return: Является ли холодильник открытым

        Примеры:
       >>> fridge = Fridge(2000, 500)
        >>> fridge.fridge_is_open()
        """
        ...


class Library:
    def __init__(self, shelving_number: int, area: float, name: str):
        """
        Создание и подготовка к работе объекта "Библиотека"

        :param shelving_number: Количество стелллажей
        :param area: Площадь
        :param name: Название библиотеки

        Примеры:
        >>> library = Library(17, 110.3, "Библиотека имени Маяковского")  # инициализация экземпляра класса
        """
        if not isinstance(shelving_number, int):
            raise TypeError("Количество стеллажей должно быть типа int")
        if shelving_number <= 0:
            raise ValueError("Количество стеллажей должно быть положительным числом")
        self.shelving_number = shelving_number

        if not isinstance(area, float):
            raise TypeError("Площадь должна быть типа float")
        if area <= 0:
            raise ValueError("Площадь должна быть положительным числом")
        self.area = area

        if not isinstance(name, str):
            raise TypeError("Название библиотеки должен быть типа str")
        self.name = name

    def library_is_ok(self) -> bool:
        """
        Функция, которая проверяет, все ли в порядке с техническим состоянием зданием.

        :return: в порядке ли техническое состояние здания

        Примеры:
        >>> library = Library(17, 110.3, "Библиотека имени Маяковского")
        >>> library.library_is_ok()
        """
        ...

    def new_books(self, books: int) -> None:
        """
        Количество новых книг в бибилиотеке.

        :param books: Новые книги

        Примеры:
        >>> library = Library(17, 110.3, "Библиотека имени Маяковского")
        >>> library.new_books(25)
        """
        if not isinstance(books, int):
            raise TypeError("Количество новых книг должно быть типа int")
        if books <= 0:
            raise ValueError("Количество новых книг должно быть положительным числом")
        ...


if __name__ == "__main__":
    doctest.testmod()
