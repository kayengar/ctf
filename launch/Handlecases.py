# This python file is to handle 2 broad different cases - 1. web 2. Binary exploits

print 'Which case do you want to try? \nEnter 1 for web and 2 for binary exploits'
# Get input from attacker for options 1 and 2
s = raw_input()
# Handle different cases

if s == '1':
    print 'Welcome to web exploits - detect sql injection and cross site scripting attacks'
    s = False
    print 'Detecting sql injection attack'
    # Call the function to detect sql injection attack

    
    # If vulnerable set s = True and attack


    # If the web service is not vulnerable to sql injection attack
    if s != True:
        print 'Detecting cross site scripting attack'
        # Call the function to detect cross site scripting attack


        # If vulnerable attack

elif s == '2':
    print 'Welcome to binary exploits - brute force attacks'

else:
    print 'Invalid request'







