from flask import *
from extensions import db
#from app import db

import pdb
import json

push = Blueprint('push', __name__)
#db.create_all()

@pic.route('/push', methods=['POST'])
def push_tasks():
    cur = db.cursor()
    tasks = request.get_json(force=True)
    for_return = {}
    
    for tsk in tasks:
        name = str(tsk['task_name'])
        cur.execute('SELECT * FROM Tasks WHERE task_name=\"' + name + '\"') ## AND THERE classid = classid
        if (len(cur.fetchall()) > 0 ):
            pass
            for_return[name] = 1
        else:
            taskname = str(tsk['task_name'])
            classid = str(tsk['classid'])
            due_date = str(tsk['due_date'])
            sql_command = 'INSERT INTO Tasks (task_name, classid, due_date) VALUES (\"' + task_name + '\", \"' + classid + '\", \"' + due_date + '\")'
            for_return[name] = 0
    return jsonify(for_return)
    