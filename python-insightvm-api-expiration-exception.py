import os
import re
import sys
import itertools
import pprint
import requests
import json
import base64
import urllib3
import socket
import string
import time



'''
Author: Anthony Sarran
Date: 12/8/2022

Overview:
Rapid7 script that makes 2 GET request and one Put request to modify the expiration date on all vulnerability exceptions within Rapid7 InsightVM.
GET Request [~1~]: Grabs Total Page, then iterates through a range from 0 to totalpage and then executes GET Request [~2~]: Extract vulnerability exception ID off all pages.
Script will then draft payload with the information that was entered by the user prompt. Finally, script will execute PUT Request [~1~]: Modifying expiration time on all vulnerability exceptions.
'''


#*****[ Date ]*****#
y=input("Enter Year: (Example: 202x)")
m=input("Enter Month: (Example: 01 - 12)")
d=input("Enter Day: (Example: 01 - 31)")


#*****[ Credentials ]*****#
username = 'username'
password = 'creds'


#*****[ Timeouts ]*****#
socket.setdefaulttimeout(1)


#*****[ Disable Url Warning ]*****#
urllib3.disable_warning()



#*****[ Lists ]*****#
rid=[]
pgdata=[]
ged_id=[]
url=[]
rawdata=[]



'''*****[ Get Request [~1~] Total Pages ]*****'''
#***** Get Request[1]: Total Pages *****#
r7 = requests.get(url='URL', auth=((username), (password)), verify=False)


#***** Append List with Get Request *****#
pgdata.append(r7)

#***** Iterate List Containing Get Request *****#
for p in pgdata:

    #***** Json Object *****#
    json_object_pgdata = json.dumps(p.json(), sort_keys=True, indent=4)

    #***** Covert JSON Object to String *****#
    json_pgdata = json.loads(json_object_pgdata)

    #***** Covert JSON Object to String *****#
    totalpage = ((json_pgdata['page']['totalPages']))
    print(str(totalpage))

'''*****[ Get Request [~2~] Exceptions IDs ]*****'''
#***** Iterate through range of totalpages *****#
pg=0
for pg in range(totalpage):
    print(pg)

    #***** Get Request[2]: Exceptions IDs *****#
    r8 = requests.get(url='URL?page=' +str(pg), auth=((username), (password)), verify=False)

    #***** Append List with Get Request *****#
    get_id.append(r8)

    #***** Iterate through Get Request *****#
    for getid in get_id:

        #***** Json Object *****#
        json_object_getid = json.dumps(getid.json(), sort_keys=True, indent=4)

        #***** Convert Json Object to String *****#
        json_getid = json.loads(json_object_getid)


    #***** Iterate through resources json *****#
    for i in json_getid['resources']:

        #***** Extract Exception ID *****#
        reid = ((i['id']))

        #***** Append Exception ID to List *****#
        rid.append(reid)
        print(reid)

'''*****[ Payload ]*****'''
#***** Compose Data *****#
data=((y)+'-'+(m)+'-'+(d)+'T23:59:59.999z')
print(data)

#***** Compose Payload *****#
payload = json.dumps(data)

        
'''*****[ PUT Request [~1~] Modify Exception Time *****'''
#***** Authorization Header *****#
head = {'Content-Type':'application/json','Accept':'application/json','Accept-Encoding':'gzip'}


#*****[ Timeouts ]*****#
socket.setdefaulttimeout(1)


#*****[ Disable Url Warning ]*****#
urllib3.disable_warning()

           
#*****[ Iterate through RID ]*****#
for x in rid:

    #*****[ PUT Request [~1~]: Modification of Exception Time  ]*****#
    r = requests.put(url='url'+(str(x))+'/expires/', headers=head, auth=((username),(password)), verify=False, data=payload)

    #*****[ Success Code - 200 ]*****#
    print('Vulnerability Exception ID: ' + str(x) + ' ' + 'HTTP Response Code: ' +(str{r))
