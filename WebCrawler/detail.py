import requests
from bs4 import BeautifulSoup
from selenium import webdriver


class ImgCrawler:

    def img_crawler(self, code):

        url = 'https://www.metacritic.com{}'.format(code)
        # 사이트에서 비정상적인 request를 요청하면 403에러가 뜨는걸 우회하는 방법 : url + header 값을 가져와서 넣어주면 해결
        headers = {'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
        resp = requests.get(url, headers=headers)
        soup = BeautifulSoup(resp.text, 'html.parser')
        img = soup.select('img.product_image')[0].get('src')
        # rank_list = soup.select('div.ranking_title')
        # for i in rank_list:
        #     rank = i.select('a')[0].text
        #     print(rank)
        return img
