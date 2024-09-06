from requests import post 
from bs4 import BeautifulSoup 
from datetime import datatime,timedelta

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
