import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

name=input("Enter:")
content=urllib.request.urlopen(name).read()

sum=0
soup=BeautifulSoup(content,'html.parser')

tags=soup('span')

for tag in tags:
    num=tag.contents
    n=num[0]
    n=int(n)
    sum=sum+n
print(sum)

