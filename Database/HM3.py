import sqlalchemy as db


class User:
    def __init__(self):
        self.engine = db.create_engine('sqlite:///User.db')
        self.connection = self.engine.connect()
        self.metadata = db.MetaData()
        self.users = db.Table('Users', self.metadata,
                              db.Column('ID', db.Integer, primary_key=True),
                              db.Column('Name', db.Text),
                              db.Column('Email', db.Text, unique=True),
                              db.Column('Password', db.Text))
        self.metadata.create_all(self.engine)

    def insert_user(self, name, email, password):
        insert_query = self.users.insert().values({'Name': name, 'Email': email, 'Password': password})
        self.connection.execute(insert_query)
        self.connection.commit()

    def select_user(self, email, password):
        select_query = (db.select(self.users).where(
            self.users.columns.Email == email,
            self.users.columns.Password == password))
        result = self.connection.execute(select_query)
        for row in result.fetchall():
            print(f'User {row.Name} is authorized')

    def delete_user(self, email, password=None):
        if email == 'all':
            delete_query = db.delete(self.users)
        else:
            delete_query = db.delete(self.users).where(
                self.users.columns.Email == email,
                self.users.columns.Password == password)
        self.connection.execute(delete_query)
        self.connection.commit()

    def update_user(self, email, password, name=None, new_password=None):
        if name:
            update_query = (db.update(self.users)
                            .where(self.users.columns.Email == email,
                                   self.users.columns.Password == password)
                            .values(Name=name))
            self.connection.execute(update_query)
        if new_password:
            update_query = (db.update(self.users)
                            .where(self.users.columns.Email == email,
                                   self.users.columns.Password == password)
                            .values(Password=new_password))
            self.connection.execute(update_query)
        self.connection.commit()


users = User()

users.insert_user('John', 'dd@gmail.com', '123456qq')
users.insert_user('JohnCopy', 'dd@gmail.com', '95164')
users.insert_user('JoeStar', 'bbb@gmail.com', 'gdfdfsg')

users.select_user('dd@gmail.com', 95164)

users.delete_user('dd@gmail.com', 95164)

# users.delete_user('all')

users.update_user('dd@gmail.com', '123456qq', 'JoeJoe', '+4659-6542')
