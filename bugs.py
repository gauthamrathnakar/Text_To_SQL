import sqlite3

#Connect to sqlite
connection = sqlite3.connect('bugs.db')

#Create a cursor object to insert record, create table, retrieve
cursor = connection.cursor()

#Create table
table_info = """
Create table BUGS (TITLE VARCHAR(250), REPORTER VARCHAR(25), CURSTATE VARCHAR(25), PROJECT VARCHAR(25), TOOLVER VARCHAR(25),
                   PRIORITY VARCHAR(10), ASSIGNEE VARCHAR(25));
"""

cursor.execute(table_info)

#Insert some more records
cursor.execute('''Insert Into BUGS values('DyingLight failed', 'Moily,Gautham', 'OPENED', 'RRA', '1.9', 'P1', 'Hosier,Antony')''');
cursor.execute('''Insert Into BUGS values('Unable to open RRA', 'Moily,Gautham', 'OPENED', 'RRA', '1.8', 'P3', 'Bettel, Jacob')''');
cursor.execute('''Insert Into BUGS values('Backend tests failed', 'Moily,Gautham', 'IMPLEMENTED', 'RRA', '1.9', 'P1', 'Moily,Gautham')''');
cursor.execute('''Insert Into BUGS values('Incorrect copyright year', 'Moily,Gautham', 'CLOSED', 'RRA', '1.7', 'P1', 'Moily,Gautham')''');
cursor.execute('''Insert Into BUGS values('Unable to load SpiderMan sample', 'Adhaduk,Chand', 'OPENED', 'RRA', '1.9', 'P1', 'Hosier,Antony')''');

#Display all the records
print("The inserted records are")

data = cursor.execute('''Select * from BUGS''')

for row in data:
    print(row)

#Close the connection
connection.commit()
connection.close()