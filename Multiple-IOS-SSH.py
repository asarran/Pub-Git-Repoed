# Anthuny
# October 15, 2019
# Python 3.X
# Cisco IOS Multiple Commands
# ______________________________________________________________________________________________
#                               ***WARNING***
#
# In the event the SSH Session is in "Zombie" mode and Spikes the CPU after terminating Session
#
#  [1] "show processes cpu | i SSH"                 | Displays CPU Performance for SSH Process
#  [2] "clear session [PID]"                        | Kill ZOmbie SSH Session, Enter PID from CMD [1]
#  [3] "show processes cpu | i SSH"                 | Displays CPU Performance for SSH Process
# 
# ______________________________________________________________________________________________
#                                ***OBJECTIVES***                              
# Script will SSH into All CISCO IOS Build and execute the following cammands:
#
#
#  [1] "show run int vlan"                                         | Displays VLAN CONFIG
#  [2] "show vlan | i 1"                                            | Displays PHYSICAL PORTS IN SPECIFIC VLAN
#  [3] "show mac address-table dynamic vlan 1"      | Displays LAYER 2 ADDRWSS WITHIN VLAN MAPPED TO PORTS
# 
#
# ______________________________________________________________________________________________
# 
#
#  [1] Script will open file read sw.txt 
#  [2] Script will prompt user for credentials
#  [3] Script will pass credentials to socket
#  [4] Script will build socket 
#  [5] Script will create a channel 
#  [6] Script will intiate SSH into device
#  [7] Script will execute the commands 
#  [8] Script will iterate through the list



import paramiko
import getpass
import sys
import io
import os
import pyautogui
import time


# *****Open Plain Text  
f = open ("/Users/name/Desktop/sw.txt")

# *****Read & Store into Variable
ip = (f.read().splitlines())
f.close()

# *****Please Enter Vlan
Vlan = input("Please Enter VLAN:")

# *****Username Credentials
username = input("Please Enter Username:")

# *****Password Options
password = pyautogui.password("Please Enter password")

# *****Test IP being iterated
print (ip)

#Creating Paramiko Client
client=paramiko.SSHClient()
def connect_ssh(ip):
    try:
        #Key Managment, Exception, and Build Connections
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(ip, 22, username,password,look_for_keys=False, allow_agent=False)
        
        #Print Statement Displays Current Connection Status
        print ("Connection Attempting to: " + (ip))

        #Invoke Shell Paramiko Object for Multiple Commands
        channel = client.get_transport().open_session()
        channel.invoke_shell()
        
        # ***** CMD[1] Show Vlan [X] ***** 
        channel.sendall input("Please Enter Command [1]:")
        CMD1 = (channel.recv(1024))
        time.sleep(1)
        print (CMD1)
        print ("\n")
        print ("\n")
        print ("\n")
        
        # ***** CMD[2] Show Vlan [X] ***** 
        channel.sendall input("Please Enter Command [2]:")
        CMD2 = (channel.recv(1024))
        time.sleep(1)
        print (CMD2)
        print ("\n")
        print ("\n")
        print ("\n")

        # ***** CMD[3] Show Vlan [X] ***** 
        channel.sendall input("Please Enter Command [3]:")
        CMD3 = (channel.recv(2048))
        time.sleep(3)
        print (CMD3)
        print ("\n")
        print ("\n")
        print ("\n")

        
        # **** Convert IP into String ****
        sip = str(ip)

        # **** Convert String to Bytes ****
        bip = str.encode(sip)
        
        # ***** Create File & Write Bianry to the File *****
        with io.FileIO('/Users/name/Desktop/outfile.txt', "a") as file:
            file.write(bip)
            file.write(CMD1)
            file.write(CMD2)
            file.write(CMD3)
  

    # ***** Needs to Close the Session *****
    except Exception as e:
        print ("*** Caught exception: %s: %s") % (e.__class__, e)
        try:
            channel.close()
            client.close()
        except:
            pass


# *****Create Loop through input.txt 
for i in ip:
    print (connect_ssh(i))
