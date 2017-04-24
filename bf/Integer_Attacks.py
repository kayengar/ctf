#1 Overflow
def getBigInteger32():
    return pow(2, 32)

def getBigInteger64():
    return pow(2, 64)

#2 Underflow
def getSmallInteger32():
    return pow(2, -32)

def getSmallInteger64():
    return pow(2, -64)


def getMap():
    d = {}
    d['0'] = getBigInteger32()
    d['1'] = getBigInteger64()
    d['2'] = getSmallInteger32()
    d['3'] = getSmallInteger64()