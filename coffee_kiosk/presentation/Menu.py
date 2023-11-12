# 메뉴를 짠다. 커피 판매, 판매 현황, 종료 세 기능이 있다.
class Menu:
    def __init__(self, sales, drinks):
        self.sales = sales
        self.drinks = drinks

    def main_menu(self):
        while True:
            print("\n========Menu========")
            print("(1) 커피 판매")
            print("(2) 판매 현황")
            print("(3) 프로그램 종료")
            input_menu = int(input("입력 : "))

            if input_menu == 1:
                self.coffee_menu()
            elif input_menu == 2:
                self.statistics()
            elif input_menu == 3:
                print("* 프로그램 종료 *")
                return
            else:
                print("* 잘못된 번호입니다. 다시 입력해주세요. *")

    def coffee_menu(self):
        print("\n========List========")
    
    def statistics(self):
        print("\n========statistics========")

    