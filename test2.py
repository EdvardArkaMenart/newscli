import urllib3
from bs4 import BeautifulSoup

http = urllib3.PoolManager()
resp = urllib3.request("get", "https://www.aftenposten.no")
data_bytes = resp.data
data_string = data_bytes.decode("utf-8")
soup = BeautifulSoup(data_string, 'html.parser')
head_tag = soup.head
results = soup.find("div", "content-main-wrapper")
job_cards = results.find_all("article")
for job_card in job_cards:
    title_element = job_card.find("h2", "title")
    company_element = job_card.find_all("a", href=True)
    print("*************************")
    if title_element:
        print(title_element.text.strip())
    for i in company_element:
        
        print(i["href"])