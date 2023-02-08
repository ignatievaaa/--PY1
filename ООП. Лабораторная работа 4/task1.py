import doctest


class Automobile:
    """
    Создание и подготовка к работе базового класса "Автомобиль"

    :param count: Средняя стоимость автомобиля
    :param model: Модель автомобиля

    Пример:
    >>> automobile = Automobile(5500000, "Audi")  # инициализация экземпляра класса
     """
    def __init__(self, count: int, model: str):
        if count < 0:
            raise ValueError("Средняя стоимость автомобиля не может быть отрицательным числом")
        self.count = count

        if not isinstance(model, str):
            raise TypeError("Модель автомобиля должна быть типа данных str")
        self.model = model

    def automobiles_to_buy(self) -> None:
        """
        Количество купленных автомобилей.

        Примеры:
        >>> automobile = Automobile(5500000, "Audi")
        >>> automobile.automobiles_to_buy()
        """
        ...

    def new_model(self) -> bool:
        """
        Функция, которая проверяет является ли автомобиль новой моделью.

        :return: Является автомобиль новой моделью

        Примеры:
        >>> automobile = Automobile(5500000, "Audi")
        >>> automobile.new_model()
        """
        ...

    def __str__(self) -> str:
        return f"Средняя стоимость автомобиля - {self.count}. Модель - {self.model}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(count={self.count!r}, model={self.model!r})"


class PassengerCar(Automobile):
    """
    Создание и подготовка к работе дочернего класса "Легковой автомобиль"

    :param count: Средняя стоимость легкового автомобиля
    :param model: Модель автомобиля

    Примеры:
    >>> passenger_car = PassengerCar(5500000, "Audi")  # инициализация экземпляра класса
         """
    def __init__(self, count: int, model: str):
        super().__init__(count, model)

    def automobiles_to_buy(self) -> None:
        """
        Количество купленных легковых автомобилей.
        Перегружаем метод, так как речь идет о продаже легковых автомобилей.

        Примеры:
        >>> automobile = Automobile(5500000, "Audi")
        >>> automobile.automobiles_to_buy()
        """
        ...

    def __str__(self) -> str:
        # Метод необходимо перегрузить, так как изменилось название объекта
        return f"Средняя стоимость легкового автомобиля - {self.count}. Модель - {self.model}"


if __name__ == "__main__":
    doctest.testmod()
