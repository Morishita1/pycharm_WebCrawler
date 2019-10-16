import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import MongoDAO as DAO


class UReview:

    def __init__(self):
        self.mDao = DAO.MongoDAO('userreview')

    def u_crawler(self, game_url, game_code):
        url = 'https://www.metacritic.com{}/user-reviews'.format(game_url)
        # 사이트에서 비정상적인 request를 요청하면 403에러가 뜨는걸 우회하는 방법 : url + header 값을 가져와서 넣어주면 해결
        headers = {'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
        resp = requests.get(url, headers=headers)
        soup = BeautifulSoup(resp.text, 'html.parser')

        user_list = soup.select('div.review_top_l')
        print(len(user_list))
        for user in user_list[:-3]:
            u_score = user.select('div.metascore_w')[0].text
            u_name = user.select('div.name > a')[0].text
            u_review = user.select('div.review_body')[0].text.strip()
            data = {'game_code': game_code, 'u_score': u_score, 'u_name': u_name, 'u_review': u_review}
            self.mDao.mongo_write(data)
            print(u_score)
            print(u_name)
            print(u_review)
            print('====================================')
