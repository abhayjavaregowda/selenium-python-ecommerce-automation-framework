import json

from utils.config_reader import get_test_data_dir


def load_json_file(file_name):
    file_path = get_test_data_dir() / file_name
    with file_path.open(encoding="utf-8") as test_data_file:
        return json.load(test_data_file)


def get_user(user_key):
    return load_json_file("users.json")["users"][user_key]


def get_product(product_key):
    return load_json_file("users.json")["products"][product_key]


def get_checkout_information():
    return load_json_file("users.json")["checkout_information"]
