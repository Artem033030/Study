import unittest
from password_handler import PasswordHandler

from data_test import data_line
from data_test import expected_create_line
from data_test import expected_del_line
from data_test import expected_change_line
from data_test import expected_read_line
handler = PasswordHandler


class TestPassword(unittest.TestCase):

    def test_creat_line(self):
        for (key, val) in data_line.items():
            result = handler.create_line(key, val)
            self.assertEqual(result, expected_create_line[key])

    def test_del_line(self):
        for (key, val) in data_line.items():
            result = handler.create_line(key, val)
            self.assertEqual(result, expected_del_line[key])

    def test_read_line(self):
        for (key, val) in data_line.items():
            result = handler.create_line(key, val)
            self.assertEqual(result, expected_read_line[key])

    def test_change_line(self, password):
        for (key, val) in expected_change_line.items():
            result = handler.create_line(key, val)
            self.assertEqual(result, handler.change_line(key, val))


if __name__ == '__main__':
    unittest.main()
