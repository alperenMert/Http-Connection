import urllib.request
import urllib.parse

#header içerisine data verisini yazmak
url="http://github.com"

data={
    "username":"Alperen",
    "password":"123"
}

parse_data=urllib.parse.urlencode(data) # data sitenin okuyabileceği forma getirildi
request =urllib.request.Request(url, data=parse_data.encode("utf-8")) # encode
source=urllib.request.urlopen(request) # requesti gönder
