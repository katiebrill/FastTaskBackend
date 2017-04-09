from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy

import extensions
import controllers
import config
#import os

# Initialize Flask app with the template folder address
app = Flask(__name__, template_folder='templates')


app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']

# Url prefix is Heroku Secret Key
app.register_blueprint(controllers.push, url_prefix='')
app.register_blueprint(controllers.pull, url_prefix='')

#set secret key
app.secret_key = '\x11\x9c\n;[\xa0V\xc3O\xb9\xa1\x0e]fR+\x02\x02\xa8\xacL\x8bq\xcb'

db = SQLAlchemy(app)

#Listen on external IPs
# For us, listen to port 3000 so you can just run 'python app.py' to start the server
if __name__ == '__main__':
	 # listen on external IPs
    app.run(host=config.env['host'], port=config.env['port'], debug=True)
