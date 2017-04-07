from flask import *
from extensions import db
import config
import pdb

main = Blueprint('main', __name__, template_folder='templates')

@main.route('/pull')
def main_route():
	cur = db.cursor()
	cur.execute('SELECT username FROM User')
	usrs = cur.fetchall() 
	# Get all the public albums
	cur.execute('SELECT albumid, title, username FROM Album WHERE access="public"')
	publicAlbumIds = cur.fetchall()
	# Get first and last name of user if in session
	first, last = ('', '')
	if session:
		cur.execute('SELECT albumid, title, username FROM Album WHERE access="private" AND username=\'' + session['username'] + '\'')
		publicAlbumIds += cur.fetchall()
		cur.execute('SELECT albumid FROM AlbumAccess WHERE username=\'' + session['username'] + '\'')
		privateIDs = cur.fetchall()
		for x in privateIDs:
			cur.execute('SELECT albumid, title, username FROM Album WHERE albumid=\'' + str(x['albumid']) + '\'')
			publicAlbumIds += cur.fetchall()

		cur.execute('SELECT firstname, lastname FROM User WHERE username=\"' +session['username'] + '\"')
		results = cur.fetchall()
		first, last = results[0]['firstname'], results[0]['lastname']
	return render_template("index.html", usernames=usrs, pubalbums=publicAlbumIds,
										 firstname=first, lastname=last)