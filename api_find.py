from bs4 import BeautifulSoup
import requests

url = "https://movie.naver.com/movie/bi/mi/basic.naver?code=38444"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

review_number = int(input('보고싶은 리뷰의 개수를 작성하세요: '))

titles = soup.findAll('h3', 'h_movie', './basic.naver?code=38444') # 영화 title
title = titles[0].text.replace(',', '').replace('2016', '').replace("\n", "") # 연도는 바꿔줘야 함...ㅠㅠ
print(title)

print('\n')
score = soup.findAll('span', 'st_on')[0].text
a, b, score = score.split(" ")
print('관람객 평점: ', score) # 영화 평점
print('\n')

summary = list(soup.findAll('p', 'con_tx'))
print("줄거리: ", summary[0].text)
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