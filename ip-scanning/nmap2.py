# 192.168.0.10 has hostname BRCM-LVG
# 192.168.0.12 has no reverse DNS entry
# 192.168.0.14 has no reverse DNS entry
# 192.168.0.15 has no reverse DNS entry
# 192.168.0.17 has no reverse DNS entry
# 192.168.0.19 has no reverse DNS entry
# 192.168.0.20 has no reverse DNS entry
# 192.168.0.21 has no reverse DNS entry
# 192.168.0.24 has no reverse DNS entry

import nmap

def detect_os(target_ip):
    scanner = nmap.PortScanner()
    scanner.scan(hosts=target_ip, arguments='-O')

    try:
        os_info = scanner[target_ip]['osclass']
        for os_item in os_info:
            print(f"OS detected: {os_item['osfamily']} ({os_item['osgen']}, {os_item['cpe']})")
    except KeyError:
        print("No OS information found")


def localInfo(target_ip, port_range):
    nmScan = nmap.PortScanner()
    # nmScan.scan(target_ip, port_range)
    print(nmScan['127.0.0.1']['osclass'])


if __name__ == "__main__":
    target_ip = "192.168.0.1"
    port_range = '21-443'
    detect_os(target_ip)
    localhost = "127.0.0.1"

    #localInfo(target_ip, port_range)
    nm = nmap.PortScanner()
    machine = nm.scan(target_ip, arguments='-O')
    print(machine['scan'][target_ip]['osmatch'][0]['osclass'][0]['osfamily'])