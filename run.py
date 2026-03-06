from menu import (
    Menu,
)
from product import (
    Product,
)
from serializer import (
    JsonDeserializer,
    JsonSerializer,
    TxtReader,
)

def load_products(path: str) -> list[Product]:
    """Загрузка товаров из json.

    Args:
        path: Путь к json-файлу.

    Returns:
        list[Product]: Список объектов Product.
    """

    products = []

    if path.endswith('.json'):
        reader = JsonDeserializer()
        data = reader.read_file(path)

        for item in data:
            product = Product()
            product.set_all_attributes_from_dict(item)
            products.append(product)
    elif path.endswith('.txt'):
        reader = TxtReader()
        data = reader.read_file(path)

        for item in data:
            product = Product()
            product.set_all_attributes_from_txt(item)
            products.append(product)
    else:
        raise ValueError('Данный тип файла не поддерживается')

    return products

def main():
    """Запуск программы."""

    correct_path = False

    while not correct_path:

        print('Введите полный адрес файла для импорта товаров, если не надо, введите "n":', end=' ')

        path = input()

        if path == 'n':
            menu = Menu()
            correct_path = True

        else:
            try:
                products = load_products(path)
                menu = Menu(products)
                correct_path = True

            except FileNotFoundError:
                print('Ошибка: файл не найден. Попробуйте снова.')

            except Exception as e:
                print(f'Ошибка при чтении файла: {e}')

    print('Введите путь к json файлу, в который будет вестись запись:', end=' ')

    json_path = input()

    if not json_path.endswith('.json'):
        json_path += '.json'

    menu.json_path = json_path

    while menu.is_run:
        menu.first_menu()


main()
