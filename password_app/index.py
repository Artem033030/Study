print('Hello world')
storage = {}


class PasswordHandler:

    def logic(self):

        action = input('What do you want to do (C,R,U,D): ').capitalize()
        if action == 'C':
            print('Create action selected')
            self.creat_storage()
            print(storage)
        elif action == 'R':
            print('Read action selected')
            self.creat_storage()
            print(storage)
        elif action == 'U':
            print('Update action selected')
        elif action == "D":
            print('Delete action selected')
        else:
            print('Uoer answer is dont usalble')

    def creat_storage(self):

        key = input('Please name of site: ')
        password = input('Please password of site: ')
        storage[key]= password

    def del_storage(self):

        delkey = input('Enter site: ')
        delpassword = input('Enter password: ')
        storage.pop[delkey]= delpassword






