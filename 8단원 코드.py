# 461p 객체 만들기
students = [
    { "name" : "윤인성", "korean" : 87, "math" : 98, "english" : 88, "science": 95},
    { "name" : "연하진", "korean" : 82, "math" : 98, "english" : 96, "science": 98},
    { "name" : "구지연", "korean" : 76, "math" : 96, "english" : 94, "science": 90},
    { "name" : "나선주", "korean" : 98, "math" : 92, "english" : 96, "science": 92},
    { "name" : "윤아린", "korean" : 95, "math" : 98, "english" : 98, "science": 98},
    { "name" : "윤명월", "korean" : 64, "math" : 88, "english" : 92, "science": 92},
]
print("이름", "총점", "평균", sep="\t")
for student in students:
    score_sum = student["korean"] + student["math"] +\
        student["english"] + student["science"]
    score_average = score_sum / 4
    print(student["name"], score_sum, score_average, sep="\t")

# 462p 객체를 만드는 함수(1)
def create_student(name, korean, math, english, science):
    return {
        "name" : name,
        "korean" : korean,
        "math" : math,
        "english" : english,
        "science" : science
    }
student = [
    create_student("윤인성", 87, 98, 88, 95),
    create_student("연하진", 82, 98, 96, 98),
    create_student("구지연", 76, 96, 94, 90),
    create_student("나선주", 98, 92, 96, 92),
    create_student("윤아린", 95, 98, 98, 98),
    create_student("윤명월", 64, 88, 92, 92),
]
print("이름", "총점", "평균", sep="\t")
for student in students:
    score_sum = student["korean"] + student["math"] +\
        student["english"] + student["science"]
    score_average = score_sum / 4
    print(student["name"], score_sum, score_average, sep="\t")

# 464p 객체를 처리하는 함수(2)
def create_student(name, korean, math, english, science):
    return {
        "name" : name,
        "korean" : korean,
        "math" : math,
        "english" : english,
        "science" : science
    }
def student_get_sum(student):
    return student["korean"] + student["math"] +\
        student["english"] + student["science"]
def student_get_average(student):
    return student_get_sum(student) / 4
def student_to_string(student):
    return "{}\t{}\t{}".format(
        student["name"],
        student_get_sum(student),
        student_get_average(student))
student = [
    create_student("윤인성", 87, 98, 88, 95),
    create_student("연하진", 82, 98, 96, 98),
    create_student("구지연", 76, 96, 94, 90),
    create_student("나선주", 98, 92, 96, 92),
    create_student("윤아린", 95, 98, 98, 98),
    create_student("윤명월", 64, 88, 92, 92),
]
print("이름", "총점", "평균", sep="\t")
for student in students:
    print(student_to_string(student))

# 469p 클래스 내부에 함수(메소드) 선언하기
class student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
    def get_sum(self):
        return self.korean + self.math +\
        self.english + self.science
    def get_average(self):
        return self.get_sum() / 4
    def to_string(self):
        return "{}\t{}\t{}".format(
            self.name,\
            self.get_sum(),\
            self.get_average())
    student = [
    create_student("윤인성", 87, 98, 88, 95),
    create_student("연하진", 82, 98, 96, 98),
    create_student("구지연", 76, 96, 94, 90),
    create_student("나선주", 98, 92, 96, 92),
    create_student("윤아린", 95, 98, 98, 98),
    create_student("윤명월", 64, 88, 92, 92),
]
print("이름", "총점", "평균", sep="\t")
for student in students:
    print(student.to_string())

# 476 isinstance() 함수 활용
class Student:
    def study(self):
        print("공부를 합니다.")
class Teacher:
    def teach(self):
        print("학생을 가르칩니다.")
classroom = [Student(), Student(), Teacher(), Student(), Student()]
for person in classroom:
    if isinstance(person, Student):
        person.study()
    elif isinstance(person, Teacher):
        person.teach()

# 478p __str__() 함수
class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    def get_sum(self):
        return self.korean + self.math + self.english + self.science

    def get_average(self):
        return self.get_sum() / 4

    def __str__(self):
        return "{}\t{}\t{}".format(
            self.name,
            self.get_sum(),
            self.get_average()
        )

students = [
    Student("윤인성", 87, 98, 88, 95),
    Student("연하진", 92, 98, 96, 98),
    Student("구지연", 76, 96, 94, 90),
    Student("나선주", 98, 92, 96, 92),
    Student("윤아린", 95, 98, 98, 98),
    Student("윤명월", 64, 88, 92, 92)
]

print("이름", "총점", "평균", sep="\t")
for student in students:
    print(str(student))

# 480p 크기비교 함수
class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    def get_sum(self):
        return self.korean + self.math + self.english + self.science

    def get_average(self):
        return self.get_sum() / 4

    def __str__(self):
        return "{}\t{}\t{}".format(
            self.name,
            self.get_sum(),
            self.get_average()
        )

    def __eq__(self, value):
        return self.get_sum() == value.get_sum()

    def __ne__(self, value):
        return self.get_sum() != value.get_sum()

    def __gt__(self, value):
        return self.get_sum() > value.get_sum()

    def __ge__(self, value):
        return self.get_sum() >= value.get_sum()

    def __lt__(self, value):
        return self.get_sum() < value.get_sum()

    def __le__(self, value):
        return self.get_sum() <= value.get_sum()

students = [
    Student("윤인성", 87, 98, 88, 95),
    Student("연하진", 92, 98, 96, 98),
    Student("구지연", 76, 96, 94, 90),
    Student("나선주", 98, 92, 96, 92),
    Student("윤아린", 95, 98, 98, 98),
    Student("윤명월", 64, 88, 92, 92)
]

student_a = Student("윤인성", 87, 98, 88, 95)
student_b = Student("연하진", 92, 98, 96, 98)

print("student_a == student_b =", student_a == student_b)
print("student_a != student_b =", student_a != student_b)
print("student_a > student_b =", student_a > student_b)
print("student_a >= student_b =", student_a >= student_b)
print("student_a < student_b =", student_a < student_b)
print("student_a <= student_b =", student_a <= student_b)

# 484p 클래스 변수
class Student:
    count = 0
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

# 486p 클래스 함수
class Student:
    count = 0
    students = []

    @classmethod
    def print(cls):
        print("--------학생 목록--------")
        print("이름\t총점\t평균")
        for student in cls.students:
            print(str(student))
        print("-------- -------- --------")

    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
        Student.count += 1
        Student.students.append(self)

    def get_sum(self):
        return self.korean + self.math + self.english + self.science

    def get_average(self):
        return self.get_sum() / 4

    def __str__(self):
        return "{}\t{}\t{}".format(self.name, self.get_sum(), self.get_average())


Student("윤인성", 87, 98, 88, 95)
Student("연하진", 92, 98, 96, 98)
Student("구지연", 76, 96, 94, 90)
Student("나선주", 98, 92, 96, 92)
Student("윤아린", 95, 98, 98, 98)
Student("윤명월", 64, 88, 92, 92)
Student("김미화", 82, 86, 98, 88)
Student("김연화", 88, 74, 78, 92)
Student("박아현", 97, 92, 88, 95)
Student("서준서", 45, 52, 72, 78)

Student.print()


# 488p 가비지 컬렉터:변수에 저장하지 않는 경우
class Test:
    def __init__(self, name):
        self.name = name
        print("{} - 생성되었습니다".format(self.name))

    def __del__(self):
        print("{} - 파괴되었습니다".format(self.name))


Test("A")
Test("B")
Test("C")


# 489p 가비지 컬렉터:변수에 저장한 경우
class Test:

    def __init__(self, name):
        self.name = name
        print("{} 생성되었습니다.".format(self.name))

    def __del__(self):
        print("{} - 파괴되었습니다".format(self.name))


a = Test("A")
b = Test("B")
c = Test("C")


# 490p 원의 둘레와 넓이를 구하는 객체 지향 프로그램
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_circumference(self):
        return 2 * math.pi * self.radius

    def get_area(self):
        return math.pi * (self.radius ** 2)

circle = Circle(10)
print("원의 둘레:", circle.get_circumference())
print("원의 넓이:", circle.get_area())


# 491p 프라이빗 변수
import math

class Circle:
    def __init__(self, radius):
        self.__radius = radius

    def get_circumference(self):
        return 2 * math.pi * self.__radius

    def get_area(self):
        return math.pi * (self.__radius ** 2)

circle = Circle(10)
print("#원의 둘레와 넓이를 구합니다.")
print("원의 둘레:", circle.get_circumference())
print("원의 넓이:", circle.get_area())

print("#__radius에 접근합니다.")
print(circle._Circle__radius)


# 492p 게터와 세터
import math

class Circle:
    def __init__(self, radius):
        self.__radius = radius

    def get_circumference(self):
        return 2 * math.pi * self.__radius

    def get_area(self):
        return math.pi * (self.__radius ** 2)

    def get_radius(self):
        return self.__radius

    def set_radius(self, value):
        self.__radius = value

circle = Circle(10)
print("# 원의 둘레와 넓이를 구합니다.")
print("원의 둘레:", circle.get_circumference())
print("원의 넓이:", circle.get_area())

print()

print("#__radius에 접근합니다.")
print(circle.get_radius())

print()

circle.set_radius(2)
print("# 반지름을 변경하고 원의 둘레와 넓이를 구합니다.")
print("원의 둘레:", circle.get_circumference())
print("원의 넓이:", circle.get_area())


# 494p 데코레이터를 사용해 게터와 세터 만들기
import math

class Circle:
    def __init__(self, radius):
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise TypeError("길이는 양의 숫자여야 합니다.")
        self.__radius = value

    def get_circumference(self):
        return 2 * math.pi * self.__radius

    def get_area(self):
        return math.pi * (self.__radius ** 2)


print("# 데코레이터를 사용한 Getter와 Setter")
circle = Circle(10)
print("원래 원의 반지름:", circle.radius)
circle.radius = 2
print("변경된 원의 반지름:", circle.radius)
print()

print("# 강제로 예외를 발생시킵니다.")
circle.radius = -10


# 497p 상속의 활용
class Parent:
    def __init__(self):
        self.value = "테스트"
        print("Parent 클래스의 __init__ 메소드가 호출되었습니다.")

    def test(self):
        print("Parent 클래스의 test() 메소드입니다.")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child 클래스의 __init__ 메소드가 호출되었습니다.")

child = Child()
child.test()
print(child.value)


# 498p 사용자 정의 예외 클래스 만들기
class CustomException(Exception):
    def __init__(self):
        super().__init__()

raise CustomException()


# 498p 자식 클래스로써 부모의 함수 재정의(오버라이드)하기
class CustomException(Exception):
    def __init__(self):
        super().__init__()
        print("#### 내가 만든 오류가 생성되었어요! ####")

    def __str__(self):
        return "오류가 발생했어요"

raise CustomException()


# 499p 자식 클래스로써 부모에 없는 새로운 함수 정의하기
class CustomException(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

    def __str__(self):
        return self.message

    def print(self):
        print("# 오류 정보 #")
        print("메시지:", self.message)
        print("값:", self.value)

try:
    raise CustomException("딱히 이유 없음", 273)
except CustomException as e:
    e.print()
