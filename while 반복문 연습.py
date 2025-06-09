###
def print_a(n, *values):
    for i in range(n):
        for value in values:
            print(value)
print_a(3, "안녕", "하세", "요")

###
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(0))

#피라미드
output = ""

for i in range(1, 15):
    for j in range(14, i, -1):
        output += " "
    for k in range(0, 2 * i - 1):
        output += "*"
    output += "\n"
print(output)

# 무한 반복 while문을 사용함 문장을 계속 반복함 ctrl + c로 강제 종료
while True:
    print("*")
    break

# while문으로 반복
i = 0
while i < 10:
    print("{}번째 반복입니다.".format(i))
    i += 1

 # import time으로 시간 모듈을 가져와 2초동안 반복
import time
number = 0
time_a = time.time() + 2
while time.time() < time_a:
    number += 1
print("2초동안 {}번 반복함.".format(number))

#  반복을 멈출지 말지 정할 수 있음
i = 0
while True:
    print("{}번째 반복입니다.".format(i))
    i += 1
    input_a = input("종료할래?[y/n] : ")
    list_a = ["y", "Y"]
    if input_a in list_a:
        print("종료하였다.")
        break

# continue로 125보다 작을 시 다음 반복으로 넘어감
numbers = [515, 124, 122, 121, 344]

for number in numbers:
    if number < 125:
        continue
    print(number)

# while 반복문을 사용하여 7을 넘을 때
limit = 7
i = 1
sum_value = 0
while sum_value < limit:
    sum_value += i
    i += 1
print("{}을 더할 때 {}을 넘으며 그때의 값은 {}이다.".format(i-1, limit, sum_value))
# 0 + 1 = 1
# 1 + 2 = 3
# 3 + 3 = 6
# 6 + 4 = 10

# enumerate 사용
a = ["요소A", "요소B", "요소C"]

# for i in range(len(a)):
#     print("{}번째 요소는 {}입니다.".format(i, a[i]))

for i, value in enumerate(a):
    print("{}번째 요소는 {}입니다.".format(i, value))

