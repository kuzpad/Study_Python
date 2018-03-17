import subprocess
import time
#fresult = subprocess.run('touch test.txt', shell=True)
result = subprocess.run('open /Applications/LINE.app', shell=True)
time.sleep(5) #5秒まつ
result = subprocess.run('killall LINE', shell=True)
