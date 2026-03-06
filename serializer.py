import json
from abc import ABC, abstractmethod
from product import (
    Product,
)


class ReadFromFile(ABC):
    """Абстрактный класс для чтения файла."""

    @abstractmethod
    def read_file(self, path_to_file: str) -> None:
        """Метод для чтения данных из файла.

        Args:
            path_to_file: Путь к файлу, из которого мы читаем данные.
        """

        pass


class WriteToFile(ABC):
    """Абстрактный класс для записи данных в файл."""

    @abstractmethod
    def write_file(self, path_to_file: str, products: list[Product]) -> None:
        """Метод для записи данных в файл.

        Args:
            path_to_file: Путь к файлу, в который мы записываем данные.
            products: Список из экземпляров Product.
        """

        pass


class TxtReader(ReadFromFile):
    """Класс для чтения данных из txt."""

    def read_file(self, path_to_file: str) -> list:
        """Метод для чтения данных и преобразования в удобный вид.

        Args:
            path_to_file: Путь к txt-файлу, из которого мы читаем данные.
        """

        with open(path_to_file, 'r') as txt:
            data = txt.readlines()
            del data[0]

        for index in range(len(data)):
            data[index] = data[index].split(';')
        return data


class JsonSerializer(WriteToFile):
    """Класс сериализатора для json-файлов."""

    def write_file(self, path_to_file: str, products: list[Product]) -> None:
        """Метод для записи данных из списка в json.

        Args:
            path_to_file: Путь к json-файлу, в который мы записываем данные.
            products: Список из экземпляров Product.
        """

        with open(path_to_file, 'w') as json_file:
            json.dump(products, json_file, indent=2, ensure_ascii=False)


class JsonDeserializer(ReadFromFile):
    """Класс десериализатора для json-файла."""

    def read_file(self, path_to_file: str) -> dict:
        """Метод чтения данных из json-файла.
        Args:
            path_to_file: Путь к json-файлу, из которого мы читаем данные.
        """

        with open(path_to_file, 'r') as json_file:
            data = json.load(json_file)

        return data
