# 318p 리스트와 튜플의 특이한 사용
[a, b] = [10, 20]
(c, d) = (10, 20)
print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)

# 319p 괄호가 없는 튜플
tuple_test = 10, 20, 30, 40
print("# 괄호가 없는 튜플의 값과 자료형 출력")
print("tuple_test", tuple_test)
print("type(tuple_test):", type(tuple_test))
print()
a, b, c = 10, 20, 30
print("# 괄호가 없는 튜플을 활용한 할당")
print("a:", a)
print("b:", b)
print("c:", c)

# 320p 변수의 값을 교환하는 튜플
a, b = 10, 20
print("# 교환 전 값")
print("a:", a)
print("b:", b)
print()
a, b = b, a
print("# 교환 후 값")
print("a:", a)
print("b:", b)
print()

# 320p 여러 개의 값 리턴하기
def test():
    return (10, 20)
a, b = test()
print("a:", a)
print("b:", b)

# 322p 함수의 매개변수로 함수 전달하기
def call_10_time(func):
    for i in range(10):
        func()
def print_hello():
    print("안녕하세요")
call_10_time(print_hello)

# 323p map() 함수와 filter() 함수
def power(item):
    return item *item
def under_3(item):
    return item < 3
list_input_a = [1, 2, 3, 4, 5]
output_a = map(power, list_input_a)
print("# map() 함수의 실행 결과")
print("map(power, list_input_a):", output_a)
print("map(power, list_input_a):", list(output_a))
print()
output_b = filter(under_3, list_input_a)
print("# filter() 함수의 실행 결과")
print("filter(under_3, list_input_a):", output_b)
print("filter(under_3, list_input_a):", list(output_b))

# 325p 람다
power = lambda x: x * x
under_3 = lambda x: x < 3
list_input_a = [1, 2, 3, 4, 5]
output_a = map(power, list_input_a)
print("# map() 함수의 실행 결과")
print("map(power, list_input_a):", output_a)
print("map(power, list_input_a):", list(output_a))
print()
output_b = filter(under_3, list_input_a)
print("# filter() 함수의 실행 결과")
print("filter(under_3, list_input_a):", output_b)
print("filter(under_3, list_input_a):", list(output_b))

# 326p 인라인 람다
list_input_a = [1, 2, 3, 4, 5]
output_a = map(lambda x: x * x, list_input_a)
print("# map() 함수의 실행 결과")
print("map(power, list_input_a):", output_a)
print("map(power, list_input_a):", list(output_a))
print()
output_b = filter(lambda x: x < 3, list_input_a)
print("# filter() 함수의 실행 결과")
print("filter(under_3, list_input_a):", output_b)
print("filter(under_3, list_input_a):", list(output_b))

# 327p 파일 열고 닫기
file = open("basic.txt", "w")
file.write("Hello Python Programming...!")
file.close()

# 330p read() 함수로 텍스트 읽기
with open("basic.txt", "r") as file:
    contents = file.read()
print(contents)

# 331p 랜덤하게 1000명의 키와 몸무게 만들기
import random
hanguls = list("가나다라마바사아자차카타파하")
with open("info.txt", "w") as file:
    for i in range(1000):
        name = random.choice(hanguls) + random.choice(hanguls)
        weight = random.randrange(40, 100)
        height = random.randrange(140, 200)
        file.write("{}, {}, {}\n".format(name, weight, height))

# 332p 반복문으로 파일 한 줄씩 읽기
with open("info.txt", "r") as file:
    for line in file:
        (name, weight, height) = line.strip().split(", ")
        if (not name) or (not weight) or (not height):
            continue
        bmi = int(weight) / ((int(height) / 100) ** 2)
        result = ""
        if 25 <= bmi:
            result = "과체중"
        elif 18.5 <= bmi:
            result = "정상체중"
        else:
            result = "저체중"
        print('\n'.join([
            "이름: {}",
            "몸무게: {}",
            "키: {}",
            "BMI: {}",
            "결과: {}",   
        ]).fomat(name, weight, height, bmi, result))
        print()

# 336p 제너레이터 함수
def test():
    print("함수가 호출되었습니다.")
    yield "test"
print("A 지점 통과")
test()
print("B 지점 통과")
test()
print(test())

# 337p 제너레이터 객체와 next() 함수
def test():
    print("A 지점 통과")
    yield 1
    print("B 지점 통과")
    yield 2
    print("C 지점 통과")
output = test()
print("D 지점 통과")
a = next(output)
print(a)
print("E 지점 통과")
b = next(output)
print(b)
print("F 지점 통과")
c = next(output)
print(c)
next(output)

# 339p 키워드 매개변수에 함수 전달하기
books = [{
    "제목": "혼자 공부하는 파이썬",
    "가격": 18000
}, {
    "제목": "혼자 공부하는 머신러닝 + 딥러닝",
    "가격": 26000
}, {
    "제목": "혼자 공부하는 자바스크립트",
    "가격": 24000
}]
def 가격추출함수(book):
    return book["가격"]
print("# 가장 저렴한 책")
print(min(books, key=가격추출함수))
print()
print("# 가장 비싼 책")
print(max(books, key=가격추출함수))

# 340p 콜백 함수를 람다로 바꾸기
books = [{
    "제목": "혼자 공부하는 파이썬",
    "가격": 18000
}, {
    "제목": "혼자 공부하는 머신러닝 + 딥러닝",
    "가격": 26000
}, {
    "제목": "혼자 공부하는 자바스크립트",
    "가격": 24000
}]
print("# 가장 저렴한 책")
print(min(books, key=lambda book: book["가격"]))
print()
print("# 가장 비싼 책")
print(max(books, key=lambda book: book["가격"]))

# 341p 딕셔너리 오름차순 정렬하기
books = [{
    "제목": "혼자 공부하는 파이썬",
    "가격": 18000
}, {
    "제목": "혼자 공부하는 머신러닝 + 딥러닝",
    "가격": 26000
}, {
    "제목": "혼자 공부하는 자바스크립트",
    "가격": 24000
}]
print("# 가격 오름차순 정렬")
books.sort(key=lambda book: book["가격"])
for book in books:
    print(book)
