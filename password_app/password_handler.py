from storage import Storage


class PasswordHandler:
    def __init__(self):
        self.storage_instance = Storage()
        self.storage = self.storage_instance.read_storage()

    def create_line(self, key, password):
        self.storage[key] = password
        return f'{key}:{password} was added to the storage'

    def del_line(self, del_key, del_password):
        self.storage.pop(del_key, None)
        return f'{del_key}:{del_password} was removed from'

    def read_line(self, ent_key):
        if ent_key in self.storage:
            return self.storage[ent_key]

    def change_line(self, change_key, new_password):
        if change_key in self.storage:
            if change_key[new_password] in self.storage:
                return f'{change_key} was change from storage'
            else:
                return f"I'm sorry your password Falls"
        else:
            return f"I'm sorry your key doesn't true"
