from password_app.password_handler import PasswordHandler

ph = PasswordHandler
storage = {'test': 'abc'}


class Interaction:
    def __init__(self):
        self.ph = PasswordHandler

    def logic(self, action):
        if action == 'C':
            key_sec = input('Enter key: ')
            password_sec = input('Enter password: ')
            print('Create action selected')
            if key_sec in storage:
                print('This key is already in use, you can use change_line')
            else:
                cread_line(self, key_sec, password_sec)
        elif action == 'R':
            ent_key = input('What key printing: ')
            if ent_key in storage:
                read_line(self, ent_key)
        elif action == 'U':
            my_key = input('Enter site: ')
            if my_key in storage:
                old_password = input('Enter old password: ')
                if old_password in storage[my_key]:
                    new_password = input('Enter new password: ')

                else:
                    print("i'm sorry your password don't correct")
            else:
                print("i'm sorry your name don't correct")

        elif action == "D":
            del_key = input('Enter site: ')
            if del_key in storage:
                del_password = input('Enter password: ')
                if del_password in storage[del_key]:
                    del_line(self, del_key)
        else:
            return 'User answer is dont usable'

    def create_line(self, key_sec, password_sec):
        self.ph.create_line(key_sec, password_sec)

    def del_line(self, del_key, del_password):
        self.ph.del_line(self, del_key, del_password)

    def read_line(self, ent_key):
        self.ph.read_line(ent_key)

    def change_line(self, new_password):
        self.ph.change_line(self, change_key, new_password)
