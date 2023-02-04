class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.__name = name
        self.__author = author

    def __str__(self):
        return f"Книга {self.__name}. Автор {self.__author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.__name!r}, author={self.__author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть целочисленным значением")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным значением")

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.__name!r}, author={self.__author!r}, pages={self.pages!r})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

        if not isinstance(duration, float):
            raise TypeError("Продолжительность аудиокниги должна быть числом с плавающей запятой")
        if duration <= 0:
            raise ValueError("Продолжительность аудиокниги должна быть положительным значением")

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.__name!r}, author={self.__author!r}, duration={self.duration!r})"
