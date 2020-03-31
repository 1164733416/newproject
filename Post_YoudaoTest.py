import unittest
from unittest import mock

from get_post import *


class YoudaoPost(unittest.TestCase):

    def test_get_ts(self):
        # import time
        # t = time.time()
        # ts = str(int(round(t * 1000)))
        # print(ts)
        get_ts =mock.Mock(return_value='1585622797941')

        self.assertEquals('1585622797941', get_ts())


if __name__ == '__main__':
    unittest.main()
