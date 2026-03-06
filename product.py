class NegativeNumberError(Exception):
    """Ошибка невозможности использования отрицательного числа."""

    pass


class LocationError(Exception):
    """Ошибка статуса товара."""

    pass


class EmptyError(Exception):
    """Ошибка пустого названия товара."""

    pass


class Product:
    """Класс товара."""

    def __init__(
            self,
            number: int = None,
            id: str = 'None',
            name: str = 'None',
            quantity: int = 0,
            status: str = 'None',
            supplier: str = 'None',
            developer: str = 'None',
            price: float = 0.00,
            currency: str = 'None',
            location: str = 'None',
            city: str = 'None',
    ) -> None:
        """Инициализация конструктора класса.

        Args:
            number: Порядковый номер товара
            id: Уникальный идентификатор товара
            name: Наименование
            quantity: Количество
            status: Состояние
            supplier: Поставщик
            developer: Производитель
            price: Стоимость
            location: Местоположение
            city: Город
        """

        self.number = number
        self.id = id
        self.name = name
        self.quantity = quantity
        self.status = status
        self.supplier = supplier
        self.developer = developer
        self.price = price
        self.currency = currency
        self.location = location
        self.city = city

    def get_number(self) -> int:
        """Геттер для number.

        Returns:
            number: Порядковый номер товара
        """

        return self.number

    def get_name(self) -> str:
        """Геттер для названия.

        Returns:
            name: Название
        """

        return self.name

    def get_id(self) -> str:
        """Геттер для id.

        Returns:
            id: Уникальный идентификатор товара
        """

        return self.id

    def get_quantity(self) -> int:
        """Геттер для quantity.

        Returns:
            quantity: Количество товара
        """

        return self.quantity

    def get_status(self) -> str:
        """Геттер для status.

        Returns:
            status: Состояние товара
        """

        return self.status

    def get_supplier(self) -> str:
        """Геттер для supplier.

        Returns:
            supplier: Поставщик
        """

        return self.supplier

    def get_developer(self) -> str:
        """Геттер для developer.

        Returns:
            developer: Производитель
        """

        return self.developer

    def get_price(self) -> float:
        """Геттер для price.

        Returns:
            price: Стоимость товара
        """

        return self.price

    def get_currency(self) -> str:
        """Геттер для currency.

        Returns:
            currency: Валюта, в которой измеряется стоимость
        """

        return self.currency

    def get_location(self) -> str:
        """Геттер для location.

        Returns:
            location: Местоположение товара
        """

        return self.location

    def get_city(self) -> str:
        """Геттер для city.

        Returns:
            city: Город
        """

        return self.city

    def set_name(self, new_name: str) -> None:
        """Сеттер для названия.

        Args:
            new_name: Новое название
        """

        if len(new_name.strip()) == 0:
            raise EmptyError('Название товара не может быть пустым')
        else:
            self.name = new_name

    def set_quantity(self, new_quantity: int) -> None:
        """Сеттер для количества.

        Args:
            new_quantity: Новое количество
        """

        if new_quantity < 0:
            raise NegativeNumberError('Количество не может быть отрицательным!')
        else:
            self.quantity = new_quantity

    def set_status(self, new_status: str) -> None:
        """Сеттер для статуса товара.

        Args:
            new_status: Новый статус товара.
        """

        if len(new_status.strip()) != 0:
            self.status = new_status
        else:
            raise EmptyError('Строка состояния товара не может быть пустой!')

    def set_supplier(self, new_supplier: str) -> None:
        """Сеттер для поставщика.

        Args:
            new_supplier: Поставщик
        """

        if len(new_supplier.strip()) != 0:
            self.supplier = new_supplier
        else:
            raise EmptyError('Строка поставщика не может быть пустой!')

    def set_developer(self, new_developer: str) -> None:
        """Сеттер для производителя.

        Args:
           new_developer: Производитель
        """

        if len(new_developer.strip()) != 0:
            self.developer = new_developer
        else:
            raise EmptyError('Строка производителя не может быть пустой!')

    def set_price(self, new_price: float) -> None:
        """Сеттер для цены.

        Args:
            new_price: Цена
        """

        if new_price >= 0:
            self.price = new_price
        else:
            raise NegativeNumberError('Стоимость товара не может быть отрицательной!')

    def set_currency(self, new_currency: str) -> None:
        """Сеттер для валюты.

        Args:
            new_currency: Валюта
        """

        if len(new_currency.strip()) != 0:
            self.currency = new_currency
        else:
            raise EmptyError('Стоимость всегда имеет валюту!')

    def set_location(self, new_location: str) -> None:
        """Сеттер для местоположения.

        Args:
            new_location: Местоположение
        """

        if self.location == new_location:
            raise LocationError('Нельзя присвоить товару уже имеющийся статус!')
        elif self.location != 'В пути' and new_location != 'Списан':
            self.location = new_location
        else:
            raise LocationError('Списать товар можно лишь тогда, когда он имеет статус "Склад" или "Магазин"!')

    def set_city(self, new_city: str) -> None:
        """Сеттер для города.

        Args:
            new_city: Город
        """

        if len(new_city.strip()) != 0:
            self.city = new_city
        else:
            raise EmptyError('Название города не может быть пустым!')

    def set_all_attributes_from_txt(self, data: list) -> None:
        """Сеттер для всех значений взятых из txt.

        Args:
            data: Список данных.
        """

        self.number = data[0]
        self.id = data[1]
        self.name = data[2]
        self.quantity = data[3]
        self.status = data[4]
        self.supplier = data[5]
        self.developer = data[6]
        self.price = float(data[7].split(' ')[0])
        self.currency = data[7].split(' ')[1].rstrip('.')
        self.location = data[8]
        self.city = data[9].strip()

    def set_all_attributes_from_dict(self, data: dict) -> None:
        """Сеттер для всех значений, взятых из json.

        Args:
            data: Список данных.
        """

        self.number = data['number']
        self.id = data['id']
        self.name = data['name']
        self.quantity = data['quantity']
        self.status = data['status']
        self.supplier = data['supplier']
        self.developer = data['developer']
        self.price = data['price']
        self.currency = data['currency']
        self.location = data['location']
        self.city = data['city']

    def to_dict(self) -> dict:
        """Получение словаря из всех атрибутов объекта

        Returns:
            dict: Словарь из всех атрибутов
        """
        return self.__dict__
