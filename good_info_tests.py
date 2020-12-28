from good_info import GoodInfo, GoodInfoList
import unittest


class GoodInfoTest(unittest.TestCase):

    def setUp(self):
        self.goods_list = GoodInfoList([])
        self.goods_list.add_from_file('goods-test.info')

    def test_total(self):
        self.assertEqual(len(self.goods_list), 46)

    def test_different(self):
        self.assertEqual(len(self.goods_list['морковь 1кг']), 2)

    def test_mean(self):
        self.assertEqual(self.goods_list.get_mean(), 98.50)

    def test_std(self):
        self.assertEqual(self.goods_list.get_std(), 95.37965075307089)

    def test_expensive(self):
        self.assertEqual(self.goods_list.get_expensive()[0],
                         GoodInfo('рыба мороженая, Кета 1кг', 400.0,
                                  5, '2020-12-30', '2020-12-30', 90))

    def test_ending(self):
        self.assertEqual(self.goods_list.get_ending()[0],
                         GoodInfo('пирожки с картошкой', 30.0, 2,
                                  '2020-12-30', '2020-12-30', 7))

    def test_sort(self):
        self.assertEqual(self.goods_list.sort_goods('name')[0],
                         GoodInfo('Чай зеленый Lipton 10 пак.', 60.0,
                                  20, '2020-12-30', '2020-12-30',1080))

    def test_without_name(self):
        with self.assertRaises(TypeError):
            self.goods_list.add(GoodInfo(10, 10, '2020-12-30', '2020-12-30', 30))

    def test_wrong_expiration(self):
        self.goods_list.add(GoodInfo('хлеб', 10, 10,
                                '2020-12-30', '2020-12-30', -30))
        self.assertNotEqual(self.goods_list[-1],
                            GoodInfo('хлеб', 10, 10,
                                     '2020-12-30', '2020-12-30', -30))

    def test_add_expired(self):
        self.goods_list.add(GoodInfo('хлеб', 10, 10,
                                '2020-12-20', '2020-12-30', 3))
        self.assertNotEqual(self.goods_list[-1],
                            GoodInfo('хлеб', 10, 10,
                                     '2020-12-20', '2020-12-30', 3))

    def test_negative_cost(self):
        self.goods_list.add(GoodInfo('хлеб', -10, 10,
                                '2020-12-30', '2020-12-30', 30))
        self.assertNotEqual(self.goods_list[-1],
                            GoodInfo('хлеб', -10, 10,
                                     '2020-12-30', '2020-12-30', 30))

    def test_negative_count(self):
        self.goods_list.add(GoodInfo('хлеб', 10, -10,
                                '2020-12-30', '2020-12-30', 30))
        self.assertNotEqual(self.goods_list[-1],
                            GoodInfo('хлеб', 10, -10,
                                     '2020-12-30', '2020-12-30', 30))

    def test_zero_count(self):
        self.goods_list.add(GoodInfo('хлеб', 10, 0, '2020-12-30',
                                '2020-12-30', 30))
        self.assertNotEqual(self.goods_list[-1],
                            GoodInfo('хлеб', 10, 0, '2020-12-30',
                                     '2020-12-30', 30))

    def test_remove(self):
        self.goods_list.remove('свинина 1кг')
        self.assertFalse(self.goods_list['свинина 1кг'])

    def test_remove_expensive(self):
        self.assertEqual(str(self.goods_list.remove_expensive()),
                         'Товар:рыба мороженая, Кета 1кг Цена: 400.0 '
                         'Количество: 5 Произведен:2020-12-30 '
                         'Поставка: 2020-12-30 Срок годности 90 дней')

    def test_sell_one(self):
        self.assertEqual(self.goods_list.sell('говядина 1кг', 1), 250)

    def test_sell_more(self):
        self.assertFalse(self.goods_list.sell('говядина 1кг', 100))

    def test_sell_not_exist(self):
        self.assertFalse(self.goods_list.sell('черешня', 1))

    def test_sell_absent(self):
        self.goods_list.sell('баранина 1кг', 10)
        self.assertFalse(self.goods_list.sell('баранина 1кг', 10))

    def test_read_file(self):
        self.assertEqual(len(self.goods_list), 46)

    def test_read_empty(self):
        self.assertNotEqual(str(self.goods_list[-2]), '')

    def test_read_colons(self):
        self.assertNotEqual(str(self.goods_list[-1]),
                            'Товар: Цена: Количество: Произведен: '
                            'Поставка: Срок годности  дней')


if __name__ == '__main__':
    unittest.main()
