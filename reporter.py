from good_info import GoodInfoList, GoodInfo
import logging
import os
import shutil

FORMAT = '%(asctime)s %(levelname)s %(filename)s - %(funcName)s - %(message)s'
logging.basicConfig(filename="goods.log", filemode='a', level=logging.INFO, format=FORMAT)


def main():
    # logging.info('Program started')
    #
    # file_path = os.path.abspath(input('Введите путь к файлу:').strip('"\''))
    # if not os.path.exists(file_path):
    #     print('Такого файла нет')
    #     logging.error('Нет файла {}'.format(file_path))
    # elif not os.path.isfile(file_path):
    #     print('Зто не файл')
    #     logging.error('{} - не файл'.format(file_path))
    # else:
    #     shutil.copy(file_path, 'data')
        goods_list = GoodInfoList()
        goods_list.add_from_file('goods2.info')

        print("Общее количество товаров - {total}".format(total=len(goods_list)))
        # print("Средняя цена товара - {mean:.2f}".format(mean=goods_list.get_mean()))
        # print(goods_list.get_std())
        # print("Самые дорогие товары - \n {exp}".format(exp=goods_list.get_expensive()))
        # print("Заканчивются товары - \n {end}".format(end=goods_list.get_ending()))
        # print("Просроченные товары - \n {}".format(goods_list.get_expired()))
        # print(goods_list['свинина 1 кг'])
        # logging.info('Program finished')
        # print(goods_list.sell('морковь 1кг', 60))
        # print(goods_list.revenue)
        # print(goods_list['морковь 1кг'])
        # goods_list.add(GoodInfo('хлеб', 10, 10, '2020-12-20', '2020-12-30', 30))
        # print(goods_list[-1])
        # print(goods_list.remove_expensive())
        print(goods_list.get_ending())


if __name__ == '__main__':
    main()
