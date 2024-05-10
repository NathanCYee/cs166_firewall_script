import json
import sys
import subprocess

# read first argument in command
FILE_PATH = sys.argv[1]
ip_list = []

# Read log file
with open(FILE_PATH, "r") as f:
    # loop through each record
    for line in f.readlines():
        # load JSON into a dictionary
        line_json = json.loads(line)
        # extract the detected source IP of the attack and append to the IP list
        ip_list.append(line_json["source_ip"])

ip_list = set(ip_list)

print(ip_list)


# Apply log file to rules
for ip in ip_list:
    print(f"ufw insert 1 deny from {ip}")
    subprocess.call(["ufw", "insert", "1", "deny", "from", ip])
    print(f"iptables -A INPUT -s {ip} -p icmp -j DROP")
    subprocess.call(['iptables', '-A', 'INPUT', '-s', ip, '-p', 'icmp', '-j', 'DROP'])
