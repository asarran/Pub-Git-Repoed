import requests
import json
import base64
import urllib3
import sys
import re
import os
import pprint
import pandas as pd


#***** [ Token ] *****#
token=('')

#***** [ Create Cookie ] *****#
cookies = {"access_token": token}

#***** [ Create Header ] *****#
headers = {"Accept": "application/json"}

#***** [ Get Request [~1~]: Grab CentOS Directory ] *****#
r = requests.get("https://api.pkgs.org/v1/search?query=bash&distributions=220", cookies=cookies, headers=headers)

#***** [ HTTP Code ] *****#
print(r)

#***** [ Create List ] *****#
pkgs_repo=[]
pkgs_id=[]
pkgs_name=[]

#***** [ Append List with Get Request ] *****#
pkgs_repo.append(r)

#***** [ Iterate List Containing Get Request ] *****#
for i in pkgs_repo:

    #***** [ Json Object ] *****#
    json_object_pkgs_repo = json.dumps(i.json(), sort_keys=True, indent=4)

    #***** { Covert JSON Object to String ] *****#
    json_pkgs = json.loads(json_object_pkgs_repo)
    pprint.pprint(json_pkgs)

'''
for x in json_pkgs:
    if x['distribution_id'] == 150:
        pkgsid = ((x['id']))
        pkgsname = ((x['name']))

        print(pkgsid)
        print(pkgsname)
        
'''
