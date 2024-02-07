class User:
    def __init__(self, name, is_admin=False):
        self.name = name
        self.is_admin = is_admin


class SecureSystem:
    def amin_func(self):
        print(f'Admin function')

    def regular_func(self):
        print(f'Regular function')


class AccessControlProxy:
    def __init__(self, user):
        self.user = user
        self.secure_system = SecureSystem()

    def amin_func(self):
        if self.user.is_admin:
            self.secure_system.amin_func()
        else:
            print(f'{self.user.name} is not admin')

    def regular_func(self):
        self.secure_system.regular_func()


def t_access_user(user):
    proxy = AccessControlProxy(user)
    print(f'testing user {user.name}')
    proxy.amin_func()
    proxy.regular_func()


user1 = User('John', True)
user2 = User('Bob', False)

t_access_user(user1)
t_access_user(user2)
