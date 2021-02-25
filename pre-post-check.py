import paramiko
import time
import getpass


print("""
*******************************************\n
** Legacy/SDWAN Pre & Post Check **
\n*******************************************
""")

ip = input("Enter the IP of the device you are connecting to:  ")
device_type = input("""
INFO:  Devices Available:\n 
Cisco 2911 Router [1] \nCisco 2960 Switch [2] 
Cisco 9200 Switch [3] \nNX-Extreme Wireless Controller [4]
ENCS-NFVIS-5408 [5] \nENCS–vEdge–VNF [6]\n\nINFO:  Select Device: """)

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

    # Cisco 2911 Router Commands

    ssh_conn.send("terminal length 0\n")
    time.sleep(1)
    ssh_conn.send("show int GigabitEthernet0/0\n")
    time.sleep(1)
    ssh_conn.send("show ip route ospf\n")
    time.sleep(1)
    ssh_conn.send("show ip bgp sum\n")
    time.sleep(1)
    ssh_conn.send("show dmvpn\n")
    time.sleep(1)
    ssh_conn.send("show ip route bgp\n")
    time.sleep(1)
    ssh_conn.send("\nexit\n")
    time.sleep(1)

    output_lr = ssh_conn.recv(65535)
    print(output_lr.decode('utf-8'))


    lg = "C:/Users/alex/Desktop/" + username + "-" + device_type + "-" + ip + ".log"
    logfile = open(lg, "wb")
    logfile.write(output_lr)
    print("\nLog file Created: " + lg)


elif device_type == "2":
    print("\nINFO: You are connecting to ", ip, "\n")

    pre_ssh_conn = paramiko.SSHClient()
    pre_ssh_conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    pre_ssh_conn.connect(ip, port=22, username=username,
                         password=password,
                         look_for_keys=False, allow_agent=False)

    ssh_conn_sw = pre_ssh_conn.invoke_shell()
    banner_output = ssh_conn_sw.recv(77535)

    ssh_conn_sw.send("show cdp neighbors\n")
    time.sleep(5)
    ssh_conn_sw.send("\nshow mac address-table\n")
    time.sleep(3)
    ssh_conn_sw.send("\nshow int desc | i up / show int desc | i down\n")
    time.sleep(1)
    ssh_conn_sw.send("\nshow ver | i bin\n")
    time.sleep(1)
    ssh_conn_sw.send("\nshow switch\n")
    time.sleep(5)
    ssh_conn_sw.send("\nshow logging\n")
    time.sleep(1)
    ssh_conn_sw.send("\nshow spanning-tree blockedports\n")
    time.sleep(1)
    ssh_conn_sw.send("\nshow interfaces status err-disabled\n")
    time.sleep(1)
    ssh_conn_sw.send("\nRouter\n")
    time.sleep(1)
    ssh_conn_sw.send("\nexit\n")
    time.sleep(1)

    output = ssh_conn_sw.recv(77535)
    print(output.decode('utf-8'))

    # Write Logfile to Desktop
    lg = "C:/Users/alex/Desktop/" + username + "-" + device_type + "-" + ip + ".log"
    logfile = open(lg, "wb")
    logfile.write(output)
    print("\nLog file Created: " + lg)

elif device_type == "3":
    print("\nINFO: You are connecting to ", ip, "\n")

    pre_ssh_conn = paramiko.SSHClient()
    pre_ssh_conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    pre_ssh_conn.connect(ip, port=22, username=username,
                         password=password,
                         look_for_keys=False, allow_agent=False)

    ssh_conn_sw = pre_ssh_conn.invoke_shell()
    banner_output = ssh_conn_sw.recv(77535)

    ssh_conn_sw.send("show cdp neighbors\n")
    time.sleep(5)
    ssh_conn_sw.send("\nshow mac address-table\n")
    time.sleep(3)
    ssh_conn_sw.send("\nshow int desc | i up / show int desc | i down\n")
    time.sleep(1)
    ssh_conn_sw.send("\nshow ver | i bin\n")
    time.sleep(1)
    ssh_conn_sw.send("\nshow switch\n")
    time.sleep(5)
    ssh_conn_sw.send("\nshow logging\n")
    time.sleep(1)
    ssh_conn_sw.send("\nshow spanning-tree blockedports\n")
    time.sleep(1)
    ssh_conn_sw.send("\nshow interfaces status err-disabled\n")
    time.sleep(1)
    ssh_conn_sw.send("\nRouter\n")
    time.sleep(1)
    ssh_conn_sw.send("\nexit\n")
    time.sleep(1)

    output = ssh_conn_sw.recv(77535)
    print(output.decode('utf-8'))

    # Write Logfile to Desktop
    lg = "C:/Users/alex/Desktop/" + username + "-" + device_type + "-" + ip + ".log"
    logfile = open(lg, "wb")
    logfile.write(output)
    print("\nLog file Created: " + lg)

elif device_type == "4":
    print("\nINFO: You are connecting to ", ip, "\n")

    pre_ssh_conn = paramiko.SSHClient()
    pre_ssh_conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    pre_ssh_conn.connect(ip, port=22, username=username,
                         password=password,
                         look_for_keys=False, allow_agent=False)

    ssh_conn_sw = pre_ssh_conn.invoke_shell()
    banner_output = ssh_conn_sw.recv(89935)

    ssh_conn_sw.send("show global device-list | i 1005\n R")
    time.sleep(5)
    ssh_conn_sw.send("\nshow wireless ap on LS01005\n R")
    time.sleep(3)
    ssh_conn_sw.send("\nshow wireless client on LS01005\n R")
    time.sleep(1)
    ssh_conn_sw.send("\nshow adoption status | i 1005\n R")
    time.sleep(1)
    ssh_conn_sw.send("\nshow adoption offline | i 1005\n R")
    time.sleep(5)
    ssh_conn_sw.send("\nexit\n")
    time.sleep(1)

    output = ssh_conn_sw.recv(89935)
    print(output.decode('utf-8'))

    lg = "C:/Users/alex/Desktop/" + username + "-" + device_type + "-" + ip + ".log"
    logfile = open(lg, "wb")
    logfile.write(output)
    print("\nLog file Created: " + lg)
