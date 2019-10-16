from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# selenium driver()의 메서드()
# 1. URL에 접근하는 api
# get('https://python.org)

# 2.page의 단일 element에 접근하는 api
#  - find_element_by_name('HTML_name')
#  - find_element_by_id('HTML_id')
#  - find_element_by_xpath('/html/body/some/xpath')

# 3.page의 여러 element에 접근하는 api
#  - find_element_by_css_selector('#css > div.selector')
#  - find_element_by_class_name('some_class_name')
#  - find_element_by_tag_name('h1')
# 2, 3번 메서드를 사용시 HTML을 브라우저에서 파싱하기 때문에
# python과 BeautifulSoup를 사용하지 않아도 된다.
# but, selenium built in 함수만 사용하면 불편하기 때문에
# BeautifulSoup 객체를 이용하려면 driver.paghe_source API를
# 사용하여 현재 랜더링 된 페이지의 Elements를 모두 가져올 수있음



# chrome driver가 위치하는 주소
path = 'E:\Bigdata\webdriver\chromedriver.exe'

# chrome webdiver 생성
drivber = webdriver.Chrome(path)

# chrome driver로 접속할 url
drivber.get('https://www.python.org') # 핵심 : https://도 꼭 적을것

# 암묵적으로 웹 자원 로드를 위해 3초까지 기다림
drivber.implicitly_wait(3)

# id가 id-ssearch-field인 태그를 찾아서 search 변수에 담음
search = drivber.find_element_by_id('id-search-field')

# input 값 초기화
search.clear()

# inplut 태그에 'labda'값을 입력
search.send_keys('lambda')

search.send_keys(Keys.Return)