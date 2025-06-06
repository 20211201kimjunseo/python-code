# 383p 예외객체
try:
    number_input_a = int(input("정수 입력>"))
    print("원의 반지름:", number_input_a)
    print("원의 둘레:", 2 * 3.14 * number_input_a)
    print("원의 넓이:", 3.14 * number_input_a * number_input_a)
except Exception as exception:
    print("type(exception):", type(exception))
    print("exception:", exception)

# 384p 여러 가지 예외가 발생할 수 있는 코드
list_number = [52, 273, 32, 72, 100]

try:
    number_input = int(input("정수 입력>"))
    print("{}번째 요소: {}".format(number_input, list_number[number_input]))
except Exception as exception:
    print("type(exception):", type(exception))
    print("exception:", exception)

# 386p 예외 구분하기
list_number = [52, 273, 32, 72, 100]

try:
    number_input = int(input("정수 입력> "))
    print("{}번째 요소: {}".format(number_input, list_number[number_input]))
except ValueError:
    print("정수를 입력해 주세요!")
except IndexError:
    print("리스트의 인덱스를 벗어났어요!")

# 387p 예외 구문과 예외 객체
list_number = [52, 273, 32, 72, 100]

try:
    number_input = int(input("정수 입력>"))
    print("{}번째 요소: {}".format(number_input, list_number[number_input]))
except ValueError as exception:
    print("정수를 입력해 주세요!")
    print("exception:", exception)
except IndexError as exception:
    print("리스트의 인덱스를 벗어났어요!")
    print("exception:", exception)

# 388p 예외 처리를 했지만 예외를 못 잡는 경우
list_number = [52, 273, 32, 72, 100]

try:
    number_input = int(input("정수 입력>"))
    print("{}번째 요소: {}".format(number_input, list_number[number_input]))
    예외_발생해주세요  # 이 부분은 실제 예외를 발생시키기 위한 코드로 의도한 것이라면 정의되지 않은 이름으로 NameError가 발생합니다.
except ValueError as exception:
    print("정수를 입력해 주세요!")
    print(type(exception), exception)
except IndexError as exception:
    print("리스트의 인덱스를 벗어났어요!")
    print(type(exception), exception)

# 389p 모든 예외 잡기
list_number = [52, 273, 32, 72, 100]

try:
    number_input = int(input("정수 입력> "))
    print("{}번째 요소: {}".format(number_input, list_number[number_input]))
    예외_발생해주세요()  # 정의되지 않은 함수 호출로 예외 발생
except ValueError as exception:
    print("정수를 입력해 주세요!")
    print(type(exception), exception)
except IndexError as exception:
    print("리스트의 인덱스를 벗어났어요!")
    print(type(exception), exception)
except Exception as exception:
    print("기타 예외가 발생했어요!")
    print(type(exception), exception)
