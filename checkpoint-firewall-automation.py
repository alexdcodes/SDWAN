# Alex Diker 
import getpass
import paramiko
import xlsxwriter
import time
import datetime
import smtplib, ssl

command1 = "uptime"
command2 = "/bin/asg stat vs all"
command3 = "asg resource"
command4 = "g_uptime"
command5 = "g_fw ctl pstat | grep watermark"
command6 = "asg resource | grep Memory"
command7 = "asg resource | grep log"
command8 = "g_all mpstat"
command9 = "asg_cores_util"
commanda = "asg stat -v"


def write_log_raw():
    tnow = datetime.datetime.now()
    lg = "log/" + ip1 + "-" + username + ".log"
    logfile = open(lg, "w")
    logfile.write("Username: " + username + "  Device: " + ip1 + "  Time: " + tnow.strftime("%Y-%m-%d %H:%M:%S") + "\n\n")
    logfile.write(output1)
    print("\nINFO: Log file created in location: ", lg)
    logfile.close()


def create_log(filename):
    print("INFO: Creating the log file: \n")
    print("\n ", filename)
    return filename


def file_name(name="Default.xlxs"):
    """ Allows user to set file name """
    print("INFO: file created: " + name + " within directory: ")


def create_work_book():
    workbook_name = input("INFO: What do you want to name the file: ")
    workbook = xlsxwriter.Workbook(workbook_name)
    worksheet = workbook.add_worksheet()

    data = (
        ['r1', 1000],
        ['r2', 100],
        ['r3', 300],
        ['r4', 50],
    )

    row = 0
    col = 0

    for server_name, server_data in (data):
        worksheet.write(row, col, server_name)
        worksheet.write(row, col + 1, server_data)
        row += 1

    worksheet.write(row, 0, 'Total')
    worksheet.write(row, 1, '=SUM(B1:B4)')   # Math formula

    workbook.close()


def send_mail_report():
    smtp_server = "mail.gmail.com"
    port = 587
    sender_email = "report@gmail.ca"
    email_password = "password"

    context = ssl.create_default_context()

    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()
        server.starttls(context=context)
        server.login(sender_email, email_password)
        server.quit()
    except Exception as e:
        print("INFO: Error Email Report Not Sent: ")
        print(e)
    # Send email report


print("***********************************")
print("             Firewall              ")
print("      Health Check / Checkpoint    ")
print("***********************************")
print("""
INFO: Message of the day, this will be changed to include instructions 
for the application. Right now the application will SSH into a firewall
device, and will execute commands, save the commands into a log file
and send the log file via SMTP email notification.  
""")
file = input("INFO: Name the log file: ")
ip1 = input("INFO: Enter the IP or Device List  : ")
username = input("INFO: What is your Username: ")
password = getpass.getpass(prompt="INFO: Enter your Password?: ")


pre_ssh_conn = paramiko.SSHClient()
pre_ssh_conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
pre_ssh_conn.connect(ip1, port=22, username=username,
                        password=password,
                        look_for_keys=False, allow_agent=False)

ssh_conn = pre_ssh_conn.invoke_shell()
banner_output = ssh_conn.recv(99535)

global output1, output2, output3, output4, output5, output6, output7
global output8, output9, outputa

stdin, stdout, stderr = pre_ssh_conn.exec_command(command1)
output1 = stdout.read().decode('ascii').strip("\n")
stdin, stdout, stderr = pre_ssh_conn.exec_command(command2)
output2 = stdout.read().decode('ascii').strip("\n")
stdin, stdout, stderr = pre_ssh_conn.exec_command(command3)
output3 = stdout.read().decode('ascii').strip("\n")
stdin, stdout, stderr = pre_ssh_conn.exec_command(command4)
output4 = stdout.read().decode('ascii').strip("\n")
stdin, stdout, stderr = pre_ssh_conn.exec_command(command5)
output5 = stdout.read().decode('ascii').strip("\n")
stdin, stdout, stderr = pre_ssh_conn.exec_command(command6)
output6 = stdout.read().decode('ascii').strip("\n")
stdin, stdout, stderr = pre_ssh_conn.exec_command(command7)
output7 = stdout.read().decode('ascii').strip("\n")
stdin, stdout, stderr = pre_ssh_conn.exec_command(command8)
output8 = stdout.read().decode('ascii').strip("\n")
stdin, stdout, stderr = pre_ssh_conn.exec_command(command9)
output9 = stdout.read().decode('ascii').strip("\n")
stdin, stdout, stderr = pre_ssh_conn.exec_command(commanda)
outputa = stdout.read().decode('ascii').strip("\n")


print("Command Output: ", output1)
print("\nCommand Output: ", output2)
print("\nCommand Output: ", output3)
print("\nCommand Output: ", output4)
print("\nCommand Output: ", output5)
print("\nCommand Output: ", output6)
print("\nCommand Output: ", output7)
print("\nCommand Output: ", output8)
print("\nCommand Output: ", output9)
print("\nCommand Output: ", outputa)
print('\n\nINFO: Commands Executed Successfully')
