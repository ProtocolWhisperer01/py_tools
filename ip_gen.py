#!/bin/python3

#############################################################################
## 									   ##
##	Title : IP Generator						   ## 	
##									   ##
##	Author : Ernest Odhiambo Elnino					   ##
##									   ##
##	Github : https://github.com/ProtocolWhisperer01 		   ##
#############################################################################

import ipaddress

def generate_ip_list(start_ip,end_ip):
	start = ipaddress.IPv4Address(start_ip)
	end = ipaddress.IPv4Address(end_ip)
	ips = []
	for ip in range(int(start), int(end)):
		ips.append(str(ipaddress.IPv4Address(ip)))
		
	return ips

start_ip = input("Enter your start IP address: ")
end_ip = input("Enter your end IP address: ")
file_name = input("Give file name (.txt): ")

with open(file_name, 'w') as file:
	for i in generate_ip_list(start_ip,end_ip):
		file.write('%s\n' % i)
	

	
