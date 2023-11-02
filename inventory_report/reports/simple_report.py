from inventory_report.inventory import Inventory
from inventory_report.product import Product
from inventory_report.reports.report import Report
from datetime import datetime, date


class SimpleReport(Report):
    def __init__(self) -> None:
        self.inventorys: list[Inventory] = []

    def add_inventory(self, inventory: Inventory) -> None:
        self.inventorys.append(inventory)

    def generate(self) -> str:
        return (
            f'Oldest manufacturing date: {self.get_oldest_manufacturing()}\n'
            f'Closest expiration date: {self.get_closest_expiration_date()}\n'
            f'Company with the largest inventory:'
            f' {self.get_company_larg_inventory()}'
        )

    def get_all_products(self) -> list[Product]:
        all_products: list[Product] = []
        for inventory in self.inventorys:
            for product in inventory.data:
                all_products.append(product)
        return all_products

    def get_oldest_manufacturing(self) -> str:
        all_products = self.get_all_products()
        oldest_manufacturing = sorted(
            all_products,
            key=lambda x: x.manufacturing_date)[0].manufacturing_date
        return oldest_manufacturing

    def get_closest_expiration_date(self) -> str:
        today = date.today()
        all_products = self.get_all_products()
        filter_all_products = [
            product for product in all_products
            if datetime.strptime(
                product.expiration_date, "%Y-%m-%d").date() > today]
        closest_expiration_date = sorted(
            filter_all_products,
            key=lambda x: x.expiration_date)[0].expiration_date
        return closest_expiration_date

    def get_company_larg_inventory(self) -> str:
        all_companys: list[str] = []
        all_products = self.get_all_products()
        for product in all_products:
            all_companys.append(product.company_name)
        company_largest_inventory = max(
            all_companys,
            key=all_companys.count)
        return company_largest_inventory


if __name__ == "__main__":
    inventory1 = Inventory()
    inventory1.add_data([
        Product(
            id="1",
            product_name="Arroz",
            company_name="Marca",
            manufacturing_date="2020-10-10",
            expiration_date="2023-10-10",
            serial_number="123456",
            storage_instructions="Manter em local seco e arejado.",
        ),
        Product(
            id="2",
            product_name="Feijão",
            company_name="São Braz",
            manufacturing_date="2020-02-25",
            expiration_date="2024-12-25",
            serial_number="123456",
            storage_instructions="Manter em local seco e arejado.",
        ),
    ])

    inventory2 = Inventory()
    inventory2.add_data([
        Product(
            id="3",
            product_name="Arroz",
            company_name="São Braz",
            manufacturing_date="2017-06-17",
            expiration_date="2020-06-17",
            serial_number="123456",
            storage_instructions="Manter em local seco e arejado.",
        ),
        Product(
            id="4",
            product_name="Feijão",
            company_name="São Braz",
            manufacturing_date="2017-06-15",
            expiration_date="2023-12-25",
            serial_number="123456",
            storage_instructions="Manter em local seco e arejado.",
        ),
    ])

    report = SimpleReport()
    report.add_inventory(inventory1)
    report.add_inventory(inventory2)
    # print(report.get_oldest_manufacturing())
    # print(report.get_closest_expiration_date())
    # print(report.get_company_larg_inventory())
    print(report.generate())
