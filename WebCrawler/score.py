import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import detail
import Creply as critic
import Ureply as user
import MongoDAO as DAO

# path = 'E:\Bigdata\webdriver\chromedriver.exe'
# driver = webdriver.Chrome(path)

page = 0
count = 0
i_scrap = detail.ImgCrawler()
c_scrap = critic.CReview()
u_scrap = user.UReview()
mDao = DAO.MongoDAO('metascore')
while True:
    url = 'https://www.metacritic.com/browse/games/score/metascore/90day/all/filtered?page={}'.format(page)
    # 사이트에서 비정상적인 request를 요청하면 403에러가 뜨는걸 우회하는 방법 : url + header 값을 가져와서 넣어주면 해결
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
    resp = requests.get(url, headers=headers)
    soup = BeautifulSoup(resp.text, 'html.parser')
    game_list = soup.select('li.game_product')
    if len(game_list) == 0:
        break
    for game in game_list:
        count += 1
        m_score = game.select('div.product_wrap div.metascore_w')[0].text
        name = game.select('div.product_title > a')[0].text.strip()
        # '('인덱스값 추출
        index = name.find('(')
        # 0번부터 인덱스까지의 값을 추출하고 공백 삭제
        game_name = name[:index].strip()
        # 인덱스값 + 1 부터 마지막값 전까지 추출
        _type = name[index+1:-1]
        u_score = game.select('li.product_avguserscore > span.textscore')[0].text
        href = game.select('div.product_title a')[0].get('href')
        game_code = href[6:]
        # 이미지 url
        img_src = i_scrap.img_crawler(href)
        # 전문가 평점 url
        c_scrap.c_crawler(href, game_code)
        # user 평점 url
        u_scrap.u_crawler(href, game_code)
        data = {'game_code': game_code,
                'm_score': m_score,
                'game_name': game_name,
                'type': _type,
                'u_score': u_score,
                'img_src': img_src}
        mDao.mongo_write(data)
        print("전문가 평점 :", m_score)
        print("게임명 :", game_name)
        print(game_code)
        print(href)
        print(_type)
        print("유저 평점 :", u_score)
        print("================================================================")

    page += 1
    print(page)
# driver.close()
