#!/usr/bin/env python
# coding=utf-8

import mock
import unittest


def hello(x, y):
    add = x + y
    mul = world(x, y)
    return add, mul


def world(x, y):
    return x * y + 3


class MyTestCase(unittest.TestCase):
    @mock.patch('test.world')
    def test_hello(self, mock_mul):
        x = 3
        y = 5
        mock_mul.return_value = 15
        add, mul = hello(x, y)
        mock_mul.assert_called_once_with(3, 5)
        self.assertEqual(8, add)
        self.assertEqual(15, mul)


if __name__ == '__main__':
    unittest.main()
