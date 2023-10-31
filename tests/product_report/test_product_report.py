from inventory_report.product import Product


def test_product_report() -> None:
    params = {
        "id": "1",
        "product_name": "Arroz",
        "company_name": "Marca",
        "manufacturing_date": "10/10/2020",
        "expiration_date": "10/10/2021",
        "serial_number": "123456",
        "storage_instructions": "Manter em local seco e arejado",
    }
    instance_product = Product(**params)
    assert (
        str(instance_product)
        == "The product 1 - Arroz with serial number 123456 "
        "manufactured on 10/10/2020 by the company Marca "
        "valid until 10/10/2021 must be stored according to the "
        "following instructions: Manter em local seco e arejado."
    )
