import socket
import pandas as pd
import openpyxl
import re
import sys
import os
import itertools

# ***** [ Declare Lists ] *****#
lookup = []
lookip = []

# ***** [ Read Excel File ] *****#
nslookup = pd.read_excel('nslookup.xlsx', sheet_name='Sheet1')

# ***** [ Iterate through column "fqdn" and "ip" ] *****#
for o,g in zip(nslookup['fqdn'], nslookup['ip'] ):
    lookup.append(o)
    lookip.append(g)

# ***** [ Declare Lists ] *****#
hostname = []
ipv4 = []

# ***** [ Iterate through list ] *****#
for i,p in zip(lookup, lookip):

    # ***** [ Lookup FQDN/IP socket functions ] *****#
    asset = socket.gethostbyname(str(i))
    ip = socket.getfqdn(str(p))

    # ***** [ output to lists ] *****#
    hostname.append(asset)
    ipv4.append(ip)

# ***** [ Print FQDN Lookups ] *****#
print('######## [FQDN] ########')   
for x, y in zip(lookup, hostname):
    print((str(x) + ', ' +  (str(y))))

# ***** [ print empty spaces  ] *****#          
print('                      ')

# ***** [ Print IP Lookups ] *****#
print('######## [IP] ########')   
for c, d in zip(lookip, ipv4):
    print((str(c) + ', ' +  (str(d))))
