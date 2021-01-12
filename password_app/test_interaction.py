import unittest
from Interaction import Interaction

INT = Interaction()


class TestInteraction(unittest.TestCase):

    def test_creat_line(self):
        creat_line = 'test'
        result = INT.create_line()
        self.expected_output = 'test'
        self.assertEqual(result, f'{creat_line}')

    def test_del_line(self):
        result = INT.del_line()
        del_line = 'test'
        self.expected_output = 'test'
        self.assertEqual(result, f'{del_line} was removed from')

    def test_read_line(self):
        result = INT.read_line()
        read_line = 'test'
        self.expected_output = 'test'
        self.assertEqual(result, f'{read_line}')

    def test_change_line(self):
       result = INT.change_line()
       change_key = 'test'
       self.expected_output = 'test'
       self.assertEqual(result, f'{change_key} was change from storage')


if __name__ == '__main__':
    unittest.main()
