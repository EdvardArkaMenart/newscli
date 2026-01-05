import urllib3
from bs4 import BeautifulSoup

def aftenposten_articles():       
    soup = make_soup("https://www.aftenposten.no") 
    results = soup.find("div", "content-main-wrapper")
    articles = results.find_all("article")
    articles_list = []

    for article in articles:
        headline = article.find("h2", "title")
        article_link = article.find_all("a", href=True)
        if headline:
            for i in article_link:
                link = i["href"]
            d = dict(headline = headline.text.strip, link = link)
            articles_list.append(d)
    return(articles_list)

def article_scaner(unfiltered_articles, filter):
    for l in unfiltered_articles:
        u = l["link"]
        soup = make_soup(u)
        results = soup.find(id="main")
        article = results.find_all("div")
        for article_text in article:
            print("**********")
            a = article_text.find("a")
            if a:
                print(a.text.strip())          

def get_input():
    print("Skriv stikkord for å finne relevant artikel")
    i = input().lower().split()
    if not i:
        return(False)
    return(i)

def make_soup(url):
    resp = urllib3.request("get", url)
    data_bytes = resp.data
    data_string = data_bytes.decode("utf-8")
    soup = BeautifulSoup(data_string, 'html.parser')
    return(soup)

def nrk_articles():   
    soup = make_soup("https://www.nrk.no")  
    results = soup.find(id="kurator_main")
    articles = results.find_all("div", "kur-room")
    #print(articles)
    for article in articles:
        headline = article.find("h2" )
        article_url = article.find_all("a", href=True)
        special_headline = article.find("h3")
        print("*************************")
        if special_headline:
            print(special_headline)
        if headline:
            print(headline.text.strip())
        for i in article_url:
            print(i["href"])

def vg_articles():   
    soup = make_soup("https://www.vg.no")    
    results = soup.find(id="hovedlopet")
    articles = results.find_all("div", "article-container")

    for article in articles:
        headline_big = article.find("h2", class_="headline")
        article_url = article.find_all("a", href=True)
        headline_small = article.find("span", role="presentation")
        print("*************************")
        if headline_small:
            print(headline_small.text)
        print(headline_big.text.strip())
        for i in article_url:
            print(i["href"])