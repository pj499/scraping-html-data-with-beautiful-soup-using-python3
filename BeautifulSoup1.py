#==========Import required libraries==========
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

#==========Enter URL==========
name=input("Enter:")

#==========Connect the contents in HTML page in handler==========
content=urllib.request.urlopen(name).read()

#==========Organize the messy content of HTML page==========
soup=BeautifulSoup(content,'html.parser')

#==========Find the span tag==========
tags=soup('span')

#==========Evaluate sum==========
sum=0
for tag in tags:
    num=tag.contents
    n=num[0]
    n=int(n)
    sum=sum+n
print(sum)

