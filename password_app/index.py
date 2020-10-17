print('Hello world')
storage = {}


def logic():

    action = input('What do you want to do (C,R,U,D): ').capitalize()
    if action == 'C':
        print('Create action selected')

    elif action == 'R':
        print('Read action selected')
    elif action == 'U':
        print('Update action selected')
    elif action == "D":
        print('Delete action selected')
    else:
        print('Uoer answer is dont usalble')


def creat_storage():

    key = input('Please name of site: ')
    password = input('Please password of site: ')
    storage = dict(key=password)
    print(storage)






creat_storage()



