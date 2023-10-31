from inventory_report.product import Product


def test_create_product() -> None:
    # criando um dicionário com os parâmetros do construtor da classe Product
    params = {
        "id": "1",
        "product_name": "Arroz",
        "company_name": "Marca",
        "manufacturing_date": "10/10/2020",
        "expiration_date": "10/10/2021",
        "serial_number": "123456",
        "storage_instructions": "Manter em local seco e arejado.",
    }
    # **params expande o dicionário params em argumentos nomeados
    instance_product = Product(**params)
    assert instance_product.id == "1"
    assert instance_product.product_name == "Arroz"
    assert instance_product.company_name == "Marca"
    assert instance_product.manufacturing_date == "10/10/2020"
    assert instance_product.expiration_date == "10/10/2021"
    assert instance_product.serial_number == "123456"
    assert (
        instance_product.storage_instructions
        == "Manter em local seco e arejado."
    )
