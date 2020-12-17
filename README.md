# GOODS
Python project for processing goods information

- [About](#1)
- [Class GoodInfo](#2)
- [Class GoodInfoList](#3)
- [Function get_data](#4)
- [Function create_good_info](#5)

## <a name="1">About</a>
This program processes text file with goods data
and outputs their total number, mean price,
the most expensive product name and price,
name and quantity for the least item.

## <a name="2">Class GoodInfo</a>
Creates instance of goods with name, quantity and price properties.

    :param name: name of product
    :type name: str
    :param count: quantity of product
    :type name: int
    :param cost: price of product
    :type cost: float
  
## <a name="3">Class GoodInfoList</a>
 Processes list of goods with name, quantity and price properties.

        Realizes methods: get most expensive goods; get cheapest goods;
        get end product list; sort goods list by the name, count or cost;
        add product; remove product; remove most expensive product;
        get product by the index; get standard deviation of prices;
        remove last product.

        :param goods: list of goods
        :type goods: list
        
