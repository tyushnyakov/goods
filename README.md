# GOODS
Python project for processing goods information

- [About](#1)
- [module good_info](#2)
- [module reporter](#3)

## <a name="1">About</a>
This programm processes text file with goods data.
It consists from two modules: __good_info.py__ and __reporter.py__ and text file __goods2.info__.
Good_info module contains all logic.
Entry point is __reporter.py__.

## <a name="2">module good_info</a>
Includes 2 classes: GoodInfo and GoodInfoList.

###GoodInfo
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

###GoodInfoList
Processes list of goods with name, quantity, price, delivery date
and expiration date properties.Realizes methods: get most expensive goods;
get cheapest goods; get end product list; sort goods list by the name,
count or cost; add product; remove product; remove most expensive product;
get product by the index; get standard deviation of prices; remove last product.

    :param goods: list of goods
    :type goods: list

## <a name="3">module reporter</a>
Entry point. For execution, write in command line reporter.py and press enter.
Executed function main gets data from text file goods2.info and processed it.
Outputs total quantity of goods, mean price, most expensive goods, ending goods,
expired goods and demonstrate work of new GoodInfoList method __getitem__ by product name.
        

