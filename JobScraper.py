import requests
from bs4 import BeautifulSoup
import csv

r = requests.get('https://www.careers24.com/jobs/kw-web-developer/rmt-incl/')
print(r)
soup = BeautifulSoup(r.content, 'html.parser')
links=soup.find_all('i')

linkArr=[]
count=1
for link in links:
    d={}
    dataUrl=link.get('data-url')
    if dataUrl == None:\
        linkArr.append(d)
    else:
        d['Job Number'] = f'{count}'
        d['Link'] = link.get('data-url')
        count += 1
        print(link.get('data-url'))
        linkArr.append(d)

filename = 'jobs.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f,['Job Number','Link'])
    w.writeheader()
     
    w.writerows(linkArr)