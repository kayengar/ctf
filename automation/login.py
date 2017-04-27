import subprocess
from ictf import iCTF

info = iCTF('http://35.167.152.77/')
session = info.login('sheep@example.com','sheep')
key_info = session.get_ssh_keys()

with open('ctf_key', 'wb') as f:
    f.write(key_info['ctf_key'])

with open('root_key', 'wb') as f:
    f.write(key_info['root_key'])

# cmd = "ssh -i ctf_key -p " + str(key_info['port']) + " ctf@" + key_info['ip']
ret = subprocess.Popen(["ssh", "-i", "ctf_key", "-p", str(key_info['port']), "ctf@", key_info['ip']], stderr = subprocess.PIPE)
# errdata = ret.communicate()[1]