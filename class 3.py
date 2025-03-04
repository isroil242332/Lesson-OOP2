class User:
    def __init__(self,user_id, name):
        self._user_id = user_id
        self._name = name
        self._level = 'user'

    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_level(self):
        return self._level

    def set_name(self, name):
        self._name = name

class Admin(User):
    def init(self, user_id, name):
        super().__init__(user_id, name)
        self.level = 'admin'

    def add_user(self, user_list, user):
        user_list.append(user)
        print(f'Ползователь успешно добавлен в список')

    def remove_user(self, user_list, user):
        user_list.remove(user)

users = []
admin = Admin('a', 'Sodiq')
user1 = User('u1', 'Muhammad')
user2 = User('u2', 'Isroil')

print(user2.get_name())
admin.add_user(users, user1)