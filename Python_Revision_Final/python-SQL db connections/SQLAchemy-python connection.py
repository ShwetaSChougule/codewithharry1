#Connecting to SQL using SQLAlchemy to python
# it needs to use sql library
# pip install SQLAlchemy
# dialect - Actually Sqlalchemy makes it possible for your code to communicate with multiple databases (like Postgres,Mysql,MS,Oracal etc.).
# Dialect is like a personal secretary to Sqlalchemy that makes Sqlalchemy aware of specific database it has to communicate with.

from sqlalchemy import create_engine

user = 'root'
password = 'password'
host = '127.0.0.1'
port = 3306
database = 'Geeks'

def get_connection():
    def get_connection():
        return create_engine(
            url="postgresql://{0}:{1}@{2}:{3}/{4}".format(
                user, password, host, port, database
            )
        )
if __name__ == '__main__':
    try:
        engine = get_connection()
        print("Connection successful")
    except:
        print("error")