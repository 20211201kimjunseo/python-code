# 키 딕셔너리를 사용하여 캐릭터에 넣기
key_list = ["name", "hp", "mp", "level"]
value_list = ["기사", "200", "30", "5"]
character = {}
for i in range(0, len(key_list)):
    character[key_list[i]] = value_list[i]
print(character)

# 리미트를 주어주고 while 반복문으로 값 찾기
limit = 10000
i = 1
sum_value = 0
while sum_value < limit:
    sum_value += i
    i += 1
print("{}를 더할 때 {}을 넘으며 그때의 값은 {}입니다.".format(i-1, limit, sum_value))

# 반복문 사용해서 최댓값을 계속 갱신하면서 찾기
max_value = 0
a = 0
b = 0
for i in range(1, 100 // 2 + 1):
    j = 100 - i
    current = i * j
    if max_value < current:
        a = i
        b = j
        max_value = current
print("최대가 되는 경우 : {} * {} = {}".format(a, b, max_value))

# 리버스 사용
numbers = [1, 2, 3, 4, 5, 6]
r_num = reversed(numbers)

print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(list(r_num))