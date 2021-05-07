import requests
import sys
import bs4
from bs4 import BeautifulSoup

if len(sys.argv) == 3:
    domain_name = 'http://%s' % sys.argv[1]
    file_name = sys.argv[2]

req = requests.get(domain_name)
html_parser = BeautifulSoup(req.text, 'html.parser')
Final = html_parser.prettify()

Output = open(file_name, 'w', encoding="utf-8")
print('Status Code: ', req.status_code, '\n\n', 'Reponse Header: ','\n' , req.headers, '\n\n', 'Reponse Body: ','\n' , Final, file = Output)
