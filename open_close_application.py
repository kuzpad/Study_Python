import subprocess
import time
#fresult = subprocess.run('touch test.txt', shell=True)
cnt = 0
while cnt < 5:
	result = subprocess.run('open /Applications/LINE.app', shell=True)
	time.sleep(5) #5秒まつ
	result = subprocess.run('killall LINE', shell=True)
	cnt += 1
	print(cnt)
