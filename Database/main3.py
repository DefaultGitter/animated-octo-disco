import sqlalchemy as db

engine = db.create_engine('sqlite:///Univer1.db')
connection = engine.connect()
metadata = db.MetaData()

students = db.Table('Students', metadata,
                    db.Column('ID', db.Integer, primary_key=True),
                    db.Column('FirstName', db.Text),
                    db.Column('LastName', db.Text),
                    db.Column('Age', db.Integer))

metadata.create_all(engine)

student_list = [{'FirstName': 'John', 'LastName': 'Doe', 'Age': 23},
                {'FirstName': 'Job', 'LastName': 'Work', 'Age': 13},
                {'FirstName': 'Nod', 'LastName': 'Dod', 'Age': 33}]

# insert
# insert_query = students.insert().values({'FirstName': 'John', 'LastName': 'Doe', 'Age': 23})
# insert_query = students.insert().values(student_list)
# connection.execute(insert_query)
# connection.commit()

# update
# update_query = db.update(students).where(students.columns.FirstName == 'Job').values(Age=666)
# connection.execute(update_query)
# connection.commit()

# delete
# delete_query = db.delete(students).where(students.columns.FirstName == 'Nod')
# connection.execute(delete_query)
# connection.commit()

# select
# select_query = db.select(students)
select_query = db.select(students).where(students.columns.FirstName == 'John')
result = connection.execute(select_query)

for row in result.fetchall():
    print(row)
