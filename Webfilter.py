#!/bin/python
#This python program prompts the user for a web which he want to block and then adding the FQDN with the local host address to the etc/hosts

#importing the time library
import time
from datetime import datetime as dt
#environment variables
hosts_path = r"hosts.txt"
Lo0 = "127.0.0.1"

#prompting the user for details regarding the webpage block and the working hours of the program
website_list = raw_input ("Fill the FQDN of the website you want to block: ")
working_hours = raw_input ("Do you want the website to be blocked only on working hours? (Y/N)")

 
def filterFunction(website_list):
	for website in website_list:
		with open(hosts_path, 'a') as file:
			if "www" in website:
				file.write(Lo0 +  website_list + "\n")
			else:
				file.write(Lo0 + " " + "www." +  website_list + "\n")

if working_hours.lower() == "n":
	filterFunction(website_list)
elif working_hours.lower() == "y":
	if dt(dt.now().year, dt.now().month, dt.now().day,8) < dt(dt.now().year, dt.now().month, dt.now().day,18):
		with open(hosts_path,'r+') as file:
			content=file.read()
			for website in website_list:
				if website in content:
					pass
				else:
					file.write(Lo0 + " " + website_list + "\n")
	else:
		with open(hosts_path, 'r+') as file:
			content=file.readlines()
			file.seek(0)
			for line in content:
				if not any(website in line for website in website_list):
					file.write(line)
				file.truncate()
			time.sleep(2.5)
