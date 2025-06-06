# 339p 키워드 매개변수에 함수 전달하기
books = [{
    "제목" : "혼자 공부하는 파이썬",
    "가격" : 18000
}, {
    "제목" : "혼자 공부하는 머신러닝 + 딥러닝",
    "가격" : 26000
}, {
    "제목" : "혼자 공부하는 자바스크립트",
    "가격" : 24000
}]

def 가격추출함수(book):
    return book["가격"]

print("# 가장 저렴한 책")
print(min(books, key=가격추출함수))
print()

print("# 가장 비싼 책")
print(max(books, key=가격추출함수))
print()
print()


# 340p 콜백 함수를 람다로 바꾸기
books = [{
    "제목" : "혼자 공부하는 파이썬",
    "가격" : 18000
}, {
    "제목" : "혼자 공부하는 머신러닝 + 딥러닝",
    "가격" : 26000
}, {
    "제목" : "혼자 공부하는 자바스크립트",
    "가격" : 24000
}]


print("# 가장 저렴한 책")
print(min(books, key=lambda book: book["가격"]))
print()

print("# 가장 비싼 책")
print(max(books, key=lambda book: book["가격"]))
print()
print()

# 341p 딕셔너리 오름차순 정렬하기
books = [{
    "제목" : "혼자 공부하는 파이썬",
    "가격" : 18000
}, {
    "제목" : "혼자 공부하는 머신러닝 + 딥러닝",
    "가격" : 26000
}, {
    "제목" : "혼자 공부하는 자바스크립트",
    "가격" : 24000
}]

print("# 가격 오름차순 정렬")
books.sort(key=lambda book: book["가격"])
for book in books:
    print(book)

# 426p beautiful soup 모듈로 날씨 가져오기
from urllib import request
from bs4 import BeautifulSoup

target = request.urlopen("http://www.kma.go.kr/wether/forecast/mid-term-rss3.jsp?stnId=108")

soup = BeautifulSoup(target, "html.parser")

for location in soup.select("location"):
    print("도시:", location.select_one("city").string)
    print("날씨:", location.select_one("wf").string)
    print("최저기온:", location.select_one("tmn").string)
    print("최고기온:", location.select_one("tmx").string)
    print()

# 429p Flask 모듈 사용하기
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello World!</h1"

#431p Beautiful Soup 스크레이핑 실행하기

from flask import Flask
from urllib import request
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/")
def hello():
    target = request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")
    soup = BeautifulSoup(target, "html.parser")

    output = ""
    for location in soup.select("location"):
        output += "<h3>{}</h3>".format(location.select_one("city").string)
        output += "날씨: {}<br/>".format(location.select_one("wf").string)
        output += "최저/최고 기온: {}/{}<br/>".format(
            location.select_one("tmn").string,
            location.select_one("tmx").string
        )
        output += "<hr/>"
    
    return output