import nmap

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
