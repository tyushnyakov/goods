# This program processes text file with goods data
# and outputs their total number, mean price,
# the most expensive product name and price,
# name and quantity for the least item.
from statistics import stdev


class GoodInfo:
    """
    Creates instance of goods with name, quantity and price properties.

    :param name: name of product
    :type name: str
    :param count: quantity of product
    :type name: int
    :param cost: price of product
    :type cost: float
    """

    def __init__(self, name, count, cost):
        self.name = name
        self.count = count
        self.cost = cost


class GoodInfoList:
    """
        Processes list of goods with name, quantity and price properties.

        Realizes methods: get most expensive goods; get cheapest goods;
        get end product list; sort goods list by the name, count or cost;
        add product; remove product; remove most expensive product;
        get product by the index; get standard deviation of prices;
        remove last product.

        :param goods: list of goods
        :type goods: list
        """

    def __init__(self, goods):
        self.goods = goods

    def __getitem__(self, goods_number):
        return self.goods[goods_number]

    def __len__(self):
        return len(self.goods)

    def get_std(self):
        return stdev([x.cost for x in self.goods])

    def sort_goods(self, sort_key):
        if sort_key == 'name':
            self.goods.sort(key=lambda x: x.name)
        if sort_key == 'count':
            self.goods.sort(key=lambda x: x.count)
        if sort_key == 'cost':
            self.goods.sort(key=lambda x: x.cost)
        return self

    def get_expensive(self):
        self.sort_goods('cost')
        return self.goods[-3:]

    def get_cheapest(self):
        self.sort_goods('cost')
        return self.goods[:3]

    def get_ending(self):
        self.sort_goods('count')
        return self.goods[:3]

    def add(self, product):
        self.goods.append(product)

    def remove(self, name):
        self.goods = [item for item in self.goods if item.name != name]

    def remove_expensive(self):
        self.sort_goods('cost')
        self.goods.pop()

    def remove_last(self):
        self.goods.pop()


def get_data(data_file):
    """
    This function gets data from the text file and returns list of goods

    :param data_file: path to file
    :type data_file: string
    :return: returns list of GoodInfo objects
    :rtype: list of objects
    """
    open_file = open(data_file, "r", encoding="utf-8")
    string_list = open_file.readlines()
    open_file.close()

    goods_list = []
    for string in string_list:
        list_from_string = string.split(":")
        goods_list.append(create_good_info(goods_list, list_from_string))

    return goods_list


def create_good_info(good_info_list, item_list):
    """
    This function transforms string row to instance of GoodInfo object

    :param good_info_list: processed list of GoodInfo objects
    :type good_info_list: list of objects
    :param item_list: row from data file transformed to list of strings
    :type item_list: list of strings
    :return: new GoodInfo object
    """
    item_list[2] = item_list[2].replace("\n", "")
    if len(item_list) < 3:
        print("Нет данных о товаре")
    elif any(x.name == item_list[0] for x in good_info_list):
        print("Такой товар уже есть!")
    elif not item_list[1].isdigit() or not item_list[2].isdigit():
        print("Неверный формат данных")

    return GoodInfo(item_list[0], int(item_list[1]), float(item_list[2]))


goods = get_data("goods")
# total - total count of goods
total = len(goods)
# mean - mean price of goods
mean = sum([item.cost for item in goods]) / total
# max_price - maximal price good
max_price = GoodInfoList(goods).get_expensive()[2]
# min_count - minimal count good
min_count = GoodInfoList(goods).get_ending()[0]

print("Общее количество товаров - {total}".format(total=total))
print("Средняя цена товара - {mean:.2f}".format(mean=mean))
print("Самый дорогой товар - {name}, Цена\
 - {price}".format(name=max_price.name, price=max_price.cost))
print("Заканчивается товар - {name}, Осталось\
 - {count}".format(name=min_count.name, count=min_count.count))
