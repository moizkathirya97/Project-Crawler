import requests
import sys
import bs4
from bs4 import BeautifulSoup
import re

if len(sys.argv) == 3:
    domain_name = 'http://%s' % sys.argv[1]
    domain_name_2 = sys.argv[1]
    file_name = sys.argv[2]

req = requests.get(domain_name, allow_redirects=False)
html_parser = BeautifulSoup(req.text, 'html.parser')

Output = open(file_name, 'w', encoding="utf-8")
print('Status Code: ', req.status_code, '\n\n', 'Reponse Header: ','\n' , req.headers, '\n\n', 'Reponse Body: ','\n' ,html_parser , file = Output)

primary_list = list()
Output2 = open('crawled_links.txt', 'w', encoding="utf-8")
for Link in html_parser.find_all('a', href=True):
    Links = Link.get('href')
    if Links.startswith('/'):
        Links = 'https://' + domain_name_2 + Links
    elif Links.startswith('.'):
        Links = 'https://' + domain_name_2 + '/' + Links
    elif Links.startswith('https://') or Links.startswith('http://') or Links.startswith('javascript:'):
        continue
    else:
        Links = 'https://'+ domain_name_2 + '/' + Links
    print(Links, file = Output2)
    primary_list.append(Links)
Output3 = open("All_Responses.txt", 'w', encoding="utf-8")
for iteration in primary_list:
    req2 = requests.get(iteration, allow_redirects=False)
    html_parser2 = BeautifulSoup(req2.text, 'html.parser')
    print('Status Code: ', req2.status_code, '\n\n', 'Reponse Header: ','\n' , req2.headers, '\n\n', 'Reponse Body: ','\n' ,html_parser2 , file = Output3)

for Link2 in html_parser2.find_all('a', href=True):
    Links2 = Link2.get('href')
    if Links2.startswith('/'):
        Links2 = 'https://' + domain_name_2 + Links2
    elif Links.startswith('.'):
        Links2 = 'https://' + domain_name_2 + '/' + Links2
    elif Links2.startswith('https://') or Links2.startswith('http://') or Links2.startswith('javascript:'):
        continue
    else:
        Links2 = 'https://'+ domain_name_2 + '/' + Links2
    print(Links2, file = Output2)
    primary_list.append(Links2)
