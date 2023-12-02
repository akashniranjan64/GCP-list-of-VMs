import datetime
import db_con
import get_list

import log_impl
logger = log_impl._init_logger()

#current_time = datetime.datetime.now().time()
#print(current_time.hour,":",current_time.minute)

def get_unique_projects(rows):
    unique_list = list(set(rows))
    for project_name in unique_list:
        logger.info(project_name)
        #get_list.get_project_list(project_name)


def get_active_schedules(task):
    my_list = []
    open('project-list-db.txt', 'w')
    connection = db_con.get_db_connection()
    cursor = connection.cursor()
    if task == "start":
        logger.info("fetching active start schedules for the time")
        cursor.execute("SELECT vm_sch_start ,project_name FROM VMs_list")
    else:
        logger.info("fetching active stop schedules from the DB")
        cursor.execute("SELECT vm_sch_stop ,project_name FROM VMs_list")
    datetime_value = cursor.fetchall()
    for item in datetime_value:
        row_text = item[0]
        db_time = datetime.datetime.strptime(str(row_text), '%Y-%m-%d %H:%M:%S')
        if (db_time.time().hour >= datetime.datetime.now().time().hour-1 and db_time.time().hour <= datetime.datetime.now().time().hour):
            my_list.append(item[1])
    get_unique_projects(my_list)
    #cursor.close()
    #connection.close()
