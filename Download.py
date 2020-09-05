import urllib.request

#google.com üzerindeki favicon.ico resim dosyasını indirmek
urllib.request.urlretrieve("http://google.com/favicon.ico", "indirilen.ico")