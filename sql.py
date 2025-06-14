import sqlite3
connection = sqlite3.connect('data.db')  # Creates file if not exists

cursor = connection.cursor()

table = '''
CREATE TABLE Students(name VARCHAR (30),class VARCHAR(10),marks INT , company VARCHAR(30))
'''

cursor.execute(table)

cursor.execute('''INSERT INTO STUDENTS VALUES ('Ramesh', 'BCom', 89, 'Google')''')
cursor.execute('''INSERT INTO STUDENTS VALUES ('Suresh', 'MCom', 78, 'TCS')''')
cursor.execute('''INSERT INTO STUDENTS VALUES ('Mahesh', 'BCom', 85, 'Infosys')''')
cursor.execute('''INSERT INTO STUDENTS VALUES ('Ganesh', 'MCom', 91, 'Microsoft')''')
cursor.execute('''INSERT INTO STUDENTS VALUES ('Dinesh', 'BCom', 67, 'Amazon')''')

print("the inserted records-")
df = cursor.execute('''select * from students''')

for row in df:
    print(row)

connection.commit()
connection.close()