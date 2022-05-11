from bs4 import BeautifulSoup
import requests

url = "https://movie.naver.com/movie/bi/mi/basic.naver?code=38444"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

review_number = int(input('보고싶은 리뷰의 개수를 작성하세요: '))

ko_title = soup.select_one('h3.h_movie > a').get_text()  # 영화 title
en_title = soup.select_one('strong.h_movie2').text.strip().replace('\t','').replace('\r','').replace('\n','')
print(ko_title, en_title)
print('\n')

score1 = soup.select_one('span.st_off').text
print(score1, end = ', ') # 영화 평점
print('\n')

summary = soup.select_one('p.con_tx').text
print("줄거리: ", summary)
print('\n')

# 영화 리뷰
reviews = soup.findAll('div', 'score_reple')

# print('리뷰1: ', reviews[0].p.get_text().strip())
# print('\n')
# print('리뷰2: ', reviews[1].p.get_text().strip())
# print('\n')
# print('리뷰3: ', reviews[2].p.get_text().strip())
# print('\n')
# print("리뷰4: ", reviews[3].p.get_text().strip())
# print("\n")
# print("리뷰5:", reviews[4].p.get_text().strip())

for i in range(review_number):
    print('리뷰', i+1, ':', reviews[i].p.get_text().strip(), end = '\n\n') # 페이지에 리뷰가 5개 작성되어있으므로 6 이상의 수를 출력하면 error가 나온다.
