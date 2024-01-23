from unittest import TestCase
from UniHm import Google


class TestHM(TestCase):
    def test_add_existing(self):
        test_list = Google()
        test_list.insert('Bob')
        with self.assertRaises(ValueError) as ex:
            test_list.insert('Bob')
        self.assertEqual('Bob is already exist', ex.exception.args[0])

    def test_rem_not_existing(self):
        test_list = Google()
        test_list.insert('Bob')
        with self.assertRaises(ValueError) as ex:
            test_list.remover('Bob1')
        self.assertEqual('Bob1 is not exist', ex.exception.args[0])

    def test_rem_from_empty(self):
        test_list = Google()
        with self.assertRaises(ValueError) as ex:
            test_list.remover('Bob1')
        self.assertEqual('Profile list is empty', ex.exception.args[0])

    def test_add(self):
        test_list = Google()
        # test_list.insert('Bob')
        self.assertEqual(test_list.insert('Bob'), None)

    def test_rem(self):
        test_list = Google()
        test_list.insert('Bob')
        self.assertEqual(test_list.remover('Bob'), None)
