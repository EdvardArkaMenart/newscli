import urllib3
from bs4 import BeautifulSoup

http = urllib3.PoolManager()
resp = urllib3.request("get", "https://www.vg.no")
data_bytes = resp.data
data_string = data_bytes.decode("utf-8")
soup = BeautifulSoup(data_string, 'html.parser')
head_tag = soup.head
results = soup.find(id="hovedlopet")

job_cards = results.find_all("div", class_="articles")
for job_card in job_cards:
    title_element = job_card.find("h2", class_="title")
    company_element = job_card.find("h3", class_="company")
    location_element = job_card.find("p", class_="location")
    print(title_element)
    print(company_element)
    print(location_element)
    print()
#print(soup.find_all('a'))
#print(len(list(soup.descendants)))
#print(head_tag.contents)
#print(soup.text)
#for link in soup.find_all('a'):
    #print(link.get('href'))