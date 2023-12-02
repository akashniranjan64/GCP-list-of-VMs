import db_con
import re
import subprocess
import datetime
import log_impl
logger = log_impl._init_logger()

#project_pattern = r"[,'()\\]"
#return re.sub(project_pattern, "", str(results))

def get_project_list(project_name):
    with open('project-list-db.txt', 'a') as file:
        file.write(project_name + '\n')

def get_vm_list(task):
    with open('project-list-db.txt', 'r') as file:
        contents = file.readlines()

    for line in contents:
        project_name = line.strip('\n')
        connection = db_con.get_db_connection()
        cursor = connection.cursor()
        if task == "start":
            cursor.execute("SELECT vm_sch_start,vm_name FROM VMs_list where project_name = %s", (project_name,))
            datetime_value = cursor.fetchall()

            for item in datetime_value:
                row_text = item[0]
                db_time = datetime.datetime.strptime(str(row_text), '%Y-%m-%d %H:%M:%S')
                if (db_time.time().hour >= datetime.datetime.now().time().hour-1 and db_time.time().hour <= datetime.datetime.now().time().hour):
                    vm_scheduling_job(project_name, item[1], task)
                    vm_update_state(project_name, item[1], True)
                cursor.close()
                connection.close()
        else:
            cursor.execute("SELECT vm_sch_stop,vm_name FROM VMs_list where project_name = %s", (project_name,))
            datetime_value = cursor.fetchall()

            for item in datetime_value:
                row_text = item[0]
                db_time = datetime.datetime.strptime(str(row_text), '%Y-%m-%d %H:%M:%S')
                if (db_time.time().hour >= datetime.datetime.now().time().hour-1 and db_time.time().hour <= datetime.datetime.now().time().hour):
                    vm_scheduling_job(project_name, item[1], task)
                    vm_update_state(project_name, item[1], False)
            cursor.close()
            connection.close()

def vm_update_state(project_name, vm_name, vm_state):
    try:
        connection = db_con.get_db_connection()
        cursor = connection.cursor()
        cursor.execute("UPDATE VMs_list SET vm_status = %s where project_name = %s and vm_name = %s", (vm_state, project_name, vm_name))
        connection.commit()
        cursor.close()
    finally:
        connection.close()


def vm_scheduling_job(project_name, vm_list, task):
    vm_list = re.sub(r"[,'()\\]", "", str(vm_list))
    vm_list = vm_list.strip("[]")
    vm_list = vm_list.replace(' ', '|')
    subprocess.call(['/Users/akasnir/Documents/loblaw/Stories/GCP-list-of-VMs/compute-scheduler/scheduler_impl.sh', vm_list, project_name, task])