from Backend.FileHandler.read_from_file import get_data

items_path = 'database/items.json'


def get_sales_data():
    # Mock data for demonstration

    items = get_data(items_path)

    return items
