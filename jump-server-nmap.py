# Tony
# January 30, 2018
# Telnet Port Scan
#
# The Input is a hostname.txt located on the desktop.
# Hostname.txt contains a list of suspected IP addresses
#
#
#
#
#

import paramiko
import getpass
import io
import getpass
import unidecode
import xlsxwriter
import base64


# ***** Open Plain Text
f = open("telnet.txt")

# ***** Read & Store into Variable
ip=(f.read().splitlines())
f.close()

# ***** IP
olympus = "X.X.X.X"

# ***** Credentials 
username =  raw_input("Please Enter Username: ")
password =  getpass.getpass("Please Enter Password: ")


# ***** SSH
client=paramiko.SSHClient()
def connect_ssh(ip):
    try:
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.load_system_host_keys()
        client.connect(olympus, 22, username, password)
        print 'Attempting: '+(ip)
        stdin, stdout, stderr=client.exec_command("nmap"+""+" "+"-p"+" "+"23"+" "+str(ip))
        output=stdout.read()
        print (output)
        
        # ***** Create File & Write Bianry to the File *****
        with io.FileIO(str(name)+"output.csv", "a") as file:
            file.write(output)

            # *****Create Loop through input.txt
            for i in ip:
                print connect_ssh(i)
