import os, os.path,time
DIR='C:\\Tomcat\\apache-tomcat-8.5.30\\bin'
count=0
for name in os.listdir(DIR):
	if os.path.isfile(os.path.join(DIR, name)):
		count+=1
		print(name)
		print("Last Modified: %s" % time.ctime(os.path.getmtime(os.path.join(DIR, name))))
		print("Created: %s" % time.ctime(os.path.getctime(os.path.join(DIR, name))))
print('Total file in "{}" directory is {}'.format(DIR,count))
