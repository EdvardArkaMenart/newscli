import urllib3
from bs4 import BeautifulSoup

http = urllib3.PoolManager()
resp = urllib3.request("get", "https://www.nrk.no")
data_bytes = resp.data
data_string = data_bytes.decode("utf-8")
soup = BeautifulSoup(data_string, 'html.parser')
head_tag = soup.head
results = soup.find(id="kurator_main")
job_cards = results.find_all("div", class_="kur-floor__content lp_flow")
#print(job_cards)
for job_card in job_cards:
    title_element = job_card.find("h2" )
    company_element = job_card.find_all("a", href=True)
    #location_element = job_card.find("span", role="presentation")
    print("*************************")
    #if location_element:
        #print(location_element.text)
    if title_element:
        print(title_element.text.strip())
    for i in company_element:
        
        print(i["href"])