# This program processes text file with goods data
# and outputs their total number, mean price,
# the most expensive product name and price,
# name and quantity for the least item.
from statistics import stdev
from datetime import date, timedelta
import logging


class GoodInfo:
    """
    Creates instance of goods with name, quantity, price,

    delivery date and expiration date properties.

    :param name: name of product
    :type name: str
    :param count: quantity of product
    :type name: int
    :param cost: price of product
    :type cost: float
    :param delivery: product delivery date
    :type cost: str
    :param expiration: product expiration date as integer days
    :type cost: int
    """

    def __init__(self, name, cost, count, made_date,
                 delivery_date, expiration_time):
        """
        Initialize instance of class with name, cost, count,

        made abd delivery dates, expiration time properties.

        :param name: name of product
        :type name: str
        :param count: quantity of product
        :type name: int
        :param cost: price of product
        :type cost: float
        :param made_date: product made date
        :type cost: str
        :param delivery_date: product delivery date
        :type cost: str
        :param expiration_time: product expiration date as integer days
        :type cost: int
        """
        self.name = name
        self.cost = cost
        self.count = count
        self.made_date = date.fromisoformat(made_date)
        self.delivery_date = date.fromisoformat(delivery_date)
        self.expiration_time = timedelta(days=expiration_time)

    def __str__(self):
        return "Товар:{name} Цена: {cost} Количество: {count} Произведен:"\
               "{made} Поставка: {delivery} Срок годности {expiration} дней"\
               .format(name=self.name, cost=self.cost, count=self.count,
                       made=self.made_date, delivery=self.delivery_date,
                       expiration=self.expiration_time.days)


class GoodInfoList:
    """
    Processes list of goods with name, quantity, price, delivery date

    and expiration date properties.Realizes methods: get most expensive goods;
    get cheapest goods; get end product list; sort goods list by the name,
    count or cost; add product; remove product; remove most expensive product;
    get product by the index; get standard deviation of prices;
    remove last product.

    :param goods: list of goods
    :type goods: list
    """

    def __init__(self, goods=[], revenue=0):
        """
        Initialize instance of class from list of GoodInfo objects

        :param goods: list of goods
        :type goods: list
        """
        self.goods = goods
        self.revenue = revenue

    def __str__(self):
        return '\n'.join(str(item) for item in self.goods)

    def __getitem__(self, key):
        """
        This method gets item by the key: index or name of product

        :param key: product index or name
        :type key: int or str
        :return: object with key index or object(s) with key name
        :rtype: object or list
        """
        if isinstance(key, int):
            return self.goods[key]
        goods = [item for item in self.goods if item.name == key]
        if len(goods) == 1:
            return goods[0]
        return GoodInfoList(goods)

    def __len__(self):
        return len(self.goods)

    def add_from_file(self, data_file):
        """
        This method gets goods data from the text file, transform text data

        into new GoodInfo objects and add them to the GoodInfoList

        :param data_file: path to file
        :type data_file: string
        """
        try:
            open_file = open(data_file, "r", encoding="utf-8")
            rows = open_file.readlines()
            open_file.close()
        except Exception:
            print('Не удалось открыть файл')
            logging.error('Не удалось открыть файл {}'.format(open_file))

        if not rows or len(rows) == 0:
            print('Пустой файл!')
            logging.error('Пустой файл!')
            return
        for row in rows:
            list_row = row.split(":")
            if len(list_row) < 6:
                print("Нет данных о товаре")
                logging.error("Нет данных о товаре")
                continue
            elif not list_row[1].isdigit() or not list_row[2].isdigit():
                print("Неверный формат данных")
                logging.error("Неверный формат данных для {}".format(list_row[0]))
                continue
            list_row[5] = list_row[5].replace("\n", "")
            name = list_row[0]
            cost = float(list_row[1])
            count = int(list_row[2])
            made_date = list_row[3]
            delivery_date = list_row[4]
            expiration_time = int(list_row[5])
            self.add(GoodInfo(name, cost, count, made_date,
                              delivery_date, expiration_time))

    def get_expired(self):
        """
        This method delete expired goods and return them.

        :return: list of expired goods
        :rtype: list
        """
        expired = []
        for product in self.goods:
            if product.made_date + product.expiration_time < date.today():
                expired.append(product)
                self.goods.remove(product)
        return GoodInfoList(expired)

    def get_mean(self):
        """
        This method calculates mean price of goods in list

        :return: mean price of goods in list
        :rtype: float
        """
        if len(self.goods) == 0:
            return 0
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
        if sort_key == 'made':
            self.goods.sort(key=lambda x: x.made_date)
        return self

    def get_expensive(self):
        """
        This method get most expensive goods from the list

        :return: most expensive goods list
        :rtype: list
        """
        self.sort_goods('cost')
        if len(self.goods) > 0:
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
        if len(self.goods) > 0:
            self.sort_goods('count')
            minimal_count = self.goods[0].count
            goods = [x for x in self.goods if x.count == minimal_count]
            return GoodInfoList(goods)

    def is_in(self, product):
        check = self[product.name]
        if isinstance(check, GoodInfo):
            if product.delivery_date == check.delivery_date:
                return True
        else:
            if product.delivery_date in [x.delivery_date for x in check]:
                return True

    def add(self, product):
        """
        This method add product to the goods list

        :param product: product to add as instance of GoodInfo
        :type product: object
        """
        if not product.name:
            print('Ошибка! Нет названия товара!')
            logging.error('Ошибка! Нет названия товара!')
        elif product.cost < 0:
            print('Ошибка! Отрицательная цена!')
            logging.error('Ошибка! Отрицательная цена {}!'
                          .format(product.name))
        elif product.count <= 0:
            print('Ошибка! Количество должно быть > 0!')
            logging.error('Ошибка! Количество {} должно быть > 0!'
                          .format(product.name))
        elif product.delivery_date < date.today():
            print('Ошибка! Дата поставки меньше текущей!')
            logging.error('Ошибка! Дата поставки {date} для {name} меньше текущей!'
                          .format(date=product.delivery_date, name=product.name))
        elif self.is_in(product):
            print('Такой товар уже есть!')
            logging.error('{} - такой товар уже есть!'.format(product.name))
        elif product.expiration_time.days < 0:
            print('Срок годности < 0!')
            logging.error('Срок годности {name} < 0!'.format(name=product.name))
        elif product.made_date + product.expiration_time < date.today():
            print('Товар просрочен!')
            logging.error('Товар {name} просрочен!'.format(name=product.name))
        else:
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

    def sell(self, name, count):
        """
        This method changes GoodInfoList with selling goods.

        Accepts two parameters: selling product name and count.
        Reduces the count of selling product, increases total revenue.
        Earlier made date goods are first for sale.
        Returns sell revenue.

        :param: name: selling product name
        :type: name: str
        :param: count: selling product count
        :type: count: int
        :return: sell revenue
        :rtype: float
        """
        if isinstance(self[name], GoodInfo):
            total_count = self[name].count
            selling_goods = GoodInfoList([self[name]])
        else:
            selling_goods = self[name].sort_goods('made')
            counts = [x.count for x in selling_goods.goods]
            total_count = sum(counts)
        if not selling_goods or total_count == 0:
            print("Нет товара!")
            logging.info("Нет товара {}".format(name))
            return None
        if count > total_count:
            print("Не хватает количества товара!")
            logging.info("Не хватает количества товара {}".format(name))
            return None
        sell_revenue = 0
        sell_count = count
        for item in selling_goods.goods:
            if item.count >= sell_count:
                item.count -= sell_count
                sell_revenue += sell_count * item.cost
                break
            if item.count < sell_count:
                sell_count -= item.count
                sell_revenue += item.count * item.cost
                item.count = 0
        self.revenue += sell_revenue
        return sell_revenue
