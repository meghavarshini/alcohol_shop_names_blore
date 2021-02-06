from bs4 import BeautifulSoup
import requests as req
resp = req.get('https://www.google.com/maps/search/wine/@12.9749149,77.5591986,13z/data=!3m1!4b1!4m9!2m8!3m6!1swine!2sBengaluru,+Karnataka,+India!3s0x3bae1670c9b44e6d:0xf8dfc3e8517e4fe0!4m2!1d77.5945627!2d12.9715987!6e6')
soup = BeautifulSoup(resp.text, 'lxml')
for tag in soup.find_all('a'):
        print(f'{tag.name}: {tag.text}')
# print(soup.title)
# print(soup.title.text)
# print(soup.title.parent)
# print(soup.prettify())
# if __name__ == '__main__':
#     print_hi('PyCharm')

