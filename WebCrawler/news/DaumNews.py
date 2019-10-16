# 다음 뉴스 1건 출력(제목, 작성자, 작성일자, 내용)

import requests
from bs4 import BeautifulSoup
# url 설정
url = 'https://news.v.daum.net/v/20191001091306434'
resp =requests.get(url)
soup = BeautifulSoup(resp.text,'html.parser')
# 수집
title = soup.select('h3.tit_view')[0].text.strip()
reporter = soup.select('span.txt_info')[0].text.strip()[:3]
reg_date = soup.select('span.txt_info')[1].text.strip()[3:13]

contents = ''
for p in soup.select('div#harmonyContainer p'):
    contents += p.text.strip()
# 출력
print('제목 : ', title)
print('기자 : ', reporter)
print('작성일자 : ', reg_date)
print('내용 : ', contents)