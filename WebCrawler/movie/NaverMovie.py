import requests
from bs4 import BeautifulSoup
page = 1 # 페이지 넘버
count = 0 # 댓글 총 갯수
compare_reple = '' # 마지막페이지를 찾기위한 댓글정보
while True:
    url ='https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=182205&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page={}'.format(page)

    doc = requests.get(url)
    soup = BeautifulSoup(doc.text, 'html.parser')

    # 1페이지에 존재하는 댓글 10건 List
    reply_list = soup.select('div.score_result > ul > li')

    # 댓글 10건중 첫번째 댓글이 다음 페이지의 첫번째 댓글과
    # 같으면 끝난 페이지임 break로 반복문을 빠져나가라
    print('>>>>>>>>>>>>>>', page, '페이지 수집함')
    flag = reply_list[0].select('div.score_reple span[id^="_filter"]')[0].text
    if compare_reple == flag:
        break
    else:
        compare_reple = flag

    # 댓글 10건씩 꺼내서 reply에 담음

    for reply in reply_list:
        # 작성자, 내용, 평점, 작성일자
        writer = reply.select('div > dl > dt > em > a')[0].text.strip()
        cont = reply.select('div.score_reple span[id^="_filter"]')[0].text
        star_score = reply.select('div.star_score > em')[0].text
        reg_date = reply.select('div > dl > dt > em')[1].text[:10]
        indexNo = writer.find('(')
        writer = writer[:indexNo] # 초롱이(ccw****)의 (~)내용 제거
        print('▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒')
        print('평점 : ', star_score)
        print('댓글 : ', cont)
        print('작성자 : ', writer)
        print('작성일자 : ', reg_date)
        count += 1
    page += 1
print('수집한 게시글 수는 {}건입니다.'.format(count))