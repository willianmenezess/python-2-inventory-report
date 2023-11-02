from inventory_report.reports.simple_report import SimpleReport
from inventory_report.inventory import Inventory
from inventory_report.product import Product


class CompleteReport(SimpleReport):
    def generate(self) -> str:
        return (
            f'{super().generate()}\n'
            f'{self.get_stocked_by_company()}'
        )

    def get_stocked_by_company(self) -> str:
        all_products = super().get_all_products()
        stocked_by_company: dict[str, int] = {}
        for product in all_products:
            if product.company_name in stocked_by_company:
                stocked_by_company[product.company_name] += 1
            else:
                stocked_by_company[product.company_name] = 1
        sorted_stocked_by_company = sorted(
            stocked_by_company.items(),
            key=lambda x: x[0],
            reverse=True)
        print(sorted_stocked_by_company)
        result_string = 'Stocked products by company:\n'
        for company, quantity in sorted_stocked_by_company:
            result_string += f'- {company}: {quantity}\n'
        return result_string


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

    complete_report = CompleteReport()
    complete_report.add_inventory(inventory1)
    complete_report.add_inventory(inventory2)
    print(complete_report.generate())
