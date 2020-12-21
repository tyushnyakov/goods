from good_info import GoodInfoList


def main():
    goods_list = GoodInfoList()
    goods_list.add_from_file('goods2.info')

    print("Общее количество товаров - {total}".format(total=len(goods_list)))
    print("Средняя цена товара - {mean:.2f}".format(mean=goods_list.get_mean()))
    print("Самые дорогие товары - \n {exp}".format(exp=goods_list.get_expensive()))
    print("Заканчивются товары - \n {end}".format(end=goods_list.get_ending()))
    print("Просроченные товары - \n {}".format(goods_list.get_expired()))
    print(goods_list['свинина 1кг'])


if __name__ == '__main__':
    main()
