import requests
import sys
import bs4
from bs4 import BeautifulSoup
import re
import threading
import http.client
import socket
import urllib3
from urllib.parse import urlparse

if len(sys.argv) == 3:
    domain_name = 'http://%s' % sys.argv[1]
    domain_name_2 = sys.argv[1]
    file_name = sys.argv[2]

print("  I'm Crawling .....")

req = requests.get(domain_name, timeout=60, allow_redirects=False)
html_parser = BeautifulSoup(req.text, 'html.parser')

primary_list = list()
Output2 = open(file_name, 'w', encoding="utf-8")
for Link in html_parser.find_all('a', href=True):
    Links = Link.get('href')
    if Links.startswith('/'):
        Links = 'https://' + domain_name_2 + Links
    elif Links.startswith('.'):
        Links = 'https://' + domain_name_2 + '/' + Links
    elif Links.startswith('https://') or Links.startswith('http://'):
        Links
    elif Links.startswith('javascript:'):
        continue
    else:
        Links = 'https://'+ domain_name_2 + '/' + Links
    print(Links, file = Output2)
    primary_list.append(Links)
    for i in primary_list:
        if i == i:
            del i
        else:
            continue

Output3 = open('Req_Res_data.txt', 'w', encoding="utf-8")
for iteration in primary_list:
    try:
        req2 = requests.get(iteration, timeout=60, allow_redirects=False)
    except socket.gaierror:
        pass
    except socket.error:
        pass
    except requests.ConnectionError as e:
        print(str(e))
        pass
    except requests.Timeout as e:
        print(str(e))
        pass
    except requests.RequestException as e:
        print(str(e))
        pass
    html_parser2 = BeautifulSoup(req2.text, 'html.parser')
    print('\n' , 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX NEW REQUEST XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', file = Output3)
    print('\n' ,iteration, '  Status Code: ', req2.status_code, '\n\n', 'Reponse Header: ','\n' , req2.headers, '\n\n', 'Reponse Body: ','\n' ,html_parser2 , file = Output3)

Secondary_list = list()
for Link2 in html_parser2.find_all('a', href=True):
    Links2 = Link2.get('href')
    if Links2.startswith('/'):
        Links2 = 'https://' + domain_name_2 + Links2
    elif Links.startswith('.'):
        Links2 = 'https://' + domain_name_2 + '/' + Links2
    elif Links2.startswith('https://') or Links2.startswith('http://'):
        Links
    elif Links.startswith('javascript:'):
        continue
    else:
        Links2 = 'https://'+ domain_name_2 + '/' + Links2
    print(Links2, file = Output2)
    primary_list.append(Links2)

for iteration2 in primary_list:
    req3 = requests.get(iteration2, timeout=30, allow_redirects=False)
    html_parser3 = BeautifulSoup(req3.text, 'html.parser')
    print('\n' , 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX NEW REQUEST XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', file = Output3)
    print('\n' ,iteration2, '  Status Code: ', req3.status_code, '\n\n', 'Reponse Header: ','\n' , req3.headers, '\n\n', 'Reponse Body: ','\n' ,html_parser3 , file = Output3)
print('There you Go!')
