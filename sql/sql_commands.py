import hashlib, os, uuid, pdb

# Users

# Generate sportslover's password hash

algorithm = 'sha512'
paul_password = 'paulpass93'
paul_salt = uuid.uuid4().hex

m = hashlib.new(algorithm)
m.update(paul_salt + paul_password)
paul_password_hash = m.hexdigest()
paul_password_db = "$".join([algorithm, paul_salt, paul_password_hash])

print 'INSERT INTO User VALUES ("sportslover", "Paul", "Walker", "' + \
								paul_password_db + '", "sportslover@hotmail.com");'

# Generate traveler's password hash

rebecca_password = "rebeccapass15"
rebecca_salt = uuid.uuid4().hex
m = hashlib.new(algorithm)
m.update(rebecca_salt + rebecca_password)
rebecca_password_hash = m.hexdigest()
rebecca_password_db = "$".join([algorithm, rebecca_salt, rebecca_password_hash])

print 'INSERT INTO User VALUES ("traveler", "Rebecca", "Travolta", "' +\
								rebecca_password_db + '", "rebt@explorer.org");'

# Generate spacejunkie's password hash
bob_password = "bob1pass"
bob_salt = uuid.uuid4().hex
m = hashlib.new(algorithm)
m.update(bob_salt + bob_password)
bob_password_hash = m.hexdigest()
bob_password_db = "$".join([algorithm, bob_salt, bob_password_hash])

print 'INSERT INTO User VALUES ("spacejunkie", "Bob", "Spacey", "' +\
								bob_password_db + '", "bspace@spacejunkies.net");'

# Paul Walker's (sportslover's) albums

print 'INSERT INTO Album (title, created, lastupdated, username, access) VALUES ("I lov\
e sports", CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, "sportslover", "public");'

print 'INSERT INTO Album (title, created, lastupdated, username, access) VALUES ("I lov\
e football", CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, "sportslover", "private");'

# Rebecca Travolta's (traveler's) album

print 'INSERT INTO Album (title, created, lastupdated, username, access) VALUES ("Aroun\
d The World", CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, "traveler", "public");'

# Bob Spacey's (spacejunkie's) album

print 'INSERT INTO Album (title, created, lastupdated, username, access) VALUES ("Cool \
Space Shots", CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, "spacejunkie", "private");'

# Photos and Contain
picid = ''
albumid = ''
path = '../static/images'
for filename in os.listdir(path):
	fileNameWithoutExtension = ''
	splitFileName = filename
	fileNameWithoutExtension, fileExtension = os.path.splitext(splitFileName)
	fileName = os.path.join(path, filename)
	if filename.startswith('sports'):
		albumid = '1'
		picid = hashlib.md5(str(1) + filename).hexdigest()
		os.rename(fileName, fileName.replace(fileNameWithoutExtension, picid) )
	elif filename.startswith('football'):
		albumid = '2'
		picid = hashlib.md5(str(2) + filename).hexdigest()
		os.rename(fileName, fileName.replace(fileNameWithoutExtension, picid) )
	elif filename.startswith('world'):
		albumid = '3'
		picid = hashlib.md5(str(3) + filename).hexdigest()
		os.rename(fileName, fileName.replace(fileNameWithoutExtension, picid) )
	elif filename.startswith('space'):
		albumid = '4'
		picid = hashlib.md5(str(4) + filename).hexdigest()
		os.rename(fileName, fileName.replace(fileNameWithoutExtension, picid) )
	if picid == '':
		continue
	print 'INSERT INTO Photo VALUES ("' + picid + '", "' + fileExtension[1:] + '", \
CURRENT_TIMESTAMP);'
	print 'INSERT INTO Contain (albumid, picid, caption) VALUES (' + albumid +', \'' + picid + '\', "");'

# Populate AlbumAccess table with proper tuples (only "I love sports" and 
# "Around the World" are public, and no tuples for owner of album)

print 'INSERT INTO AlbumAccess VALUES (1, "traveler");'
print 'INSERT INTO AlbumAccess VALUES (1, "spacejunkie");'
print 'INSERT INTO AlbumAccess VALUES (3, "sportslover");'
print 'INSERT INTO AlbumAccess VALUES (3, "spacejunkie");'
