import os
import json
import reporter
import good_db


def get_mean():
    print("Средняя цена товара - {mean:.2f}"
          .format(mean=reporter.goods_list.get_mean()))


def file_to_db(file_path):
    good_db.file_to_db(file_path)


def remove_expensive():
    reporter.goods_list.get_expensive()


def get_expired():
    reporter.goods_list.get_expired()


def complex_function(file_path):
    get_mean()
    file_to_db(file_path)
    remove_expensive()
    get_expired()


def start_reporter():
    reporter.main()


config = {
    "configFile": "config.json",
    "functions": [
        "get_mean",
        "file_to_db",
        "remove_expensive",
        "get_expired",
        "complex_function",
        "start_reporter"
    ],
    "loggingConfig": {
        "filename": "goods.log",
        "filemode": "a",
        "level": "logging.INFO",
        "format": "%(asctime)s %(levelname)s %(filename)s - %(funcName)s - %(message)s"
    }
}


if not os.path.exists('config.json'):
    with open('config.json', 'w') as config_file:
        json.dump(config, config_file, indent=4)

start_reporter()
