import requests

# 2019.10.07 by ChoLONG
# sc: Selenium과 BeautifulSoup를 사용하여
#     Daum 영화평(댓글, 작성자, 평점, 작성일자) 수집,
#     수집 된 데이터를 MongoDB에 저장하는 프로그램

from bs4 import BeautifulSoup
from selenium import webdriver
from pymongo import MongoClient

# MongoDB Connection
client = MongoClient('localhost', 27017) # 클래스 객체 할당(ip주소,
# MongoDB에 계정이 있거나 외부 IP인 경우
# DB_HOST = 'xxx.xx.xx.xxx:27017'
# DB_ID = 'root'
# DB_PW = 'pw'
# client = MongoClient('mongodb://%s:%s@%s' % (DB_ID, DB_PW, DB_HOST))
# selenium 설정

db = client['local'] # MongoDB의 'local' DB를 할당

collection = db.movie


def mongo_write(data):
    print('>> MongoDB write data!')
    collection.insert(data) # JSON Type = Dict Type(python)


path = 'E:\Bigdata\webdriver\chromedriver.exe'
driver = webdriver.Chrome(path)


# 웹 크롤링
def crawler(code):
    page = 1
    count = 0
    while True:
        url = 'https://movie.daum.net/moviedb/grade?movieId={}&type=netizen&page={}'.format(code, page)
        driver.get(url) # http:// 까지 적어야함
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        reply_list = soup.select('div.main_detail ul.list_review.list_netizen li')

        if reply_list == []:
            break

        for reply in reply_list:
            writer = reply.select('div.review_info a em')[0].text
            cont = reply.select('div.review_info p.desc_review')[0].text.strip()
            star_score = reply.select('div.review_info div.raking_grade em')[0].text
            reg_date = reply.select('div.review_info div.append_review span.info_append')[0].text.strip()[:10]

            data = {'star_score': star_score, 'writer': writer, 'cont': cont, 'reg_date': reg_date}

            # MongoDB에 댓글 저장
            mongo_write(data)

            print('▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒')
            print('작성자 : ', writer)
            print('내용 : ', cont)
            print('평점 : ', star_score)
            print('작성일자 : ', reg_date)
            count += 1
        print('>>>>>>>>>>>>>>', page, '페이지 수집함')
        page += 1
    print('수집한 게시글 수는 {}건입니다.'.format(count))


# 실행부
crawler('127878')
