from urllib import  request, parse
import urllib

url = 'http://www.whoseme.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5603.400 QQBrowser/10.1.1775.400'
}
dict = {
    'name': 'Germey'
}

data = bytes(parse.urlencode(dict), encoding='utf8')
req = request.Request(url=url, data=data, headers=headers, method='POST')
response = request.urlopen(req)
print(response.read().decode('utf-8','ignore'))