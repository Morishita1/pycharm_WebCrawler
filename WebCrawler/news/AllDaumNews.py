import requests
from bs4 import BeautifulSoup

# url = Daum IT 전체기사
url = 'https://news.daum.net/breakingnews/digital'
resp = requests.get(url)
bs = BeautifulSoup(resp.text, 'html.parser')
news_list = bs.select('ul.list_news2 a.link_txt')

for news in news_list:
    news_url = news['href']
    doc = requests.get(news_url)
    soup = BeautifulSoup(doc.text, 'html.parser')

    # 기사 수집
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