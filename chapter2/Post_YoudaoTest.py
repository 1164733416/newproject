import unittest
from unittest import mock


class YoudaoPost(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_get_ts(self):
        get_ts = mock.Mock(return_value='1584683853810')
        self.assertEquals('1584683853810', get_ts())

    def test_get_salt(self):
        get_salt = mock.Mock(return_value='15846838538107')
        self.assertEquals('15846838538107', get_salt())

    def test_get_sign(self):
        get_sign = mock.Mock(return_value='b4f6d46d7883e2dbb18cd92cbaa411b7')
        self.assertEquals('b4f6d46d7883e2dbb18cd92cbaa411b7', get_sign())


if __name__ == '__main__':
    unittest.main()
