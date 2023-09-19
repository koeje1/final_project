import random

# 초기 금액 설정
initial_coin = 1000
coin = initial_coin

# 각 팀의 배당률 설정
allo_team_A = 2.0 # A 팀 배당률
allo_team_B = 1.5 # B 팀 배당률
allo_team_T = 1.0 # 무승부 배당률

while True:
    print(f"현재 잔액: {coin}코인")
    # 배팅할 팀 선택
    team_choice = input("배팅할 팀을 선택하세요. (A, B, T(무승부) ): ")
    if team_choice not in ["A", "B", "T"]:
        continue

    # 배팅 금액 입력
    bet_amount = int(input("배팅할 코인을 입력하세요 (한 번에 걸수 있는 최대 코인 10000): "))

    if bet_amount > coin:
        print("현재 코인 보다 많은 코인을 입력할 수 없습니다.")
        continue
    if bet_amount > 10000:
        print("한번에 1000코인 이상 입력할 수 없습니다.")
        continue
    # 사용자에게 정말로 게임을 종료할 것인지 묻기
    choice = input("정말로 배팅하시겠습니까? (Y,N): ")
    if choice == "N":
        continue
    # 승패 결정(임시용)
    winning_team = random.choice(["A", "B", "T"])

    # 베팅 결과 계산
    if team_choice == winning_team:
        if team_choice == "A":
            winnings = bet_amount * allo_team_A + bet_amount
        elif team_choice == "B":
            winnings = bet_amount * allo_team_B + bet_amount
        else:
            winnings = bet_amount * allo_team_T + bet_amount
        coin += winnings - bet_amount
        if winning_team == "T":
            print("무승부 입니다 배팅에 성공하셨습니다")
        else:
            print(f"{winning_team}팀이 이겼습니다. 배팅에 성공하셨습니다")
        print(f"베팅에 대한 수익: {winnings - bet_amount}원")
    else:
        if winning_team == "T":
            print("무승부 입니다. 배팅에 실패하셨습니다.")
        else:
            print(f"{winning_team}가 이겼습니다. 배팅에 실패하셨습니다.")
        coin -= bet_amount

    if coin <= 0:
        print("배팅금액이 부족합니다 충전 후 이용바랍니다.")
        break


