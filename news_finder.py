# finn resten av overskriften
# sjekke om artikel er synelig

import urllib3
from bs4 import BeautifulSoup

http = urllib3.PoolManager()
resp = urllib3.request("get", "https://www.vg.no")
data_bytes = resp.data
data_string = data_bytes.decode("utf-8")
soup = BeautifulSoup(data_string, 'html.parser')
head_tag = soup.head
results = soup.find(id="hovedlopet")

job_cards = results.find_all("div", "article-container")
#print(job_cards)
for job_card in job_cards:
    title_element = job_card.find("h2", class_="headline")
    company_element = job_card.find_all("a", href=True)
    location_element = job_card.find("p", class_="location")
    #print(type(company_element))
    print("*************************")
    print(title_element.text.strip())
    for i in company_element:
        
        print(i["href"])
    
    #print(type(company_element))
    #print(location_element)
    #print()
#print(soup.find_all('a'))
#print(len(list(soup.descendants)))
#print(head_tag.contents)
#print(soup.text)
#for link in soup.find_all('a'):
    #print(link.get('href'))