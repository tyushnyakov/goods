# GOODS
Python project for processing goods information

- [About](#1)
- [Class GoodInfo][2]
- [Class GoodInfoList][3]
- [Function get_data][4]
- [Function create_good_info][5]

## <a name="1">About</a>
This program processes text file with goods data
and outputs their total number, mean price,
the most expensive product name and price,
name and quantity for the least item.

## [2]Class GoodInfo
Creates instance of goods with name, quantity and price properties.

    :param name: name of product
    :type name: str
    :param count: quantity of product
    :type name: int
    :param cost: price of product
    :type cost: float
  
## [3]Class GoodInfoList
 Processes list of goods with name, quantity and price properties.

        Realizes methods: get most expensive goods; get cheapest goods;
        get end product list; sort goods list by the name, count or cost;
        add product; remove product; remove most expensive product;
        get product by the index.

        :param goods: list of goods
        :type goods: list
        
## [4]Function get_data
This function gets data from the text file and returns list of goods

    :param data_file: path to file
    :type data_file: string
    :return: returns list of GoodInfo objects
    :rtype: list of objects
    
## [5]Function create_good_info
This function transforms string row to instance of GoodInfo object

    :param good_info_list: processed list of GoodInfo objects
    :type good_info_list: list of objects
    :param item_list: row from data file transformed to list of strings
    :type item_list: list of strings
    :return: new GoodInfo object
