from base64 import b64encode
import json
import os
import json
import boto3
from flask import Flask, render_template, request,make_response,session
app = Flask(__name__)
s3 = boto3.resource('s3',aws_access_key_id = 'AKIAI3KOSZRHWY6AAHUQ',
        aws_secret_access_key = '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',config= boto3.session.Config(signature_version='s3v4'))
app.secret_key='any string'
@app.route('/')
def hello_world():
  return render_template('index.html')

@app.route('/logout/')
def logout():
  session.clear()
  return render_template('index.html')

@app.route('/login/',methods=['POST'])
def login():
   username=request.form['username']
   session['bucket_name']=username
   result = s3.meta.client.get_object(Bucket='priyankaj', Key='Users.txt')
   content= result['Body'].read()
   user=username+" "
   if user in content:
   	return render_template('welcome.html')
   else:
	return render_template('index.html',message="User does not exist!!")
	
@app.route('/download/')
def download():
   return render_template('download.html')

@app.route('/downloadComplete',methods=['POST'])
def downloadComplete():
	filename=request.form['filename']
	try:
		f=s3.meta.client.get_object(Bucket=session['bucket_name'],Key=filename)
		contents=f['Body'].read()
		response = make_response(contents)
		response.headers["Content-Disposition"] = "attachment; filename=%s"%filename
		return response
	except:
		return render_template('welcome.html',message="File %s not on cloud"%(filename))
		
@app.route('/upload/')
def upload():
	return render_template('upload.html')
	
@app.route('/uploadComplete',methods=['POST'])
def uploadComplete():
        f=request.files['fileField']
        filename=f.filename
	data = f.read()
	response=s3.meta.client.put_object(ContentType=f.content_type,Bucket=session['bucket_name'],Key=filename,Body=data)
        message="File %s uploaded successfully"%(filename)
        return render_template('welcome.html',message=message)

@app.route('/deleteComplete',methods=['POST'])
def deleteComplete():
        filename=request.form['filename']
	try:	
        	response=client.delete_object(Bucket=session['bucket_name'],Key=filename)
        	message="File %s deleted successfully"%(filename)
        	return render_template('welcome.html',message=message)
	except:
		return render_template('welcome.html',message="File %s  not on cloud"%(filename))
		
@app.route('/delete/')
def delete():
	return render_template('delete.html')
	
@app.route('/list/')
def list():
	list=""
	bucket=s3.Bucket(session['bucket_name'])	
	for object in bucket.objects.all():
		list+='<tr><td>%s</td></tr>' % (object.key)
	return render_template('list.html',list=list)
	
if __name__ == '__main__':
  app.run()

