import paramiko
import time
import getpass


print("""
*******************************************\n
\nLegacy/SDWAN\n
Version: 1.0 
\n*******************************************
""")

ip = input("Enter the IP of the device you are connecting to:  ")
device_type = input("""
\nINFO: Checks Available:\n 
Legacy Check [1] \nSDWAN Check  [2]\nINFO:  Select Check: """)

username = input("What is your username: ")
password = getpass.getpass(prompt="What is your password?: ")

if device_type == "1":
    print("\nINFO: You are connecting to ", ip, "\n")

    pre_ssh_conn = paramiko.SSHClient()
    pre_ssh_conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    pre_ssh_conn.connect(ip, port=22, username=username,
                        password=password,
                        look_for_keys=False, allow_agent=False)

    ssh_conn = pre_ssh_conn.invoke_shell()
    banner_output = ssh_conn.recv(65535)

#   Legacy Commands
#   Legacy Commands provided in email
#   copied and pasted the commands

    ssh_conn.send("show ip route \n")
    time.sleep(1)
    ssh_conn.send("show ip bgp summary\n")
    time.sleep(1)
    ssh_conn.send("show interface gi0/0\n")
    time.sleep(1)
    ssh_conn.send("show ip bgp sum\n")
    time.sleep(1)
    ssh_conn.send("ping 10.62.10.12 rep 100 size 1024  \n") #less than 120
    time.sleep(1)
    ssh_conn.send("show standby brief \n")
    time.sleep(1)
    ssh_conn.send("\nexit\n")
    time.sleep(1)

    output_lr = ssh_conn.recv(65535)
    print(output_lr.decode('utf-8'))


# SDWAN Check
# commands for SDWAN Stores Provided:
#Commands for SD-WAN stores:
#show bfd sessions
#show app-route stats local-color mpls | tab
#show app-route stats local-color blue | tab
#show app-route stats local-color green | tab
#show vrrp interfaces | tab
#Type 1 - MPLS and Green
#Type 2 - MPLS , Blue is for the latency checks
#show control connections


elif device_type == "2":
    print("\nINFO: You are connecting to ", ip, "\n")

    pre_ssh_conn = paramiko.SSHClient()
    pre_ssh_conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    pre_ssh_conn.connect(ip, port=22, username=username,
                         password=password,
                         look_for_keys=False, allow_agent=False)

    ssh_conn_sw = pre_ssh_conn.invoke_shell()
    banner_output = ssh_conn_sw.recv(77535)

    ssh_conn_sw.send("show bfd sessions\n")
    time.sleep(5)
    ssh_conn_sw.send("\nshow app-route stats local-color mpls | tab\n")
    time.sleep(3)
    ssh_conn_sw.send("\nshow app-route stats local-color blue | tab\n")
    time.sleep(1)
    ssh_conn_sw.send("\nshow app-route stats local-color green | tab n")
    time.sleep(1)
    ssh_conn_sw.send("\nshow vrrp interfaces | tab\n")
    time.sleep(5)
    ssh_conn_sw.send("\nshow control connections\n")
    time.sleep(1)
    ssh_conn_sw.send("\nexit\n")
    time.sleep(1)

    output = ssh_conn_sw.recv(77535)
    print(output.decode('utf-8'))


def log_file():
    # Write Logfile to Desktop
    lg = "C:/Users/adiker/Desktop/" + username + "-" + device_type + "-" + ip + ".log"
    logfile = open(lg, "wb")
    logfile.write(output)
    print("\nLog file Created: " + lg)
