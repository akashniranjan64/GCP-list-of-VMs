import mysql.connector
from db_scripts import db_con_impl
import log_impl

logger = log_impl._init_logger()

def get_db_connection():
    return db_con_impl.create_db_connection( '127.0.0.1', 'root', 'password','vm_scheduler')
    #return mysql.connector.connect(user='root', password='password', host='127.0.0.1',database='vm_scheduler')

"""""
cnx = db_con_impl.create_db_connection( '127.0.0.1', 'root', 'password','vm_scheduler')
cursor = cnx.cursor()
cursor.execute("show create table VMs_list")
results = cursor.fetchall()
for row in results:
    print(row)
cursor.close()
cnx.close()
"""""