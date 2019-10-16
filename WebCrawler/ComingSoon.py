import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import detail
import MongoDAO as DAO

mDao = DAO.MongoDAO('comingsoon')

scrap = detail.ImgCrawler()
# 플랫폼별로 출시예정작 정보를 가져오기위해 리스트에 담음
code_list = ['ps4', 'xboxone', 'switch', 'pc']
# 페이지를 0페이지부터 10페이지까지 돌기위해 리스트에 담음
page_list = range(10)

# 플랫폼 순회
for game in code_list:
    # page 순회
    for page in page_list:
        url = 'https://www.metacritic.com/browse/games/release-date/coming-soon/{}/date?page={}'.format(game, page)
        # 사이트에서 비정상적인 request를 요청하면 403에러가 뜨는걸 우회하는 방법 : url + header 값을 가져와서 넣어주면 해결
        headers = {'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
        resp = requests.get(url, headers=headers)
        soup = BeautifulSoup(resp.text, 'html.parser')
        coming_list = soup.select('li.game_product')
        # coming_list에 값이 없으면 부레이키
        if len(coming_list) == 0:
            break
        # comin_list에서 필요한 정보 추출
        for coming in coming_list:
            name = coming.select('div.product_title > a')[0].text.strip()
            date = coming.select('span.data')[1].text
            # 이미지를 가져오기 위한 href
            href = coming.select('div.product_title > a')[0].get('href')
            img = scrap.img_crawler(href)
            data = {'platform': game, 'c_name': name, 'c_date': date, 'c_img': img}
            mDao.mongo_write(data)
            print(name)
            print(date)
            print(img)
            print(game)
            print('--------------------------------')