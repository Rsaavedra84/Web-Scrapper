from bs4 import BeautifulSoup as bs
from urllib import request

class Scrapper:

    #source_code = source.text

    def get_titlelink(self, soup):
        items = soup.find_all('div', {'class': "MomentCapsuleSummary-details"})
        likes = soup.find_all('div', {'class': "MomentCapsuleLikesCount"})

        for item in items:
            print(item.a['href'] + " " + item.a['title'].replace("\n", "").strip() + self.get_likes(likes))

    def get_likes(self, likes):
        for likeCount in likes:
            return likeCount.text

def main():
    x = Scrapper()
    source = request.urlopen("https://twitter.com/i/moments")
    soup = bs(source, "html.parser")
    x.get_titlelink(soup)


if __name__ == '__main__':
        main()