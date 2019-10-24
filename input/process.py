import sys
import subprocess
pl = subprocess.Popen(["tasklist.exe"], shell=True, stdout=subprocess.PIPE)
output = pl.communicate()[0]
print(output.decode('utf-8'))