import unittest
from password_app.password_handler import PasswordHandler

handler = PasswordHandler()
data_create_line = {'google': 'we_wr', '123': '456', 'ASD': 'DFG', '__123__': '__456__'}  # ...
expected_create_line = {'google': 'google:we_wr was added to the storage', '123': '123:456 was added to the storage',
                        'ASD': 'ASD:DFG was added to the storage',
                        '__123__': '__123__:__456__ was added to the storage'}
create_test_del_line = {'test': 'test', '__': '__', '123': '123', '!@#': '$%^', '__123__': '__123__'}
expected_del_line = {'test': 'test:test  was removed from storage', '__': '__:__  was removed from storage',
                     '123': '123:', '!@#': '!@#:$%^  was removed from', '__123__': '__123:__123__  was removed from'}
read_test_line = {'test': 'test', '__': '__', '123': '123', '!@#': '$%^', '__123__': '__123__'}

expected_change_line = {'test': 'test:test was change from storage', '__': '__:__ was change from storage',
                        '123': '123:123 was change from storage', '!@#': '!@#:$%^ was removed from',
                        '__123__': '__123:__123__ was removed from'}


class TestPassword(unittest.TestCase):

    # def test_creat_line(self):
    #     for (key, val) in data_create_line.items():
    #         result = handler.create_line(key, val)
    #         self.assertEqual(result, expected_create_line[key])

    # def test_del_line(self):
    #     for (key, val) in create_test_del_line.items():
    #         result = handler.create_line(key, val)
    #         self.assertEqual(result, expected_del_line[key])
    #
    # def test_read_line(self):
    #     for (key, val) in create_test_del_line.items():
    #         result = handler.create_line(key, val)
    #         self.assertEqual(result, read_test_line[key])

    # def test_change_line(self):
    #     for (key, val) in create_test_del_line.items():
    #         result = handler.create_line(key, val)
    #         self.assertEqual(result, handler.change_line[key])
