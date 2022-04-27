#!/usr/bin/python3
#In this cripts, I will connect to one of the sandbox, then send then command to see the ip interface brief.

#create the try block with an account user provided, password, and link.
#developer
#C1sco12345
#sandbox-iosxe-latest-1.cisco.com

try:
    #use netmiko to connect to sandbox with user and password provided.
    from ipaddress import ip_interface
    from netmiko import ConnectHandler
    username = input()
    user_password = input()
    destination_ip = input()
    # Template for Netmiko
    cisco = {
    'device_type': 'cisco_ios',
    'host': '1.1.1.1',
    'username': username,
    'password': user_password
    #'secret': 'mysecret'
    }
    cisco['host'] = destination_ip
    net_connect = ConnectHandler(**cisco)
    #connect and use find prompt to find the command
    net_connect.find_prompt()

    #create  varible, send command to see ip interface brief 
    ip_interface = net_connect.send_command('show ip interface brief')
    print(ip_interface)
except:
    #if input wrong will output the friendly message
    print('The input values was wrong, try again!!!')



#output of ip interface to new csv file.
with open('result.csv', 'w') as f:
    f.write(ip_interface)













