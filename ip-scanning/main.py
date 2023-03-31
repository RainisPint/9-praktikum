import os
from ping3 import ping
import socket

def ping_scan(network_prefix, start, end):
    live_hosts = []

    for ip_suffix in range(start, end + 1):
        ip = f"{network_prefix}.{ip_suffix}"
        try:
            response_time = ping(ip, timeout=0.5)
            if response_time is not None and response_time != False:
                print(f"{ip} is online, response time: {response_time} ms")
                live_hosts.append(ip)
            else:
                print(f"{ip} is offline")
        except Exception as e:
            print(f"Ping error: {e}")

    return live_hosts

def get_device_names(ip_list):
    device_names = []

    for ip in ip_list:
        try:
            hostname = socket.gethostbyaddr(ip)
            print(f"{ip} has hostname {hostname[0]}")
            device_names.append(hostname[0])
        except socket.herror:
            print(f"{ip} has no reverse DNS entry")
            device_names.append(ip)

    return device_names

if __name__ == "__main__":
    network_prefix = "192.168.0"
    start_ip_suffix = 1
    end_ip_suffix = 254

    online_devices = ping_scan(network_prefix, start_ip_suffix, end_ip_suffix)
    print("\nOnline devices:")
    device_names = get_device_names(online_devices)

    print("\nDevice names:")
    for name in device_names:
        print(name)