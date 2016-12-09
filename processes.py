#To obatin the top level domain...

import os
import io
import urllib.request
from tld import get_tld

def get_domain_name(url):
    domain_name = get_tld(url)
    return (domain_name)
#print(get_domain_name("http://themrinalsinha.com/"))

def get_ip_address(url):
    command = "host " + url
    process = os.popen(command)
    results = str(process.read())
    marker = results.find("has address") + 12
    return (results[marker:].splitlines()[0])
#print(get_ip_address("themrinalsinha.com"))

def get_whois(url):
    command = "whois " + url
    process = os.popen(command)
    results = str(process.read())
    return (results)
#print(get_whois("themrinalsinha.com"))

#Finding Robots.txt
def get_robots_txt(url):
    if url.endswith('/'):
        path = url
    else:
        path = url + '/'
    req = urllib.request.urlopen(path + "robots.txt", data = None)
    data = io.TextIOWrapper(req, encoding='utf-8')
    return data.read()
#print(get_robots_txt('http://www.reddit.com/'))
