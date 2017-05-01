import subprocess
import sys
from ictf import iCTF

info = iCTF('http://35.160.215.67/')
session = info.login('praveen0989@gmail.com','U9gHVyWAdWda')
key_info = session.get_ssh_keys()

with open('ctf_key', 'wb') as f:
    f.write(key_info['ctf_key'])

with open('root_key', 'wb') as f:
    f.write(key_info['root_key'])

print key_info['port']
print key_info['ip']

# cmd = "ssh -i ctf_key -p " + str(key_info['port']) + " ctf@" + key_info['ip']
# ret = subprocess.Popen(["ssh", "-p", str(key_info['port']), "-i", "ctf_key", "ctf@", key_info['ip']], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
