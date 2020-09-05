import urllib.request

adress=input("Hangi siteye bağlanmak istersiniz:")

header={
    'User_agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4209.0 Safari/537.36'
}

istek=urllib.request.Request(adress, headers=header)  #istek hazırlandı

html= urllib.request.urlopen(istek) #istek gönderildi
print("\nİstediğiniz sitenin kaynak kodu: \n\n")

print(html.read())