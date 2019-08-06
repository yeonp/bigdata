# 웹스크레이핑실습문제.py

from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import urllib.request as REQ
import urllib
# import json
# import folium

# 1.1
print('1.1','-'*50)
baseurl= 'http://www.menupan.com'
murl = '/restaurant/bestrest/bestrest.asp?pt=rt&areacode=dj201'

response = REQ.urlopen(baseurl+murl)
soup = BeautifulSoup( response, 'html.parser')

listData=[]
href=[]

ulList = soup.select_one( '.rankingList .list')
for li in ulList.select('li'):
    rank = li.select_one('.numTop,.rankNum').string
    href.append( li.select_one('.listName a')['href'] )
    listName = li.select_one('.listName').string
    listType = li.select_one('.listType').string
    listArea = li.select_one('.listArea').string
    listData.append({'랭킹':rank,
                     "상호명":listName,
                     "업종":listType,
                     "지역":listArea})

df= pd.DataFrame(listData)
print(df)


# 1.2
print('1.2','-'*50)
tel=[]
addr=[]
for h in href:
    response = REQ.urlopen(baseurl+h)
    sMenu = BeautifulSoup( response, 'html.parser')
    stel = sMenu.select_one('.tel1').string
    saddr = sMenu.select_one('.add1').string
    tel.append( stel )
    addr.append(saddr)
    # print(stel, saddr)

df['전화번호'] = tel
df['주소']=addr
print(df)

# 1.3
print('1.3','-'*50)
df.set_index('랭킹',inplace=True)
# inplace : bool, default False
# Modify the DataFrame in place (do not create a new object).

print(df)
df.to_excel("menu.xlsx")


#  1.4
print('1.4','-'*50)
m = df[ df['업종'].str.contains('한식')]
print(m)


#  1.5
print('1.5','-'*50)
area = df[ df['지역'].str.contains('대흥')]
print(area)