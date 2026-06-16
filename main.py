# AI 활용 자유 주제 파이썬 미니 프로젝트
# 이름 또는 학번: 
# 프로젝트 주제: 

import random

# ==========================================
# 1. 게임 데이터 및 환경 설정
# ==========================================
# 컴퓨터가 숨겨놓은 진짜 땅 속성 (F:불, W:물, G:흙)
hidden_map = [
    ['F', 'W', 'G'],
    ['G', 'F', 'W'],
    ['W', 'G', 'F']
]

# 플레이어가 보게 될 화면 ([❓]는 아직 땅 속성을 모르는 빈 칸)
game_map = [
    ['[❓]', '[❓]', '[❓]'],
    ['[❓]', '[❓]', '[❓]'],
    ['[❓]', '[❓]', '[❓]']
]

gold = 0
properties_info = {'F': '🔥불', 'W': '💧물', 'G': '🌱흙'}

print("==================================================")
print(" 🐉 드래곤 아일랜드 : 배치와 이주 경영 시뮬레이션🐉")
print("==================================================")
player_name = input("▶️ 매니저님의 이름을 알려주세요: ")

print("==================================================")
print("              🎮 게임 규칙 안내 🎮")
print("==================================================")
print("동일한 속성의 서식지에 드래곤을 매칭하는 전략 퍼즐 게임입니다.\n")
print("1. ⏳ 게임은 총 10턴 동안 진행됩니다.")
print("2. 📦 매 턴 시작 시 [드래곤 알 1개]와 [이동권 1개]가 지급됩니다.")
print("3. 🎮 매 턴 플레이어는 다음 2가지 행동 중 하나를 선택합니다:")
print("   • 선택 1 [알 배치] : 빈 칸(❓)에 알을 심습니다. (다음 턴에 무작위 부화)")
print("   • 선택 2 [드래곤 이동] : 이미 부화한 드래곤을 다른 칸으로 이사시킵니다. (🚚 짜장면 값 50 Gold 소모!)")
print("4. 💰 턴 종료 시 배치된 드래곤들의 환경에 따라 골드를 획득합니다:")
print("   • 🔥속성 일치 (예: 불 지형 + 불 드래곤) ➡️ 매 턴 +50 Gold")
print("   • 💧속성 불일치 (예: 물 지형 + 흙 드래곤) ➡️ 매 턴 +10 Gold")
print("5. 🏆 10턴 종료 후, 누적된 최종 자산에 따라 등급(S/A/B)이 매겨집니다!\n")
print("최고의 효율을 찾아 섬을 멋지게 개척해 보세요!")


# ==========================================
# 2. 10턴 동안 게임 진행
# ==========================================
for turn in range(1, 11):
    print("\n" * 2)
    print("=" * 50)
    print(f"🏰 [TURN {turn}/10] 매니저: {player_name}")
    print(f"💰 현재 자산: {gold} Gold")
    print("🎁 [보급 완료] 이번 턴에 사용할 알 1개와 이동권 1개가 지급되었습니다.")
    print("=" * 50)
    
    print("  0   1   2  (열)")
    for i in range(3):
        print(f"{i} {game_map[i][0]} {game_map[i][1]} {game_map[i][2]}")
    print("-" * 50)
    
    while True:
        print("🎮 이번 턴에 어떤 행동을 하시겠습니까?")
        print("1. [알 배치]")
        print("2. [드래곤 이동]")
        choice = input("▶️ 행동 선택 (1 또는 2): ")
        
        action_success = False 
        
        # --------------------------------------
        # 선택지 1: 알 배치하기
        # --------------------------------------
        if choice == '1':
            print("\n🥚 알을 배치할 좌표를 입력하세요.")
            row = int(input("행 번호(0~2): "))
            col = int(input("열 번호(0~2): "))
            
            if 0 <= row <= 2 and 0 <= col <= 2:
                if game_map[row][col] == '[❓]' or '[．]' in game_map[row][col]:
                    game_map[row][col] = '[🥚]'
                    print(f"✨ ({row}, {col}) 칸에 알을 두었습니다!")
                    action_success = True
                else:
                    print("❌ 이미 다른 대상이 있는 칸입니다!")
            else:
                print("❌ 올바른 좌표 범위(0~2)가 아닙니다!")
                
        # --------------------------------------
        # 선택지 2: 드래곤 이동권 사용하기 (짜장면 이벤트 추가)
        # --------------------------------------
        elif choice == '2':
            print("\n📦 드래곤 용달트럭을 불러 이사합니다.")
            print("[1] 이사할 드래곤이 있는 칸을 고르세요.")
            s_row = int(input("출발 행(0~2): "))
            s_col = int(input("출발 열(0~2): "))
            
            print("[2] 드래곤을 보낼 목적지 칸을 고르세요.")
            e_row = int(input("목적 행(0~2): "))
            e_col = int(input("목적 열(0~2): "))
            
            if (0 <= s_row <= 2 and 0 <= s_col <= 2) and (0 <= e_row <= 2 and 0 <= e_col <= 2):
                if '🐉' in game_map[s_row][s_col] and '[🥚]' not in game_map[e_row][e_col]:
                    
                    start_cell = game_map[s_row][s_col] 
                    start_land_emoji = start_cell[1]   
                    
                    target_land_type = hidden_map[e_row][e_col]
                    target_land_emoji = properties_info[target_land_type][0] 
                    
                    target_cell_backup = game_map[e_row][e_col]
                    
                    game_map[e_row][e_col] = start_cell.replace(start_land_emoji, target_land_emoji, 1)
                    game_map[s_row][s_col] = f"[{start_land_emoji}|．]"
                    
                    if '🐉' in target_cell_backup:
                        old_target_land = target_cell_backup[1]
                        game_map[s_row][s_col] = target_cell_backup.replace(old_target_land, start_land_emoji, 1)
                        print("🔄 두 드래곤은 합의 후 집을 바꿨습니다.")
                        
                    print(f"✨ 드래곤이 성공적으로 이주했습니다! 목적지 지형({target_land_emoji}) 오픈!")
                    
                    # 🛠️ [짜장면 값 차감 로직 추가]
                    print("🍜 이사가 끝나서 모두에게 짜장면을 샀습니다.")
                    if gold >= 50:
                        gold -= 50
                        print("💸 자산이 50 Gold 차감되었습니다.")
                    else:
                        print(f"💸 자산이 부족하여 가진 돈 전액({gold} Gold)이 차감되었습니다. 다행히도 보증인을 자처한 드래곤이 있어 빚은 면했습니다. ")
                        gold = 0
                        
                    action_success = True
                else:
                    print("❌ 출발지에 드래곤이 없거나 목적지가 올바르지 않습니다!")
            else:
                print("❌ 올바른 좌표 범위(0~2)가 아닙니다!")
        else:
            print("❌ 잘못된 번호입니다.")
            
        if action_success:
            break

    # [2] ENTER 키로 턴 종료 및 자동 부화/정산 진행
    print("\n⏳ 행동 완료! [ENTER]로 부화 및 정산이 진행됩니다...")
    input()
    
    # 알 부화 처리
    for i in range(3):
        for j in range(3):
            if game_map[i][j] == '[🥚]':
                land_type = hidden_map[i][j]
                land_emoji = properties_info[land_type][0]
                dragon_type = random.choice(['F', 'W', 'G'])
                dragon_emoji = properties_info[dragon_type][0] + "🐉"
                
                game_map[i][j] = f"[{land_emoji}|{dragon_emoji}]"
                print(f"🎉 드래곤 부화 완료! ({i},{j})에 {properties_info[dragon_type]} 드래곤이 깨어났습니다! (지형: {properties_info[land_type]})")

    # 수입 정산 및 출처 순서대로 누적하기
    turn_income = 0
    income_sources = []  # 출처를 순서대로 담을 리스트
    
    for i in range(3):
        for j in range(3):
            cell = game_map[i][j]
            if '🐉' in cell:
                if cell[1] == cell[-3]: 
                    turn_income += 50
                    income_sources.append("+50") # 일치 출처 추가
                else:
                    turn_income += 10
                    income_sources.append("+10") # 불일치 출처 추가
                    
    gold += turn_income
    
    # 정산 결과 및 출처 흐름 출력
    print(f"🔍 수입 상세 내역 (지도 순서): {' ➡️ '.join(income_sources) if income_sources else '생산중인 드래곤 없음'}")
    print(f"💰 이번 턴 수입: +{turn_income} Gold (누적 자산: {gold} Gold)")
    input("\n⌨️ [ENTER]를 누르면 다음 턴으로 반복 진행합니다...")

# ==========================================
# 3. Game Over 및 최종 결과 등급 평가
# ==========================================
print("\n" * 3)
print("==================================================")
print(" 🎉 GAME OVER! 모든 개척 턴이 종료되었습니다. 🎉")
print("==================================================")
print(f" 매니저 성함: {player_name} | 최종 획득 자산: 💰 {gold} Gold")

if gold >= 400:
    grade = "🏆 S등급 (전무후무 최고의 섬 관리인)"
elif gold >= 200:
    grade = "🥇 A등급 (안빈낙도 관리인)"
else:
    grade = "🥈 B등급 (열정페이 관리인)"

print(f" 최종 경영 등급: {grade}")
print("==================================================")