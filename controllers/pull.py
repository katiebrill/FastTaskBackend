from flask import *
from extensions import db
import config
import pdb
import json

main = Blueprint('pull', __name__)

@main.route('/pull', methods=['POST'])
def pull_tasks():

    classes = request.get_json(force=True)
    for_return = {}
    cur = db.cursor()    
    
    for cls in classes:
        class_id = str(cls['class_id'])
        cur.execute('SELECT * FROM Album WHERE classid=\"' + class_id + '\"')
        tasks = cur.fetchall()
        for_return[class_id] = tasks
        
	return jsonify(tasks)
    