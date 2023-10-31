from dataclasses import dataclass


@dataclass
class Product:
    id: str
    product_name: str
    company_name: str
    manufacturing_date: str
    expiration_date: str
    serial_number: str
    storage_instructions: str

    def __str__(self) -> str:
        return (
            f"The product {self.id} - {self.product_name} "
            f"with serial number {self.serial_number} "
            f"manufactured on {self.manufacturing_date} "
            f"by the company {self.company_name} "
            f"valid until {self.expiration_date} "
            "must be stored according to the following instructions: "
            f"{self.storage_instructions}."
        )


if __name__ == "__main__":
    instance_product = Product(
        id="1",
        product_name="Arroz",
        company_name="Marca",
        manufacturing_date="10/10/2020",
        expiration_date="10/10/2021",
        serial_number="123456",
        storage_instructions="Manter em local seco e arejado.",
    )
    print(instance_product)
