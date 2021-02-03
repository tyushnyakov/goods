from good_info import GoodInfoList, GoodInfo
import logging
import os
import shutil
from good_db import create_tables, config_data

FORMAT = config_data["loggingConfig"]["format"]

logging.basicConfig(filename=config_data["loggingConfig"]["filename"],
                    filemode=config_data["loggingConfig"]["filemode"],
                    level=logging.INFO, format=FORMAT)


def get_goods_list():
    file_path = os.path.abspath(input('Введите путь к файлу:').strip('"\''))
    if not os.path.exists(file_path):
        print('Такого файла нет')
        logging.error('Нет файла {}'.format(file_path))
    elif not os.path.isfile(file_path):
        print('Зто не файл')
        logging.error('{} - не файл'.format(file_path))
    else:
        shutil.copy(file_path, 'data')
        goods_list = GoodInfoList()
        goods_list.add_from_file(file_path)
        return goods_list


goods_list = get_goods_list()


def main():
    logging.info('Program started')

    create_tables()

    if goods_list:
        print("Общее количество товаров - {total}".format(total=len(goods_list)))
        print("Средняя цена товара - {mean:.2f}".format(mean=goods_list.get_mean()))
        print(goods_list.get_std())
        print("Самые дорогие товары - \n {exp}".format(exp=goods_list.get_expensive()))
        print("Заканчивются товары - \n {end}".format(end=goods_list.get_ending()))
        print("Просроченные товары - \n {}".format(goods_list.get_expired()))
        print(goods_list['свинина 1 кг'])

    logging.info('Program finished')


if __name__ == '__main__':
    main()
