import os
from processes import get_ip_address

def get_nmap(options, ip):
    command = "nmap "+ options + " " + ip
    process = os.popen(command)
    results = str(process.read())
    return (results)
#print(get_nmap('-F -Pn', get_ip_address("themrinalsinha.com")))