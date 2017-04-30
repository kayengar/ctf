from ictf import iCTF
import os
from exploit import *
service = None
session = None
flags = {}
temp_flags = []
target_list = None
# Sample Hashmap returned by 'get_service_list' method
''' [ {
	u'flag_id_description': u'Flags are identified by the note name.', 
	u'description': u'Password-protected note storage service in C.', 
	u'service_name': u'sample_c', 
	u'team_id': 0, 
	u'state': u'enabled', 
	u'upload_id': 1, 
	u'authors': u'UCSB', 
	u'service_id': 10001, 
	u'port': 20001
} ] '''
# [method for method in dir(object) if callable(getattr(object, method))]

def login():
	try:
		global session
		global service
		info = iCTF('http://35.167.152.77/')
		session = info.login('praveen0989@gmail.com','U9gHVyWAdWda')
		key_info = session.get_ssh_keys()
		'''
			
			with open('ctf_key', 'wb') as f:
			    f.write(key_info['ctf_key'])
			with open('root_key', 'wb') as f:
			    f.write(key_info['root_key'])
		'''
		service = session.get_service_list()
		print "Session created successfully. Good to go."
	except:
		print "Something wrong while creating session. Check up with Ashwin."

def services():
	for each in service:
		# print each['service_name']
		print each['description']
		print each['service_id']

# Sample Hashmap returned by 'get_targets' method
''' {
		'targets':	[ {
			u'flag_id': u'670989573', 
			u'team_name': u'WeLoveAdam', 
			u'hostname': u'team20', 
			u'port': 20001
		} ] 
} 	'''

def attack(service_id):
	global session
	global flags
	global temp_flags
	global target_list
	temp_flags = []
	try:
		target_service = session.get_targets(service_id)
		target_list = target_service['targets']
		count = 0
		for each in target_list:
			try:
                                #print " Flag id", each['flag_id'], "Team", each['hostname'], "Port", each['port']
                                # If flag found, check if it already exists with our dictionary.
                                print "port - ", each["port"]
                                port = str(each["port"])
                                os.system(exploit().format(port))
                                with open("resp.txt", "r") as response:
                                        temp = response.readlines()
                                for each in temp:
                                        line = each.split(' ')
                                        flag = [s for s in line if "FLG" in s]
#                               print flag
                                for ele in flag:
                                        if ele[-2:] == "\n":
                                                ele = ele[:-2]
#                                        print ele
					if ele not in flag:
						flags[ele] = 1
						temp_flags.append(ele)
			except:
				print "Check the exploit. Team", each['hostname'],"service seems to outsmart it. - Index",count
			count += 1
		submit()
	except:
		print "Check the service code sent to be attacked."

def teaminfo(index):
	global target_list
	team = target_list[index]	
	print "Try to find some info on what team ",team['hostname'], "has done."
	# Make changes in the teamexploit function.

def submit():
	try:
		global temp_flags
		if temp_flags != []:
			session.submit_flag(temp_flags)
			print "New flags were submitted successfully."
		else:
			print "No new flags were collected to submit. :("		
	except:
		print "Something wrong with the session. Check up with Ashwin."

def ticket():
	try:
		session.send_support_request("We need help!", "We have run into a problem")	
		print "Ticket raised successfully"
	except BaseException as e:
		print "Issue while raising the ticket."
		print e

def status():
	try:
		status = session.get_support_tickets()
		print status
	except BaseException as e:
		print "Issue while raising the ticket."
		print e

login()

'''
	t.submit_flag(["FLGxxxxxxx","FLGyyyyyyyyy", "FLGzzzzzzzzz"])
	t.send_support_request("Help I fork-bombed myself!", "I fork-bombed myself and am a total n00b.  Could you reboot our VM?")
	t.get_support_tickets()
	ssh -i </path/to/ctf_key> -p <port number> ctf@<the_ip_here>
'''


