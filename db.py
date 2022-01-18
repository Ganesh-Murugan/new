import mysql.connector


mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="root",
  database="cruds"
)


def create(table_name):
    mycursor = mydb.cursor()
    mycursor.execute(f"CREATE TABLE if NOT EXISTS {table_name}(code_type varchar(10), code varchar(5) PRIMARY KEY, code_description varchar(20) NOT NULL);")
    mydb.commit()

    
#create("country")

def view(table_name):
    mycursor = mydb.cursor(buffered=True)
    mycursor.execute(f"SELECT * FROM {table_name}")
    mydb.commit()
    for x in mycursor:
        print(x)

#view("country")

def add(table_name, code, code_des):
    mycursor = mydb.cursor()
    mycursor.execute(f"insert into {table_name}(code_type, code, code_description) values(%s, %s,%s);",(table_name, code, code_des))
    mydb.commit()
    
#add("country","JP","Japan")

def update(table_name, code_des, code):
    mycursor = mydb.cursor()
    mycursor.execute(f"update {table_name} set code_description = %s where code = %s",(code_des, code))
    mydb.commit()
    

#update("country", "Chinas", "CN")

def delete(table_name, code):
    mycursor = mydb.cursor()
    mycursor.execute(f"delete from {table_name} where code = %s",(code,))
    mydb.commit()

#delete("country", "CN")