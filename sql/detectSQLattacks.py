# This python file is to detect SQL attacks
import requests
def detectSQLattack():
    # Get the URL
    print 'Please enter the url : '
    url = raw_input()
    # Get the number of form fields
    print 'Please enter the number of form fields in the website : '
    n = raw_input()
    # Get the names and values in each of the form fields
    jsonData = {}
    for i in range(n):
        print 'Enter name of form field ',i+1
        fieldName = raw_input()
        print 'Enter value of form field ',i+1
        fieldValue = raw_input()
        jsonData[fieldName] = fieldValue
    # Request the url
    result = requests.post(url, jsonData)
    # Check the time
    if float(result.elapsed.total_seconds()) > 1:
        return 1
    else:
        return 0

