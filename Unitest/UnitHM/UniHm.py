# Напишіть клас, який представляє просту систему керування обліковими записами
# з методами додавання та видалення облікових записів.

# Створіть тести для перевірки коректності додавання та видалення облікових записів,
# а також для обробки ситуації, коли намагаємося додати вже існуючий обліковий запис або видалити неіснуючий.
class Node:
    def __init__(self, data, right_step=None):
        self.data = data
        self.right = right_step


class Google:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, username):
        node = Node(username)
        if self.tail is None:
            self.head = node
            self.tail = node
            return
        elif self.tail:
            if username != self.tail.data:
                # node.right = self.tail
                self.tail.right = node
                self.tail = node
                return
            else:
                raise ValueError(f'{username} is already exist')

    def remover(self, username):
        if not self.head:
            raise ValueError("Profile list is empty")
        current = self.head
        end = self.tail
        while current:
            self.tail = current
            if self.head.data == username:
                self.head = current.right
            if current == end:
                if current.data != username:
                    raise ValueError(f"{username} is not exist")
                break
            if current.right == end:
                if current.right.data == username:
                    end = current
                    current.right = None

            if current.right.data == username:
                self.tail.right = current.right.right
            current = current.right
        self.tail = end

    def print_mail_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.right


if __name__ == '__main__':
    google = Google()
    while True:
        print(f'\nProfile list: :')
        google.print_mail_list()
        choice = input('''
        exit - close program
        add - add new profile
        rem - remove profile
        ''')
        match choice.lower():
            case 'exit':
                break
            case 'add':
                google.insert(input('Enter a new profile: '))
            case 'rem':
                google.remover(input('Enter the profile to remove: '))
