import requests
import Integer_Attacks
import String_attacks
import DateField_attacks

#endPoint - url
#params - list of objects containing param name, param type, param value
def getMethodAttacks(endPoint, params):
    endPoint = endPoint + "?"
    requestsList = []

    for i in range(len(params)):
        if params[i].type == 'int':
            dic = Integer_Attacks.getMap()
        elif params[i].type == 'string':
            dic = String_attacks.getStringsMap()
        elif params[i].type == 'date':
            dic = DateField_attacks.getInvalidDatesMap()

        for key, value in dic.iteritems():
            req = endPoint + params[i].name + "=" + value
            for j in range(i + 1, len(params)):
                req = req + "&" + params[j].name + '=' + params[j].value
            requestsList.add(req)

        endPoint = endPoint + params[i].name + "=" + params[i].value

#Add same parameters as above...
#But write to request body
def postMethodAttacks(endPoint, params):
    pass