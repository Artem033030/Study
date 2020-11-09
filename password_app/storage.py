import json


# from password_app.constants import PATH_TO_STORAGE


class Storage:
    def read_storage(self):
        with open('/Users/artempilipchuk/pass_storage.json', 'r') as f:
            data = json.load(f.read())
            print(data)


test = Storage()
test.read_storage()
