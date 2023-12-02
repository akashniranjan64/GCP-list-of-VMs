import subprocess
import mysql.connector
import schedule
import time
import re
from mysql.connector import Error
from os.path import exists
import os
import csv
project_pattern = r"[,'()\\]"

filename_start = "/home/lcluser01/flat_file/start_feed.csv"
filename_stop = "/home/lcluser01/flat_file/stop_feed.csv"

start_file_dir = os.path.isfile(filename_start)
stop_file_dir = os.path.isfile(filename_stop)

def create_db_connection(host='10.196.40.48', user='root', password='root', db_name='vm_scheduler'):
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

def fetch_value_from_db_start():
    fetch_values = "SELECT vm_sch_start, project_name, vm_name, vm_zone FROM VMs_list WHERE start_days LIKE CONCAT('%', (SELECT DAYOFWEEK(CURDATE())), '%');"
    conn = create_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(fetch_values)
        values = cursor.fetchall()
        generate_file_start(values)
    except Error as err:
        print(f"Error: '{err}'")
        exit(1)

def generate_file_start(list_values):
    with open(filename_start, "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Start_time","Project_id", "Instance_name", "Zone" ])
        for item in list_values:
            writer.writerow(item)
    #copy_file()

def fetch_value_from_db_stop():
    fetch_values = "SELECT vm_sch_stop, project_name, vm_name, vm_zone FROM VMs_list WHERE stop_days LIKE CONCAT('%', (SELECT DAYOFWEEK(CURDATE())), '%');"
    conn = create_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(fetch_values)
        values = cursor.fetchall()
        generate_file_stop(values)
    except Error as err:
        print(f"Error: '{err}'")
        exit(1)

def generate_file_stop(list_values):
    with open(filename_stop, "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Stop_time","Project_id", "Instance_name", "Zone"])
        for item in list_values:
            writer.writerow(item)
    copy_file()


def copy_file():
    subprocess.call(['/home/lcluser01/flat_file/copy_file.sh'])


fetch_value_from_db_start()
fetch_value_from_db_stop()
