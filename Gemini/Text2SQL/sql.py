import sqlite3

#connect to sqllite
connect_to_db = sqlite3.connect('Student.db')
#cursor to execute sql commands
cursor = connect_to_db.cursor()

create = """CREATE TABLE IF NOT EXISTS Student (name varchar(35), 
age INTEGER, class varchar(20), section varchar(20), percentage INTEGER);"""

cursor.execute(create)

#insert values
cursor.execute('''Insert into Student values('Om',19,'10','B',85)''')
cursor.execute('''Insert into Student values('Krishna',19,'10','B',90)''')
cursor.execute('''Insert into Student values('Sneh',20,'11','B',75)''')
cursor.execute('''Insert into Student values('Noman',19,'10','A',95)''')
cursor.execute('''Insert into Student values('Meet',20,'11','A',80)''')
cursor.execute('''Insert into Student values('Isha',19,'10','B',85)''')
cursor.execute('''Insert into Student values('Abhay',20,'11','B',90)''')
cursor.execute('''Insert into Student values('Om',19,'10','A',75)''')
cursor.execute('''Insert into Student values('Krishna',20,'11','A',85)''')
cursor.execute('''Insert into Student values('Aastha',19,'10','B',80)''')
cursor.execute('''Insert into Student values('Neel',21,'12','B',95)''')
cursor.execute('''Insert into Student values('Archie',20,'12','A',60)''')
cursor.execute('''Insert into Student values('Kush',21,'12','A',75)''')
cursor.execute('''Insert into Student values('Pratik',20,'12','A',85)''')
cursor.execute('''Insert into Student values('Dev',21,'12','B',80)''')
cursor.execute('''Insert into Student values('Shreya',20,'12','B',55)''')

#Display all the records
print("The Inserted Records are: ")

data = cursor.execute('''Select * FROM Student''')
for row in data:
    print(row)
       
#Close the connection
connect_to_db.commit()
connect_to_db.close()
