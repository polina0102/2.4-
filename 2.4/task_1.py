
class Automobile:
    """
    Базовый класс для представления автомобиля.
    Атрибуты:
        brand (str): Марка автомобиля.
        model (str): Модель автомобиля.
        year_of_manufacture (int): Год выпуска автомобиля.
        mileage (float): Пробег автомобиля в километрах.
    """

    def __init__(self, brand: str, model: str, year_of_manufacture: int, mileage: float):
        """
        Конструктор класса Automobile.
        :param brand: Марка автомобиля.
        :param model: Модель автомобиля.
        :param year_of_manufacture: Год выпуска автомобиля.
        :param mileage: Пробег автомобиля в километрах.
        """
        self.brand = brand
        self.model = model
        self.year_of_manufacture = year_of_manufacture
        self.mileage = mileage

    def __str__(self) -> str:
        """
        Возвращает строковое представление автомобиля.
        :return: Строка с описанием автомобиля.
        """
        return f"{self.brand} {self.model} ({self.year_of_manufacture}), пробег: {self.mileage} км"

    def __repr__(self) -> str:
        """
        Возвращает формальное строковое представление автомобиля.
        :return: Формальное строковое представление.
        """
        return f"Automobile(brand={self.brand!r}, model={self.model!r}, year_of_manufacture={self.year_of_manufacture!r}, mileage={self.mileage!r})"

    def increase_mileage(self, distance: float) -> None:
        """
        Увеличивает пробег автомобиля на заданное расстояние.
        :param distance: Расстояние в километрах, на которое нужно увеличить пробег.
        """
        if distance < 0:
            raise ValueError("Расстояние не может быть отрицательным.")
        self.mileage += distance
class PassengerCar(Automobile):
    """
    Дочерний класс для представления легкового автомобиля.
    Атрибуты:
        brand (str): Марка автомобиля.
        model (str): Модель автомобиля.
        year_of_manufacture (int): Год выпуска автомобиля.
        mileage (float): Пробег автомобиля в километрах.
        body_type (str): Тип кузова легкового автомобиля.
    """

    def __init__(self, brand: str, model: str, year_of_manufacture: int, mileage: float, body_type: str):
        """
        Конструктор класса PassengerCar.
        :param brand: Марка автомобиля.
        :param model: Модель автомобиля.
        :param year_of_manufacture: Год выпуска автомобиля.
        :param mileage: Пробег автомобиля в километрах.
        :param body_type: Тип кузова легкового автомобиля.
        """
        super().__init__(brand, model, year_of_manufacture, mileage)
        self.body_type = body_type

    def __str__(self) -> str:
        """
        Возвращает строковое представление легкового автомобиля.
        :return: Строка с описанием легкового автомобиля.
        """
        return f"{super().__str__()}, тип кузова: {self.body_type}"

    def __repr__(self) -> str:
        """
        Возвращает формальное строковое представление легкового автомобиля.
        :return: Формальное строковое представление.
        """
        return f"PassengerCar(brand={self.brand!r}, model={self.model!r}, year_of_manufacture={self.year_of_manufacture!r}, mileage={self.mileage!r}, body_type={self.body_type!r})"

    def increase_mileage(self, distance: float) -> None:
        """
        Увеличивает пробег автомобиля на заданное расстояние.
        Перегруженный метод, который также выводит сообщение о том, что пробег увеличен.
        :param distance: Расстояние в километрах, на которое нужно увеличить пробег.
        """
        super().increase_mileage(distance)
        print(f"Пробег легкового автомобиля {self.brand} {self.model} ({self.year_of_manufacture}) увеличен на {distance} км.")
