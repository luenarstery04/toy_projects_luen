# (1) 우선 main이 하는 일을 생각해보자. 파이썬은 해당 파일을 직접 실행했을 때 "__main__"이라면
# 하단의 코드를 실행시키도록 한다.
# 따라서 main() 함수를 만들어놓고 이곳에서 실행시킬 class들을 정의해준다.
from presentation.Menu import *
from service.Coffee import Coffee
from service.Sales import Sales

def main():
    drinks = [
        Coffee("HOT 아메리카노", 10, 0, 4, 2000, 3000),
        Coffee("ICE 아메리카노", 10, 0, 4, 2000, 3000),
        Coffee("카푸치노", 10, 0, 3, 3000, 4000),
        Coffee("헤이즐넛", 10, 0, 3, 3500, 4200)
    ]

    # 메뉴를 호출하면서 메인메뉴로 판매, 음료 배열을 같이 보낸다.
    Menu(Sales(), drinks).main_menu()

if __name__ == "__main__":
    main()