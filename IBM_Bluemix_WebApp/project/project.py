# Copyright 2015 IBM Corp. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from flask import Flask, jsonify
from datetime import datetime
from time import gmtime, strftime
from os.path import getmtime
from base64 import b64encode
from flask import Flask, render_template, request, make_response
from cloudant.client import Cloudant
import hashlib

app = Flask(__name__)
BLOCKSIZE = 65536
hasher = hashlib.md5()

client = Cloudant(USERNAME, PASSWORD,  url='https://acct.cloudant.com')

client.connect()

session = client.session()
print 'Username: {0}'.format(session['userCtx']['name'])
print 'Databases: {0}'.format(client.all_dbs())
my_database = client['storage_service']


# You can check that the database exists
if my_database.exists():
    print 'Database SUCCESS!!'


@app.route('/')
def Welcome():
	return render_template('index.html')

@app.route('/upload/')
def upload():
	return render_template('upload.html')
	
@app.route('/uploadComplete',methods=['POST'])
def uploadComplete():
	f = request.files['fileField']
	file_name = f.filename
	hasher = hashlib.md5()
	buf = f.read()
	while len(buf) > 0:
		hasher.update(buf)
		buf = f.read()
	hashed_value=hasher.hexdigest()
	version_number=1
	for document in my_database:
		if document.exists() and document['file_name'] == file_name:
			if document['hashed_value']==hashed_value:
				return "File already exists!!"
			else:
				version_number=int(document['version_number'])+1
	last_modified=strftime("%Y-%m-%d %H:%M:%S", gmtime()) 
	uploaded_file_content = b64encode(f.read())
	data = {'hashed_value': hashed_value,'file_name': file_name,'version_number': version_number,'last_modified': last_modified, '_attachments': {file_name : {'data': uploaded_file_content}}}
	doc = my_database.create_document(data)
	message='File %s is uploaded successfully.' %(doc['file_name'])
	return render_template('index.html',message=message)
	
	
@app.route('/download/')
def download():
	return render_template('download.html')
	
@app.route('/downloadComplete',methods=['POST'])
def downloadComplete():
	file_name=request.form['filename']
	file_version=request.form['version']
	for document in my_database:
		if document['file_name'] == file_name and document['version_number']==int(file_version):
			file = document.get_attachment(file_name, attachment_type='binary')
			response = make_response(file)
			response.headers["Content-Disposition"] = "attachment; filename=%s"%file_name
			return response
		else:
			message='File %s not found.' %(document['file_name'])
	return render_template('index.html',message=message)
	
@app.route('/delete/')
def delete():
	return render_template('delete.html')
	
@app.route('/deleteComplete',methods=['POST'])
def deleteComplete():
	file_name=request.form['filename']
	file_version=request.form['version']
	for document in my_database:
		if document['file_name'] == file_name and document['version_number']==int(file_version):
			print("File found and deleted")
			message='File %s is deleted successfully.' %(document['file_name'])
			document.delete()
			return render_template('index.html',message=message)
		else:
			message='File %s not found.' %(document['file_name'])
	return render_template('index.html',message=message)
	
@app.route('/list/')
def list():
	list=""
	for document in my_database:
		version=str(document['version_number'])
		list+='<tr><td>%s</td><td>%s</td><td>%s</td></tr>' % (document['file_name'], version, document['last_modified'])
	return render_template('list.html',list=list)	

port = os.getenv('PORT', '5000')
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=int(port),debug=True)
client.disconnect()