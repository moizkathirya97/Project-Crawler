import requests
import sys
import bs4
from bs4 import BeautifulSoup
import re

if len(sys.argv) == 3:
    domain_name = 'http://%s' % sys.argv[1]
    domain_name_2 = sys.argv[1]
    file_name = sys.argv[2]

req = requests.get(domain_name)
html_parser = BeautifulSoup(req.text, 'html.parser')

Output = open(file_name, 'w', encoding="utf-8")
print('Status Code: ', req.status_code, '\n\n', 'Reponse Header: ','\n' , req.headers, '\n\n', 'Reponse Body: ','\n' ,html_parser , file = Output)

Output2 = open('crawled_links.txt', 'w', encoding="utf-8")
for Link in html_parser.find_all('a', href=True):
    Links = Link.get('href')
    if Links.startswith('/'):
        Links = 'https:/' + domain_name_2 + Links
    elif Links.startswith('.'):
        Links = 'https://' + domain_name_2 + '/' + Links
    elif Links.startswith('https://'):
        Links
    elif Links.startswith('http://'):
        Links
    elif Links.startswith('javascript:'):
        Links
    else:
        Links = 'https://'+ domain_name_2 + '/' + Links
    print(Links, file = Output2)
