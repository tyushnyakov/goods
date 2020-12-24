from good_info import GoodInfoList
import logging
import os
import shutil

FORMAT = '%(asctime)s %(levelname)s %(filename)s - %(funcName)s - %(message)s'
logging.basicConfig(filename="goods.log", filemode='w', level=logging.INFO, format=FORMAT)


def main():
    logging.info('Program started')

    file_path = os.path.abspath(input('Введите путь к файлу:'))
    if not os.path.exists(file_path):
        print('Такого файла нет')
        logging.error('Такого файла нет')
    elif not os.path.isfile(file_path):
        print('Зто не файл')
        logging.error('Зто не файл')
    try:
        with open(file_path) as file:
            shutil.copy(file_path, 'data')
    except:
        print('Не удалось открыть файл')
        logging.error('Не удалось открыть файл')

    goods_list = GoodInfoList()
    goods_list.add_from_file(file_path)

    print("Общее количество товаров - {total}".format(total=len(goods_list)))
    print("Средняя цена товара - {mean:.2f}".format(mean=goods_list.get_mean()))
    print("Самые дорогие товары - \n {exp}".format(exp=goods_list.get_expensive()))
    print("Заканчивются товары - \n {end}".format(end=goods_list.get_ending()))
    print("Просроченные товары - \n {}".format(goods_list.get_expired()))
    print(goods_list['свинина 1кг'])
    logging.info('Program finished')


if __name__ == '__main__':
    main()
