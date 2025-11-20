import psycopg2
def table():
    connect = psycopg2.connect(dbname="postgres", user="postgres", password="123", host="localhost", port="5433")

    cursor = connect.cursor();
    cursor.execute('''create table employee(Name TEXT, ID INT,Age INT);''')
    print("Table created successfully")

    connect.commit()
    connect.close()

def data():
    connect = psycopg2.connect(dbname="postgres", user="postgres", password="123", host="localhost", port="5433")
   
    cursor = connect.cursor();
    name= input("Enter Name: ")
    age= int(input("Enter Age: "))
    id= int(input("Enter ID: "))

    query = '''insert into employee (Name, ID, Age) values (%s, %s, %s);'''
    cursor.execute(query, (name, id, age))
    print("Data inserted successfully")
    connect.commit()
    connect.close()

data()

def extract():
    connect = psycopg2.connect(dbname="postgres", user="postgres", password="123", host="localhost", port="5433")
   
    cursor = connect.cursor();
    cursor.execute('''select * from employee;''')
    print(cursor.fetchall())
    connect.commit()
    connect.close()

extract()   
