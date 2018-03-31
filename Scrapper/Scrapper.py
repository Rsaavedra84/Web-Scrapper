from bs4 import BeautifulSoup as bs
from urllib import request
import pandas as pd

class Scrapper:

    def get_titlelink(self, soup):
        items = soup.find_all('div', {'class': "MomentCapsuleSummary-details"})
        likes = soup.find_all('div', {'class': "MomentCapsuleLikesCount"})

        titles = []
        links = []
        likesT = []    #LIKES TABLE

        for item in items:
            titles.append(item.a['title'].replace("\n", ""))
            links.append(item.a['href'].replace(" ", ""))

        for likeCount in likes:
            likesT.append(likeCount.text.replace("\n", "").lstrip())  #LEARNT ABOUT RSTRIP AND LSTRIP

        info = sorted(list(zip(titles, links, likesT)))

        for i in range(len(info)):
            print(info[i])

        df = pd.DataFrame(info, columns = ['Titles', 'Links', 'Likes'])
        df.to_csv("Twitter Data.csv")


def main():
    x = Scrapper()
    source = request.urlopen("https://twitter.com/i/moments")
    soup = bs(source, "html.parser")
    x.get_titlelink(soup)


if __name__ == '__main__':
        main()