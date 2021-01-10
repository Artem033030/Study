import json

# from password_app.constants import PATH_TO_STORAGE


class Storage:
    def read_storage(self):
        with open('/Users/artempilipchuk/pass_storage.json') as f:
            data = json.load(f)
            print(data)


test = Storage()
test.read_storage()

