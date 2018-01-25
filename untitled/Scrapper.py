from bs4 import BeautifulSoup as bs
from urllib import request

source = request.urlopen("https://twitter.com/i/moments")

#source_code = source.text

soup = bs(source, "html.parser")

for item in soup.find_all('div', {'class':"MomentCapsuleSummary-details"}):
    print(item.text.replace("\n", ""))