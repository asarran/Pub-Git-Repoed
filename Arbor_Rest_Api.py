#Created by Anthony Sarran
#July 09, 2018
#Python 2.7
#
#
#Arbor REST API Script [PULL]:
'''
//REST API AUTHENTICATION
API Authentication Function Takes Two Input: (TOKEN, URL)
Python Disables TLS Warnings

//JSON OBJECT HANDLING
Converts Response Fron JSON to String with JSON DUMP [USED FOR TESTING]
Convert Response to JSON Object using JSON LOAD*

//EXCEL [XLSXWRITER]
OPEN Excel Workbook
OPEN Excel Worksheet

//FOR LOOP
LOOP through JSON Object {JSON OBJECT = DICTIONARY}
Each block consits of KEY and SUBKEY;

Purpose of LOOP Increment through each block of the JSON OBJECT.
Iterations represneted by the variable a

Created variables [name, bgp, flow]
Store JSON [KEY, Iteration & SUBKEY] into Variables


//Array
Store Variables into Array RESERVED FOR PRINTING

//EXCEL
Write Variable into Excel;
Use LOOP Increment Variables to Build ROWS
'''


from __future__ import print_function
import requests
import json
import urllib3
import io
import getpass
import unidecode
import xlsxwriter
import base64
import pprint
import pandas as pd
import numpy as np
from datetime import timedelta
import datetime

 


#Get Current Date
today = datetime.date.today()

#Convert Current Date to String
cdate = str(today)

#Current Date Break Down
day = (cdate[8:10])
mon = (cdate[5:7])
yea = (cdate[0:4])

#print (day)
#print (mon)
#print (yea)


#Get Last Week Date
week = today - datetime.timedelta(days=7)
print (week)

#Convert Current Date to String
sweek = str(week)

#Current Date Break Down
lday = (sweek[8:10])
lmon = (sweek[5:7])
lyea = (sweek[0:4])

#print (lday)
#print (lmon)
#print (lyea)



# URL 
url = 'https://sp.example.com/api/sp/alerts/?filter=/data/attributes/classification="Verified%20Attack"+AND+/data/attributes/start_time+%3E+'+str(lyea)+'%2D'+str(lmon)+'%2D'+str(lday)
#print (url)


# Token
token = 'token'

# Disables SSL Warnings: Not Ideal
requests.packages.urllib3.disable_warnings()
response = requests.get(url, verify=False,
                    headers={"X-Arbux-APIToken": token})

# Converts Response to String, Sort, Indent, and Print
json_object = json.dumps(response.json(), sort_keys=True, indent=4)

# Convert JSON Language to Script
jsonResponse=json.loads(json_object)
#pprint.pprint(jsonResponse)


#[RESERVED FOR T_SHOOT]
#print (json_object)


#Create Array For Each Data Set
mylist = []
myalert = []
myclass = []
mystart = []
mystop = []
myfast = []
myrouter = []
myhost = []
mybps = []
mypps = []
mymisuse = []


for i in jsonResponse['data']:
     if i['attributes']['alert_class'] == 'dos':
          alertid = ((i['id']))
          classification = ((i['attributes']['classification']))
          starttime = ((i['attributes']['start_time']))
          stoptime = ((i['attributes']['stop_time']))
          fastdetect = ((i['attributes']['subobject']['fast_detected']))
          router = ((i['attributes']['subobject']['impact_boundary']))
          hostip = ((i['attributes']['subobject']['host_address']))
          bps = ((i['attributes']['subobject']['impact_bps']))
          pps = ((i['attributes']['subobject']['impact_pps']))
          misuse = ((i['attributes']['subobject']['misuse_types']))

          #Store Values into Array
          mylist.append({'Alert ID': alertid, 'Classification': classification, 'Start Time': starttime, 'Stop Time': stoptime, 'Fast Flood': fastdetect, 'Router': router, 'Victim': hostip, 'BPS': bps, 'PPS': pps, 'Misuse': misuse})

          myalert.append({'Alert ID': alertid})
          myclass.append({'Classification': classification})
          mystart.append({'Start Time': starttime})
          mystop.append({'Stop TIme': stoptime})
          myfast.append({'Fast Flood': fastdetect})
          myrouter.append({'Router': router})
          myhost.append({'Victim': hostip})
          mybps.append({'BPS': bps})
          mypps.append({'PPS': pps})
          mymisuse.append({'Misuse': misuse})

          
          #Pandas Data Frame
          #df0 = pd.DataFrame(data=mylist)
          df0 = pd.DataFrame(data=myalert)                                                                                                                                                                                                                                                                                                                                                                                                                               
          df1 = pd.DataFrame(data=myclass)  
          df2 = pd.DataFrame(data=mystart)
          df3 = pd.DataFrame(data=mystop)
          df4 = pd.DataFrame(data=myfast)
          df5 = pd.DataFrame(data=myrouter)
          df6 = pd.DataFrame(data=myhost)
          df7 = pd.DataFrame(data=mybps)
          df8 = pd.DataFrame(data=mypps)
          df9 = pd.DataFrame(data=mymisuse)



          
          #Pandas Writer
          writer = pd.ExcelWriter('Verified_Attacks.xlsx', engine='xlsxwriter')

          #Pandas Writer
          #df0.to_excel(writer, sheet_name='Sheet1', header=True, index=False)
          df0.to_excel(writer, sheet_name='Sheet1', header=True, index=False, startcol=0)
          df1.to_excel(writer, sheet_name='Sheet1', header=True, index=False, startcol=1)
          df2.to_excel(writer, sheet_name='Sheet1', header=True, index=False, startcol=2)
          df3.to_excel(writer, sheet_name='Sheet1', header=True, index=False, startcol=3)
          df4.to_excel(writer, sheet_name='Sheet1', header=True, index=False, startcol=4)
          df5.to_excel(writer, sheet_name='Sheet1', header=True, index=False, startcol=5)
          df6.to_excel(writer, sheet_name='Sheet1', header=True, index=False, startcol=6)
          df7.to_excel(writer, sheet_name='Sheet1', header=True, index=False, startcol=7)
          df8.to_excel(writer, sheet_name='Sheet1', header=True, index=False, startcol=8)
          df9.to_excel(writer, sheet_name='Sheet1', header=True, index=False, startcol=9)

          #Pandas Save 
          writer.save()

          # Saves content to file
          with open('Verified_Attacks.txt', 'a') as f:
               for i in (mylist):
                    f.write(repr(i)+'\n')


#Outlook Email Import SMTPLIB
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
  
fromaddr = '*******@alticeusa.com'
toaddr = '***********@alticeusa.com'
  
# IMEMultipart
msg = MIMEMultipart()
 
# storing the senders email address  
msg['From'] = fromaddr
 
# storing the receivers email address 
msg['To'] = toaddr
 
# storing the subject 
msg['Subject'] = (str(today)+": Verified Attacks Test")

# string to store the body of the mail
body = '''Good Morning, 

The attached excel consits of all verified attacks to MDPS subscibers from last month to '''+(cdate)+'.'+'''
Please ensure the following subscibers have been notified of these attacks.

********* TEST SCRIPT *********
Cumlative of All Verified Attacks of MDPS Customer will eventually be stored on *********** (pending server hardening) 
located within /Attacks/Verified/ in a flat file, similar to high alerts.

Script
1) Pull Data through REST API
2) Print To FILE
3) Print to Excel
4) Email To XYZ



Thank You,

'''
 
# attach the body with the msg instance
msg.attach(MIMEText(body, 'plain'))
 
# open the file to be sent 
filename = 'Verified_Attacks.xlsx'
attachment = open(filename, 'rb')
 
# instance of MIMEBase and named as p
p = MIMEBase('application', 'octet-stream')
 
# To change the payload into encoded form
p.set_payload((attachment).read())
 
# encode into base64
encoders.encode_base64(p)
  
p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
# attach the instance 'p' to instance 'msg'
msg.attach(p)
 
# creates SMTP session
s = smtplib.SMTP('smtp.office365.com', 587)
 
# start TLS for security
s.starttls()

# Credent
pw = base64.b64decode("$$$$$$$")

# Authentication
s.login(fromaddr, pw)
 
# Converts the Multipart msg into a string
text = msg.as_string()
 
# sending the mail
s.sendmail(fromaddr, toaddr, text)
 
# terminating the session
s.quit()

