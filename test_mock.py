# coding=utf-8

from mock import MagicMock, patch
import test_client
# from test_client import Foo


class ProductionClass:
    def method(self):
        self.something(1, 2, 3)

    def closer(self, something):
        something.close()


real = ProductionClass()
mock = MagicMock()
real.closer(mock)
mock.close.assert_called_with()


def some_function():
    instance = test_client.Foo()
    return instance.method()


with patch('test_client.Foo') as mock:
    instance = mock.return_value
    instance.method.return_value = 'fuck'
    result = some_function()
    assert result == 'fuck'
