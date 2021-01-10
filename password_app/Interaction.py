from password_handler import PasswordHandler


storage = {'test': 'abc'}


class Interaction:
    def __init__(self):
        self.ph = PasswordHandler()

    def create_line(self):
        key_sec = input('Enter key: ')
        password_sec = input('Enter password: ')
        if key_sec in storage:
            print('This key is already in use, you can use change_line')
        else:
            return self.ph.create_line(key_sec, password_sec)

    def del_line(self):
        my_key = input('Enter site: ')
        if my_key in storage:
            password = input('Enter password: ')
            if password in storage[my_key]:
                return self.ph.del_line(my_key, password)

            else:
                print("i'm sorry your password don't correct")
        else:
            print("i'm sorry your name don't correct")

    def read_line(self):
        ent_key = input('What key printing: ')
        if ent_key in storage:
            self.ph.read_line(ent_key)

    def change_line(self):
        my_key = input('Enter site: ')
        if my_key in storage:
            old_password = input('Enter old password: ')
            if old_password in storage[my_key]:
                new_password = input('Enter new password: ')
                return self.ph.change_line(my_key, new_password)
            else:
                print("i'm sorry your password don't correct")
        else:
            print("i'm sorry your name don't correct")
