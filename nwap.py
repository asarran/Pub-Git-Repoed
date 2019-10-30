import nmap
import os
import io

# *****Open Plain Text ****
f = open ("/Users/XYZ/Desktop/sw.txt")

# *****Read & Store into Variable ****
ip = (f.read().splitlines())
f.close()

# *****Please Enter Port: ****
port = input("Please Enter Port:")

# *****Instantiate PortScanner ****
nmap = nmap.PortScanner() 

# *****Function
def nwap(ip):
    try:
        # *****Convert input into String ****
        sip = str(ip)

        # *****Contstructs Scan ****
        nmap.scan(sip, port) 

        # *****Displays Scanned Output ****
        pap = (nmap.command_line())
        sinfo = (nmap.scaninfo())

        # *****Converts Output to String ****
        spap = str(pap)
        sfo = str(sinfo)

        # **** Convert String to Bytes ****
        bpap = str.encode(spap)
        binfo = str.encode(sfo)

        # **** Displays Output ****
        print (bpap)
        print (binfo)
        
        # ***** Create File & Write Bianry to the File *****
        with io.FileIO('/Users/xyz/Desktop/outmap.txt', "a") as file:
            file.write(bpap)
            file.write(binfo)

    # ***** Needs to Close the Session *****
    except Exception as e:
        print ("*** Caught exception: %s: %s") % (e.__class__, e)
        try:
            f.close()
        except:
            pass

#*****Create Loop through input.txt 
for x in ip:
    print (nwap(x))
