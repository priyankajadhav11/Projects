import swiftclient
from keystoneclient import client 
from sys import version_info
import os
import re 
import gnupg

auth_url="https://identity.open.softlayer.com/v3"
projectId="9c6908d56f9b492cb05882ce4eb1762e"
region="dallas"
userId="Enter userId"
username="Enter Username"
password="Enter password"

conn = swiftclient.Connection(key=password,
authurl=auth_url,
auth_version='3',
os_options={"project_id": projectId,
"user_id": userId,
"region_name": region})
container_name = "Ncontainer"
conn.put_container(container_name)

def print_menu():       
    print "Welcome to Cloud Storage Service."
    print "1. Upload"
    print "2. Retrieve"
    print "3. Delete"
    print "4. List files"
    print "5. Exit"
  
loop=True      
 
gpg=gnupg.GPG(gnupghome='C:\Program Files (x86)\GNU\GnuPG') 
send_data = gpg.gen_key_input(key_type="RSA", key_length=1024,passphrase='send')

while loop:          
    print_menu()    
    choice = input("Enter your choice to proceed: ")
    
    if choice==1:     
		fileName=raw_input("Please enter file name you would like to upload:");
		send_key = gpg.gen_key(send_data)
		fileSize=os.stat(fileName).st_size 
		if fileSize < 1048576: 
			with open(fileName, 'rb') as f:
				encrypted_file = gpg.encrypt_file(f, str(send_key),output='encr.txt')
			with open('encr.txt', 'r') as my_file:
				conn.put_object(container_name,
					fileName,
					contents= my_file,
					content_type='text/plain')
			print "Files %s uploaded successfully." % fileName		
		else:
			print "File Size exceeds 1MB"
			loop=False	
    elif choice==2:
        fileName=raw_input("Please enter file name you would like to retrieve:");
	try:
		obj = conn.get_object(container_name, fileName)
		with open(fileName, 'w') as my_file:
			my_file.write(obj[1])
		with open('encr.txt', 'r') as f:
			decrypted_file = gpg.decrypt_file(f, passphrase='send',output=fileName)
			print "File %s downloaded successfully." % fileName
	except:
		print "Not on cloud"		
    elif choice==3:
        fileName=raw_input("Please enter file name you would like to delete:");
	try:
		conn.delete_object(container_name, fileName)
		print "File %s deleted successfully." % fileName
	except:
		print "Not on cloud"
    elif choice==4:
        print ("List of files:")
	for container in conn.get_account()[1]:
		for data in conn.get_container(container['name'])[1]:
			print '{0}t size: {1}t date: {2}'.format(data['name'], data['bytes'], data['last_modified'])
    elif choice==5:
        loop=False 		
    else:
        raw_input("Wrong option selection. Enter any key to try again..")