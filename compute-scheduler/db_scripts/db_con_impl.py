import mysql.connector
from mysql.connector import Error

#logger = log_impl._init_logger()


def create_server_connection(host, user, password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            passwd=password
        )
    except Error as err:
        print(f"Error: '{err}'")
        exit(1)
    return connection


def create_db_connection(host, user, password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            passwd=password,
            database=db_name
        )
    except Error as err:
        print(f"Error: '{err}'")
        exit(1)
    return connection