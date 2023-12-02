#!/bin/bash

#nohup pip install -r py_requriments.txt
#nohup python3 -c 'from db_scripts.db_script import create_db; create_db("127.0.0.1", "root", "password")'
#nohup python3 -c 'scheduler_impl.py'
#&& nohup python3 scheduler_impl.py

nohup pip3.9 install -r /home/lcluser01/scheduler/destination_dir/py_requriments.txt && nohup python3.9 -c 'from db_scripts.db_script import create_db; create_db("10.196.40.48", "root", "root")' &

