import sys, paramiko, getpass

host_name = sys.argv[1]
port_name = int(sys.argv[2])
uname = sys.argv[3]
pathWhere = sys.argv[4]
prefix = sys.argv[5]
counts = int(sys.argv[6])
mode = sys.argv[7]

print('Enter user\" '+ uname + '\" password:')
user_password = getpass.getpass()


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host_name, port_name, uname, user_password, look_for_keys=False, allow_agent=False)

for i in range(1,counts+1):
    stdin, stdout, stderr = ssh.exec_command('mkdir -m' + mode + ' ' + pathWhere + '/' + prefix + str(i))
    
print('Folder is created')

ssh.close()
