from typing import List
from inventory_report.importers import JsonImporter, CsvImporter
from inventory_report.inventory import Inventory
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
# from inventory_report.product import Product


def process_report_request(file_paths: List[str], report_type: str) -> str:
    """
    Process the report given a list of file paths and a report type,
    and returns the result.
    """
    simple_report = SimpleReport()
    complete_report = CompleteReport()
    for file_path in file_paths:
        if file_path.endswith(".json"):
            data_products = JsonImporter(file_path).import_data()
            inventory = Inventory(data_products)
            simple_report.add_inventory(inventory)
            complete_report.add_inventory(inventory)
        elif file_path.endswith(".csv"):
            data_products = CsvImporter(file_path).import_data()
            inventory = Inventory(data_products)
            simple_report.add_inventory(inventory)
            complete_report.add_inventory(inventory)
    return create_report(report_type, simple_report, complete_report)


def create_report(
        report_type: str,
        simple_report: SimpleReport,
        complete_report: CompleteReport) -> str:
    if report_type == "simple":
        return simple_report.generate()
    elif report_type == "complete":
        return complete_report.generate()
    else:
        raise ValueError("Report type is invalid.")
