import urllib.request
from bs4 import BeautifulSoup
import  requests

if __name__ == '__main__':
    target = 'https://www.xuexi.cn/'

    # req = urllib.request.urlopen(target).read()
    # html = req.decode('UTF-8')
    response = requests.get(target)
    bf = BeautifulSoup(response.text)
    print(bf.div.text)

    for x in bf.find_all("a"):
        print(x['href'])
