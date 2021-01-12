import json

from constants import PATH_TO_STORAGE


class Storage:
    def read_storage(self):
        with open(PATH_TO_STORAGE) as f:
            data = json.load(f)
            return data


test = Storage()
test.read_storage()

