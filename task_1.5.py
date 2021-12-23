import subprocess

args_1 = ['ping', 'yandex.ru']

subproc_ping = subprocess.Popen(args_1, stdout=subprocess.PIPE)
for line in subproc_ping.stdout:
            line = line.decode('cp866').encode('utf-8')
            print(line.decode('utf-8'))

args_2 = ['ping', 'youtube.com']
subproc_ping = subprocess.Popen(args_2, stdout=subprocess.PIPE)
for line in subproc_ping.stdout:
            line = line.decode('cp866').encode('utf-8')
            print(line.decode('utf-8'))