# 365p 조건문으로 예외 처리하기
user_input_a = input("정수 입력> ")
if user_input_a.isdigit():
    number_input_a = int(user_input_a)
    pirnt("원의 반지름:", number_input_a)
    print("원의 둘레:", 2 * 3.14 * number_input_a)
    print("원의 넓이:", 3.14 * number_input_a * number_input_a)
else:
    print("정수를 입력하지 않았습니다.")

# 367p try except 구문
try:
    number_input_a = int(input("정수 입력> "))
    pirnt("원의 반지름:", number_input_a)
    print("원의 둘레:", 2 * 3.14 * number_input_a)
    print("원의 넓이:", 3.14 * number_input_a * number_input_a)
except:
    print("무언가 잘못되었습니다.")

# 368p 숫자로 변환되는 것들만 리스트에 넣기
list_input_a = ["52", "273", "32", "스파이", "103"]
list_number = []
for item in list_input_a:
    try:
        float(item)
        list_number.append(item)
    except:
        pass
print("{} 내부에 있는 숫자는".format(list_input_a))
print("{}입니다.".format(list_number))

# 369p try except else 구문
try:
    number_input_a = int(input("정수 입력> "))
except:
    print("정수를 입력하지 않았습니다.")
else:
    pirnt("원의 반지름:", number_input_a)
    print("원의 둘레:", 2 * 3.14 * number_input_a)
    print("원의 넓이:", 3.14 * number_input_a * number_input_a)

# 371p finally 구문
try:
    number_input_a = int(input("정수 입력> "))
    pirnt("원의 반지름:", number_input_a)
    print("원의 둘레:", 2 * 3.14 * number_input_a)
    print("원의 넓이:", 3.14 * number_input_a * number_input_a)
except:
    print("정수를 입력하지 않았습니다.")
else:
    print("예외가 발생하지 않았습니다.")
finally:
    print("일단 프로그램이 어떻게든 끝났습니다.")

# 373p 파일이 제대로 닫혔는지 확인하기
try:
    file = open("info.txt", "w")
    file.close()
except:
    print("오류가 발생했습니다.")
print("# 파일이 제대로 닫혔는지 확인하기")
print("file.closed:", file.closed)

# 374p 파일 처리 중간에 예외 발생
try:
    file = open("info.txt", "w")
    예외.발생해라()
    file.close()
except:
    print("오류가 발생했습니다.")
print("# 파일이 제대로 닫혔는지 확인하기")
print("file.closed:", file.closed)

# 373p finally 구문 사용해 파일 닫기
try:
    file = open("info.txt", "w")
    예외.발생해라()
except:
    print("오류가 발생했습니다.")
finally:
    file.close()
print("# 파일이 제대로 닫혔는지 확인하기")
print("file.closed:", file.closed)

# 375p try except 구문 끝난 후 파일 닫기
try:
    file = open("info.txt", "w")
    예외.발생해라()
except:
    print("오류가 발생했습니다.")
file.close()
print("# 파일이 제대로 닫혔는지 확인하기")
print("file.closed:", file.closed)

# 376p try 구문 내부에서 return 키워드를 사용하는 경우
def test():
    print("test() 함수의 첫 줄입니다.")
    try:
        print("try 구문이 실행되었습니다.")
        return
        print("try 구문이 return 키워드 뒤입니다.")
    except:
        print("except 구문이 실행되었습니다.")
    else:
        print("else 구문이 실행되었습니다.")
    finally:
        print("finally 구문이 실행되었습니다.")
    print("test() 함수의 마지막 줄입니다.")
test()

# 377p finally 키워드 활용
def write_text_file(filename, texe):
    try:
        file = open(filename, "w")
        return
        file.write(text)
    except:
        print("오류가 발생했습니다.")
    finally:
        file.close()
write_text_file("text.txt", "안녕하세요!")

# 378p 반복문과 함께 사용하는 경우
print("프로그램이 시작되었습니다.")
while True:
    try:
        print("try 구문이 실행되었습니다.")
        break
        print("try 구문이 break 키워드 뒤입니다.")
    except:
        print("except 구문이 실행되었습니다.")
    finally:
        print("finally 구문이 실행되었습니다.")
    print("while 반복문의 마지막 줄입니다.")
print("프로그램이 종료되었습니다.")