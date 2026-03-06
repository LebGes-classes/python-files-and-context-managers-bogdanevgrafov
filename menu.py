from product import (
    EmptyError,
    NegativeNumberError,
    Product,
)
from evgrafov_project.serializer import (
    JsonSerializer,
)


class Menu:
    """Класс меню для карточек товара."""

    def __init__(self, products: list[Product] = []):
        """Инициализация меню.

        Args:
            products: Список объектов Product.
        """

        self.products = products
        self.ids = [product.get_id() for product in products]
        self.is_run = True
        self.is_product_change = True
        self.json_serializer = JsonSerializer()
        self.json_path = None

    def first_menu(self) -> None:
        """Главное меню программы."""

        print(
            'Список ID:\n'
            f'{self.ids}'
            '\n1) Выбрать товар из списка.\n'
            '2) Добавить новый товар.\n'
            '3) Выйти из программы.\n'
            '\nВыберите действие:', end=' '
        )

        try:
            choice = int(input())

            if choice not in (1, 2, 3):
                raise ValueError('Введено неверное число')

            match choice:
                case 1:
                    if len(self.products) == 0:
                        print('\nСписок товаров пуст!\n')
                    else:
                        print('\nВведите ID нужного товара:', end=' ')

                        try:
                            ID = input().rstrip()

                            if ID in self.ids:
                                index = self.ids.index(ID)
                                self.main_menu(self.products[index])
                            else:
                                raise NameError('Нет товара с таким ID!')
                        except NameError as e:
                            print(f'Ошибка: {e}')

                case 2:
                    new_number = len(self.products) + 1

                    if new_number < 10:
                        new_id = f'T00{new_number}'
                    elif new_number < 100:
                        new_id = f'T0{new_number}'
                    else:
                        new_id = f'T{new_number}'

                    new_product = Product(new_number, new_id)
                    self.products.append(new_product)
                    self.ids.append(new_id)

                    print(f'Добавлен новый товар с ID {new_id}!\n')

                case 3:
                    self.is_run = False

                    dict_products = self.all_to_dict(self.products)
                    self.json_serializer.write_file(self.json_path, dict_products)

        except Exception as e:
            print(f'Ошибка: {e}')

    def main_menu(self, product: Product) -> None:
        """Меню управления выбранным товаром.

        Args:
            product: Экземпляр товара, который пользователь выбрал.
        """

        self.is_product_change = True

        while self.is_product_change:

            print(
                '\n1) Получить информацию о товаре.\n'
                '2) Изменить название товара.\n'
                '3) Изменить количество товара.\n'
                '4) Изменить состояние товара.\n'
                '5) Изменить поставщика товара.\n'
                '6) Изменить производителя товара.\n'
                '7) Изменить стоимость товара.\n'
                '8) Изменить местоположение товара.\n'
                '9) Изменить город.\n'
                '10) Удалить товар.\n'
                '0) Выйти из меню.\n'
                '\nВыберите действие:', end=' '
            )

            try:
                choice = int(input())

                match choice:

                    case 1:
                        info = product.to_dict()
                        keys = [
                            'Номер', 'ID', 'Наименование', 'Количество',
                            'Состояние', 'Поставщик', 'Производитель',
                            'Стоимость', 'Валюта', 'Местоположение', 'Город'
                        ]
                        values = list(info.values())

                        for i in range(len(keys)):
                            print(f'{keys[i]}: {values[i]}')

                    case 2:
                        print('Введите новое наименование товара:', end=' ')
                        try:
                            name = input()
                            product.set_name(name)
                        except EmptyError as e:
                            print(f'Ошибка: {e}')

                    case 3:
                        print('Введите новое количество товара:', end=' ')
                        try:
                            quantity = int(input())
                            product.set_quantity(quantity)
                        except NegativeNumberError as e:
                            print(f'Ошибка: {e}')

                    case 4:
                        print('Введите новое состояние товара:', end=' ')
                        try:
                            status = input()
                            product.set_status(status)
                        except EmptyError as e:
                            print(f'Ошибка: {e}')

                    case 5:
                        print('Введите нового поставщика:', end=' ')
                        try:
                            supplier = input()
                            product.set_supplier(supplier)
                        except EmptyError as e:
                            print(f'Ошибка: {e}')

                    case 6:
                        print('Введите производителя:', end=' ')
                        try:
                            developer = input()
                            product.set_developer(developer)
                        except EmptyError as e:
                            print(f'Ошибка: {e}')

                    case 7:
                        print('Введите новую стоимость:', end=' ')

                        try:
                            price = float(input())
                            product.set_price(price)
                        except NegativeNumberError as e:
                            print(f'Ошибка: {e}')

                        print('Введите валюту:', end=' ')

                        try:
                            currency = input()
                            product.set_currency(currency)
                        except EmptyError as e:
                            print(f'Ошибка: {e}')

                    case 8:
                        print('Введите новое местоположение:', end=' ')

                        try:
                            locations = ['В пути', 'Склад', 'Магазин', 'Списан']

                            print(
                                '\n1) В пути\n'
                                '2) Склад\n'
                                '3) Магазин\n'
                                '4) Списан\n'
                                'Выберите действие:', end=' '
                            )

                            location = int(input())
                            if 1 <= location <= 4:
                                product.set_location(locations[location - 1])
                            else:
                                raise ValueError('Неверное число!')

                        except ValueError as e:
                            print(f'Ошибка: {e}')

                    case 9:
                        print('Введите город:', end=' ')

                        try:
                            city = input()
                            product.set_city(city)
                        except EmptyError as e:
                            print(f'Ошибка: {e}')

                    case 0:
                        dict_products = self.all_to_dict(self.products)

                        self.json_serializer.write_file(self.json_path, dict_products)
                        self.is_product_change = False

                    case 10:
                        print('Товар удалён!\n')
                        self.ids.remove(product.get_id())
                        self.products.remove(product)
                        self.is_product_change = False

                    case _:
                        print('Неверный пункт меню.')

            except Exception as e:
                print(f'Ошибка: {e}')

    def all_to_dict(self, products):
        """Метод для преобразования списка продуктов в словари."""

        products_dict = [product.to_dict() for product in self.products]

        return products_dict
