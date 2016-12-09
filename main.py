from local_file import *
from nmap import *
from processes import *

ROOT_DIR = "Scanned_Projects"
create_new_dir(ROOT_DIR)

def gather_information(name, url):
    print("Getting domain name...")
    domain_name = get_domain_name(url)
    print("Getting IP address...")
    ip_address = get_ip_address(url)
    print("Getting NMAP Scan result...")
    nmap_res = get_nmap('-F -Pn ', ip_address)
    print("Getting ROBOT.txt file details...")
    robots_txt = get_robots_txt(url)
    print("Getting WHOIS Result...")
    whois_res = get_whois(domain_name)
    create_report(name, url, domain_name, ip_address, nmap_res, robots_txt, whois_res)

def create_report(name, url, domain_name, ip_address, nmap_res, robots_txt, whois_res):
    print("Creating project directory...")
    project_dir = ROOT_DIR + '/' + name
    create_new_dir(project_dir)
    print("DONE ! " + project_dir + " directory created...")
    print("Creating URL.txt file...")
    write_file(project_dir + "/URL.txt", url)
    print("DONE !")
    print("Creating Domain_name.txt file...")
    write_file(project_dir + "/Domain_name.txt", domain_name)
    print("DONE !")
    print("Creating IP_Address.txt file...")
    write_file(project_dir + "/IP_Address.txt", ip_address)
    print("DONE !")
    print("Creating NMAP result in NMAP.txt file...")
    write_file(project_dir + "/NMAP.txt", nmap_res)
    print("DONE !")
    print("Creating Robot.txt file...")
    write_file(project_dir + "/Robot.txt", robots_txt)
    print("DONE !")
    print("Creating WHOIS result in WHOIS.txt file...")
    write_file(project_dir + "/WHOIS.txt", whois_res)
    print("DONE !")
    print("TASK COMPLETED...")

gather_information("<PROJECT_NAME>", "PROJECT_URL")