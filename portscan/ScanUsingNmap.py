import nmap

#TODO: test nmap. Coding on windows. Cant test here.
#After getting services list, perform specific attacks for different software.
#We have to cover apache as I think that will be the server used.
def getServicesList(host):
    nm = nmap.PortScanner()
    nm.scan(hosts = host, arguments='-n -sP -PE')
    return nm.scaninfo()

if __name__ == '__main__':
    getServicesList(host='127.0.0.1')