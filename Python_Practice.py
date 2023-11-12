# 으뜸 파이썬 p44 1.5번
# "Welcome to Python!!"을 5줄에 걸쳐 출력하는 코드를 만들어보자.
def welcome_to_python():
    for _ in range(5):
        print("Welcome to Python!!")

# 1.6번 예제와 같이 출력시킨다.
def introduce():

    name = input("이름을 입력하세요: ")
    univ = input("소속 대학을 입력하세요: ")
    depart = input("학과를 입력하세요: ")
    year = input("학년을 입력하세요: ")

    print("******************************")
    print("안녕하세요~")
    print(f"저는 {name}입니다.")
    print(f"{univ} {depart} {year}학년 입니다.")
    print("******************************")

# 1.7 별을 출력시킨다.
#    *
#   ***
#  *****
# *******
def star_triangle():
    n = 1
    for i in range(4):
        for i in range(4 - n):
            print(' ', end="")
        for j in range(2*n - 1):
            print("*", end="")
        print()
        n += 1
    # 처음에 3칸 띄우고, 그 다음 2칸, 그 다음 1칸 이런 식으로 진행한다.
    # 별도 첫 줄에 1개, 둘째 줄에 3개, 셋째 줄에 5개로 2씩 증가한다

def rev_star_triangle():
    n = 4
    space = 0
    for i in range(4):
        for i in range(space):
            print(' ', end="")
        for j in range(2*n - 1):
            print("*", end="")
        print()
        space += 1
        n -= 1

# 1.11 시속 80km의 속력으로 1시간 30분을 달렸을 때 이동한 거리는?
def total_distance():
    speed = 80
    time = 1.5

    print(speed * time, 'km') # = 120.0 km

# 1.12 2시간 동안 190km를 이동했을 때 평균 속력은?
def avg_speed():
    time = 2
    distance = 190

    print(distance / time, 'km') # = 95.0 km

"""
1.13 태양과 지구의 평균 거리는 149597870 km이다.
빛이 1초에 299792 km를 이동한다 가정할 때 태양에서 출발한 빛이
지구에 도착하는데 걸리는 시간은 몇 초인가?
이 값을 분으로 환산해보아라.
"""
def light():
    sun_to_earth = 149597870
    light_speed = 299792

    result1 = round(sun_to_earth / light_speed, 2)
    result2 = round(result1 / 60, 2)

    print(result1)
    print(result2)

"""
1.14 n 팩토리얼은 n * (n-1) * (n-2) * ... 2 * 1 로 정의한다.
이 정의를 바탕으로 다음 값을 구하여라.
(1) 3! (2) 5! (3) 12! (4) 20!
"""

def factorial(n):
    if n < 0:
        return False
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(20))

# 1.15 100과 200 두 값이 있을 경우 이 값들의 평균값을 출력하는 프로그램 작성
def num_avg(n1, n2):
    return (n1 + n2) / 2

print(num_avg(100, 200))

# 1.16 50과 30 두 값이 있을 경우 사칙연산을 수행하는 프로그램을 작성하시오

class MathCalculator:
    def __init__(self):
        self.n1 = int(input("첫 번째 수 입력 : "))
        self.n2 = int(input("두 번째 수 입력 : "))

        self.math_calculator()

    def math_calculator(self):

        while True:
            cal = input("계산자 선택 (+ - * /) 종료는 e : ")

            if cal == '+':
                print(self.add())
            elif cal == '-':
                print(self.minus())
            elif cal == '*':
                print(self.multiply())
            elif cal == '/':
                print(self.divide())
            elif cal == 'e':
                break
            else:
                print("올바른 계산자를 선택해주십시오")
                print()

    def add(self):
        return self.n1 + self.n2
    
    def minus(self):
        return self.n1 - self.n2
    
    def multiply(self):
        return self.n1 * self.n2
    
    def divide(self):
        return self.n1 / self.n2

