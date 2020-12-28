from good_info import GoodInfo, GoodInfoList
import unittest


class GoodInfoTest(unittest.TestCase):

    def test_total(self):
        goods_list = GoodInfoList([])
        goods_list.add_from_file('goods2.info')
        self.assertEqual(len(goods_list), 46)

    def test_different(self):
        goods_list = GoodInfoList([])
        goods_list.add_from_file('goods2.info')
        self.assertEqual(len(goods_list['морковь 1кг']), 2)

    def test_mean(self):
        goods_list = GoodInfoList([])
        goods_list.add_from_file('goods2.info')
        self.assertEqual(goods_list.get_mean(), 98.50)

    def test_std(self):
        goods_list = GoodInfoList([])
        goods_list.add_from_file('goods2.info')
        self.assertEqual(goods_list.get_std(), 95.37965075307089)

    def test_expensive(self):
        goods_list = GoodInfoList([])
        goods_list.add_from_file('goods2.info')
        self.assertEqual(str(goods_list.get_expensive()),
                         'Товар:рыба мороженая, Кета 1кг Цена: 400.0 '
                         'Количество: 5 Произведен:2020-12-30 '
                         'Поставка: 2020-12-30 Срок годности 90 дней')

    def test_ending(self):
        goods_list = GoodInfoList([])
        goods_list.add_from_file('goods2.info')
        self.assertEqual(str(goods_list.get_ending()),
                         'Товар:пирожки с картошкой Цена: 30.0 '
                         'Количество: 2 Произведен:2020-12-30 '
                         'Поставка: 2020-12-30 Срок годности 7 дней')

    def test_sort(self):
        goods_list = GoodInfoList([])
        goods_list.add_from_file('goods2.info')
        self.assertEqual(str(goods_list.sort_goods('name')[0]),
                         'Товар:Чай зеленый Lipton 10 пак. Цена: 60.0 '
                         'Количество: 20 Произведен:2020-12-30 '
                         'Поставка: 2020-12-30 Срок годности 1080 дней')

    def test_without_name(self):
        goods_list = GoodInfoList([])
        goods_list.add_from_file('goods2.info')
        with self.assertRaises(TypeError):
            goods_list.add(GoodInfo(10, 10, '2020-12-30', '2020-12-30', 30))

    def test_wrong_expiration(self):
        goods_list = GoodInfoList([])
        goods_list.add_from_file('goods2.info')
        goods_list.add(GoodInfo('хлеб', 10, 10,
                                '2020-12-30', '2020-12-30', -30))
        self.assertNotEqual(goods_list[-1],
                            GoodInfo('хлеб', 10, 10,
                                     '2020-12-30', '2020-12-30', -30))

    def test_add_expired(self):
        goods_list = GoodInfoList([])
        goods_list.add_from_file('goods2.info')
        goods_list.add(GoodInfo('хлеб', 10, 10,
                                '2020-12-20', '2020-12-30', 3))
        self.assertNotEqual(goods_list[-1],
                            GoodInfo('хлеб', 10, 10,
                                     '2020-12-20', '2020-12-30', 3))

    def test_negative_cost(self):
        goods_list = GoodInfoList([])
        goods_list.add_from_file('goods2.info')
        goods_list.add(GoodInfo('хлеб', -10, 10,
                                '2020-12-30', '2020-12-30', 30))
        self.assertNotEqual(goods_list[-1],
                            GoodInfo('хлеб', -10, 10,
                                     '2020-12-30', '2020-12-30', 30))

    def test_negative_count(self):
        goods_list = GoodInfoList([])
        goods_list.add_from_file('goods2.info')
        goods_list.add(GoodInfo('хлеб', 10, -10,
                                '2020-12-30', '2020-12-30', 30))
        self.assertNotEqual(goods_list[-1],
                            GoodInfo('хлеб', 10, -10,
                                     '2020-12-30', '2020-12-30', 30))

    def test_remove(self):
        goods_list = GoodInfoList([])
        goods_list.add_from_file('goods2.info')
        goods_list.remove('свинина 1кг')
        self.assertFalse(goods_list['свинина 1кг'])

    def test_remove_expensive(self):
        goods_list = GoodInfoList([])
        goods_list.add_from_file('goods2.info')
        self.assertEqual(str(goods_list.remove_expensive()),
                         'Товар:рыба мороженая, Кета 1кг Цена: 400.0 '
                         'Количество: 5 Произведен:2020-12-30 '
                         'Поставка: 2020-12-30 Срок годности 90 дней')

    def test_sell_one(self):
        goods_list = GoodInfoList([])
        goods_list.add_from_file('goods2.info')
        self.assertEqual(goods_list.sell('говядина 1кг', 1), 250)

    def test_sell_more(self):
        goods_list = GoodInfoList([])
        goods_list.add_from_file('goods2.info')
        self.assertFalse(goods_list.sell('говядина 1кг', 100))

    def test_sell_not_exist(self):
        goods_list = GoodInfoList([])
        goods_list.add_from_file('goods2.info')
        self.assertFalse(goods_list.sell('черешня', 1))

    def test_sell_absent(self):
        goods_list = GoodInfoList([])
        goods_list.add_from_file('goods2.info')
        goods_list.sell('баранина 1кг', 10)
        self.assertFalse(goods_list.sell('баранина 1кг', 10))

    def test_read_file(self):
        goods_list = GoodInfoList([])
        goods_list.add_from_file('goods2.info')
        self.assertEqual(len(goods_list), 46)

    def test_read_empty(self):
        goods_list = GoodInfoList([])
        goods_list.add_from_file('goods2.info')
        self.assertNotEqual(str(goods_list[-2]), '')

    def test_read_colons(self):
        goods_list = GoodInfoList([])
        goods_list.add_from_file('goods2.info')
        self.assertNotEqual(str(goods_list[-1]),
                            'Товар: Цена: Количество: Произведен: '
                            'Поставка: Срок годности  дней')


if __name__ == '__main__':
    unittest.main()
