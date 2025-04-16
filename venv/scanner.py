import nmap
import requests

def scan_ports(target):
    nm = nmap.PortScanner()
    nm.scan(target, '1-1024')  # Scan ports 1-1024
    results = []

    for host in nm.all_hosts():
        for proto in nm[host].all_protocols():
            for port in nm[host][proto].keys():
                service = nm[host][proto][port]['name']
                state = nm[host][proto][port]['state']
                results.append({"port": port, "service": service, "state": state})

    return results



def get_vulnerabilities(service, version):
    url = f"https://vulners.com/api/v3/burp/software/?software={service}&version={version}"
    response = requests.get(url).json()
    vulnerabilities = []

    if 'data' in response:
        for vuln in response['data']:
            vulnerabilities.append({"CVE": vuln['id'], "description": vuln['title']})

    return vulnerabilities







