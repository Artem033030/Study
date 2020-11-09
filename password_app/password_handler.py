storage = {'test': 'abc'}


class PasswordHandler:

    def create_line(self, key, password):
        storage[key] = password
        return f'{key}:{password} was added to the storage'

    def del_line(self, del_key, del_password):
        storage.pop(del_key, None)
        return f'{del_key}:{del_password} was removed from'

    def read_line(self, ent_key):
        return storage[ent_key]

    def change_line(self, change_key, new_password):
        storage[change_key] = new_password
        return f'{change_key} was change from storage'
