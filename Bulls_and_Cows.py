# 숫자 야구 게임을 만들어본다.
# 함수로 묶어 모듈화한다.


# 게임 설계
# 1. 랜덤한 숫자 배열 4개를 컴퓨터가 생성한다.
# 2. 플레이어는 배열 4개를 맞춰야 한다.

# %랜덤하게 생성되는 수에 중복은 없다.%

# 컴퓨터가 5893을 생성하였을 때 플레이어가 1234를 입력하면
# X X B X

# 플레이어가 5763을 입력하면
# S X X S

# 범례 : X 아웃 B 볼 S 스트라이크

from random import randint

# 랜덤하게 4개의 숫자를 리스트로 주는 함수
def rand_nums_gen():
    right_nums = []
    i = 0

    while i < 4:
        new_num = randint(0,9)
        if new_num not in right_nums:
            right_nums.append(new_num)
            i += 1
    return right_nums

# 플레이어에게 정수 입력 받는 함수
def player_nums():
    while True:
        player_nums = list(input("4자리 숫자 입력 : "))
        
        if len(player_nums) != 4 or len(set(player_nums)) != 4:
            print("4자리의 중복되지 않은 숫자를 입력해주세요\n")
            continue
        try:
            player_nums = [int(i) for i in player_nums]
            break
        except ValueError:
            print("입력 받은 수는 정수가 아닙니다.\n")
    
    return player_nums

# 리스트 비교하여 확인
def validate(right_nums, player_nums):
    result = ['X'] * 4

    for i in range(4):
        if player_nums[i] == right_nums[i]:
            result[i] = 'S'
        elif player_nums[i] in right_nums:
            result[i] = 'B'
    return result

com = rand_nums_gen()
tries = 1
print("""======= 숫자 야구 게임 시작 =======
임의의 4 자리 숫자를 입력해주세요.
X는 아웃, B는 볼, S는 스트라이크입니다.

X : 해당 숫자가 리스트에 없음
B : 리스트에 있으나 자리가 맞지 않음
S : 정확한 자리와 숫자
""")

while True:
    user_nums = player_nums()
    results = validate(com, user_nums)
    print(results, '\n')

    if results == ['S', 'S', 'S', 'S']:
        break
    else:
        tries += 1

print(f"정답입니다! {tries}번 만에 맞추셨습니다.")