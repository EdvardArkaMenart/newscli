import urllib3
from bs4 import BeautifulSoup

http = urllib3.PoolManager()
resp = urllib3.request("get", "https://www.vg.no")
data_bytes = resp.data
data_string = data_bytes.decode("utf-8")
soup = BeautifulSoup(data_string, 'html.parser')
head_tag = soup.head
print(soup.find_all('a'))
#print(len(list(soup.descendants)))
#print(head_tag.contents)
#print(soup.get_text())
#for link in soup.find_all('a'):
    #print(link.get('href'))