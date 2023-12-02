from mysql.connector import Error
import logging
from db_con_impl import create_server_connection, create_db_connection

################################### version 1 ###################################
create_table_vmlist = """
CREATE TABLE VMs_list (
  id int NOT NULL AUTO_INCREMENT,
  project_name varchar(45) NOT NULL,
  vm_name varchar(45) NOT NULL,
  vm_sch_start time DEFAULT NULL,
  vm_sch_stop time DEFAULT NULL,
  vm_zone varchar(45) NOT NULL,
  PRIMARY KEY (id)
)

CREATE TABLE VMs_list_TEMP (
  id_new int NOT NULL AUTO_INCREMENT,
  project_name varchar(45) NOT NULL,
  vm_name varchar(45) NOT NULL,
  vm_sch_start time DEFAULT NULL,
  vm_sch_stop time DEFAULT NULL,
  vm_zone varchar(45) NOT NULL,
  start_days varchar(255) NOT NULL,
  stop_days varchar(255) NOT NULL,
  PRIMARY KEY (id_new)
)

CREATE TABLE `VMs_list` (
  `id` int NOT NULL AUTO_INCREMENT,
  `project_name` varchar(45) NOT NULL,
  `vm_name` varchar(45) NOT NULL,
  `vm_sch_start` time DEFAULT NULL,
  `vm_sch_stop` time DEFAULT NULL,
  `vm_zone` varchar(45) NOT NULL,
  `stop_days` varchar(255) DEFAULT NULL,
  `start_days` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)



  tue varchar(45) NOT NULL,
  wed varchar(45) NOT NULL,
  thu varchar(45) NOT NULL,
  fri varchar(45) NOT NULL,
  sat varchar(45) NOT NULL,
  sun varchar(45) NOT NULL
id_sch 
mon
tue
wed
thu
fri
sat
sun
vm_name (FK)
"""

#create_table_test = """
#CREATE TABLE VMs_test (
#  id int NOT NULL AUTO_INCREMENT,
#  project_name varchar(45) NOT NULL,
#  vm_name varchar(45) NOT NULL,
#  vm_sch_start datetime DEFAULT NULL,
#  vm_sch_stop datetime DEFAULT NULL,
#  vm_status tinyint DEFAULT NULL,
#  PRIMARY KEY (id)
#)
#"""

################################### version 1 ###################################

def create_db(host, user, password):
    create_schema = 'CREATE DATABASE IF NOT EXISTS vm_scheduler'
    connection = create_server_connection(host, user, password)
    cursor = connection.cursor()
    try:
        cursor.execute(create_schema)
        connection.commit()
        logging.info("DB created")
        table_list()
    except Error as err:
        print(f"Error: '{err}'")
        exit(1)



#############################################################################
#                                                                           #
#                                                                           #
# It will keep iterating between tables.                                    #
# Do not keep old version here to avoid error : table already exist         #
#                                                                           #
#                                                                           #
#############################################################################

def table_list():
    my_list = [] # Add new tables
    table_iterator(my_list)


def table_iterator(query_list):
    for item in query_list:
        create_table(item)


def create_table(create_table_vmlist):
    connection = create_db_connection('127.0.0.1','root','password', 'vm_scheduler_new')
    cursor = connection.cursor()
    try:
        cursor.execute(create_table_vmlist)
        connection.commit()
        logging.info('table created', create_table_vmlist)
    except Error as err:
        print(f"Error: '{err}'")
        exit(1)