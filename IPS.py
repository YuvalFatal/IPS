import subprocess

MY_PORT = '4444'

p = subprocess.Popen("sudo tcpdump -l -s 0 -i any port 4444", stdout=subprocess.PIPE, shell=True)

send_length = -4
recv_length = 0

for line in iter(p.stdout.readline, b''):	
	line = line.split(' > ')
	
	if line[0].split(' ')[-1].split('.')[-1] == MY_PORT:
		send_length += int(line[1].split(' ')[-1])
	else:
		recv_length += int(line[1].split(' ')[-1])
	
	if send_length > recv_length:
		print "Send: " + str(send_length)
		print "Recv: " + str(recv_length)

		p2 = subprocess.Popen("ps a | grep nc", 			stdout=subprocess.PIPE, shell=True)

		for row in iter(p2.stdout.readline, b''):
			pid = row.split(' ')[1]
			subprocess.Popen('kill -9 ' + str(pid), shell=True)
			break
		break


