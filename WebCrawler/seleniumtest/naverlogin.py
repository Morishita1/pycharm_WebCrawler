from selenium import webdriver

path = 'E:\Bigdata\webdriver\chromedriver.exe'
drivber = webdriver.Chrome(path)
drivber.get('https://nid.naver.com/nidlogin.login')
drivber.implicitly_wait(3)

drivber.find_element_by_id('id').send_keys('iakwpi')
drivber.find_element_by_id('pw').send_keys('iakwpi')

drivber.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()

# 자동 로그인 방지 및 봇 판별 => 캡차(capcha) 프로그램
# 캡차 프로그램
# 1. 클립보드에 id, pw값을 복사했다가 붙여넣기하면 해결
# 2. script의 input태그 value값으로 값을 입력
# 3. win32api?를 이용하는 방법(완성도가 떨어짐)