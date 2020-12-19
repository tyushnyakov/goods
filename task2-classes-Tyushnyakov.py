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

    def __init__(self, name, cost, count):
        self.name = name
        self.cost = cost
        self.count = count

    def __str__(self):
        return "Товар:{name} Цена: {cost} Количество: {count}"\
            .format(name=self.name, cost=self.cost, count=self.count)


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

    def __init__(self, goods=[]):
        self.goods = goods

    def __str__(self):
        return '\n'.join(str(item) for item in self.goods)

    def __getitem__(self, index):
        return self.goods[index]

    def __len__(self):
        return len(self.goods)

    def add_from_file(self, data_file):
        """
        This method gets goods data from the text file, transform text data

        into new GoodInfo objects and add them to the GoodInfoList

        :param data_file: path to file
        :type data_file: string
        """
        open_file = open(data_file, "r", encoding="utf-8")
        rows = open_file.readlines()
        open_file.close()

        for row in rows:
            list_row = row.split(":")
            list_row[2] = list_row[2].replace("\n", "")
            if len(list_row) < 3:
                print("Нет данных о товаре")
            elif any(x.name == list_row[0] for x in self.goods):
                print("Такой товар уже есть!")
            elif not list_row[1].isdigit() or not list_row[2].isdigit():
                print("Неверный формат данных")
            name = list_row[0]
            cost = float(list_row[1])
            count = int(list_row[2])
            self.add(GoodInfo(name, cost, count))

    def get_mean(self):
        """
        This method calculates mean price of goods in list

        :return: mean price of goods in list
        :rtype: float
        """
        return sum([item.cost for item in self.goods]) / len(self.goods)

    def get_std(self):
        """
        This method calculates standard deviation of product prices

        :return: standard deviation of product prices
        :rtype: float
        """
        return stdev([x.cost for x in self.goods])

    def sort_goods(self, sort_key):
        """
        This method sort list by the name, count or cost

        :param sort_key: sort key as string
        :type sort_key: str
        :return: sorted list of goods
        :rtype: list
        """
        if sort_key == 'name':
            self.goods.sort(key=lambda x: x.name)
        if sort_key == 'cost':
            self.goods.sort(key=lambda x: x.cost)
        if sort_key == 'count':
            self.goods.sort(key=lambda x: x.count)
        return self

    def get_expensive(self):
        """
        This method get most expensive goods from the list

        :return: most expensive goods list
        :rtype: list
        """
        self.sort_goods('cost')
        highest_cost = self.goods[-1].cost
        goods = [x for x in self.goods if x.cost == highest_cost]
        return GoodInfoList(goods)

    def get_cheapest(self):
        """
        This method get cheapest goods from the list

        :return: cheapest goods list
        :rtype: list
        """
        self.sort_goods('cost')
        lowest_cost = self.goods[0].cost
        goods = [x for x in self.goods if x.cost == lowest_cost]
        return GoodInfoList(goods)

    def get_ending(self):
        """
        This method get ending goods from the list

        :return: ending goods list
        :rtype: list
        """
        self.sort_goods('count')
        minimal_count = self.goods[0].count
        goods = [x for x in self.goods if x.count == minimal_count]
        return GoodInfoList(goods)

    def add(self, product):
        """
        This method add product to the goods list

        :param product: product to add as instance of GoodInfo
        :type product: object
        """
        self.goods.append(product)

    def remove(self, name):
        """
        This method remove product from the goods list

        :param name: product name to remove
        :type name: str
        """
        self.goods = [item for item in self.goods if item.name != name]

    def remove_expensive(self):
        """
        This method remove most expensive product from the goods list

        :return: most expensive product from the goods list
        :rtype: object
        """
        self.sort_goods('cost')
        return self.goods.pop()

    def remove_last(self):
        """
        This method remove last product from the goods list

        :return: last product from the goods list
        :rtype: object
        """
        return self.goods.pop()


goods_list = GoodInfoList()
goods_list.add_from_file('goods')

print("Общее количество товаров - {total}".format(total=len(goods_list)))
print("Средняя цена товара - {mean:.2f}".format(mean=goods_list.get_mean()))
print("Самые дорогие товары - \n {exp}".format(exp=goods_list.get_expensive()))
print("Заканчивются товары - \n {end}".format(end=goods_list.get_ending()))