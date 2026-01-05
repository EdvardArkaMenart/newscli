# finn resten av overskriften
# sjekke om artikel er synelig

import urllib3
from bs4 import BeautifulSoup
from test import *

keywords = False
while keywords is False:
    keywords = get_input()
unfiltered_articles_a = aftenposten_articles()
article_scaner(unfiltered_articles_a, keywords)
  