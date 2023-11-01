from typing import Dict, Type
from abc import ABC, abstractmethod
from inventory_report.product import Product
import json


class Importer(ABC):
    def __init__(self, path: str) -> None:
        self.path = path

    @abstractmethod
    def import_data(self) -> list[Product]:
        ...


class JsonImporter(Importer):
    def import_data(self) -> list[Product]:
        with open(self.path, "r") as file:
            json_data = json.load(file)
        list_products: list[Product] = []
        for product in json_data:
            # **params desempacota o dicionário product em argumentos nomeados
            list_products.append(Product(**product))
        return list_products


class CsvImporter(Importer):
    pass


# Não altere a variável abaixo

IMPORTERS: Dict[str, Type[Importer]] = {
    "json": JsonImporter,
    "csv": CsvImporter,
}


if __name__ == "__main__":
    path = "inventory_report/data/inventory.json"
    instance_json_importer = JsonImporter(path)
    print(instance_json_importer.import_data())
