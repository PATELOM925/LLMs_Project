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
cursor.execute('''Insert into Student values('Raj',20,'11','B',75)''')
cursor.execute('''Insert into Student values('Riya',19,'10','A',95)''')
cursor.execute('''Insert into Student values('Rohit',20,'11','A',80)''')
cursor.execute('''Insert into Student values('Rakesh',19,'10','B',85)''')
cursor.execute('''Insert into Student values('Rajesh',20,'11','B',90)''')
cursor.execute('''Insert into Student values('Raza',19,'10','A',75)''')
cursor.execute('''Insert into Student values('Rahim',20,'11','A',85)''')
cursor.execute('''Insert into Student values('Rajat',19,'10','B',80)''')
cursor.execute('''Insert into Student values('Kriti',21,'12','B',95)''')
cursor.execute('''Insert into Student values('Karan',20,'12','A',60)''')
cursor.execute('''Insert into Student values('Kunal',21,'12','A',75)''')
cursor.execute('''Insert into Student values('Kiran',20,'12','A',85)''')
cursor.execute('''Insert into Student values('Komal',21,'12','B',80)''')
cursor.execute('''Insert into Student values('Kamal',20,'12','B',55)''')

#Display all the records
print("The Inserted Records are: ")

data = cursor.execute('''Select * FROM Student''')
for row in data:
    print(row)
       
#Close the connection
connect_to_db.commit()
connect_to_db.close()