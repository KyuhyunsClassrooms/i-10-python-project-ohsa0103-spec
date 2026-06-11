# AI 활용 자유 주제 파이썬 미니 프로젝트
# 이름 또는 학번: 
# 프로젝트 주제: 

import random

# ==========================================
# [1단계] 데이터 구조 및 초기 변수 설정
# ==========================================

# 1. 컴퓨터가 숨겨놓은 진짜 땅 속성 지도 (정답 맵)
hidden_map = [
    ['F', 'W', 'G'],  # 0번 행 (F:불, W:물, G:흙)
    ['G', 'F', 'W'],  # 1번 행
    ['W', 'G', 'F']   # 2번 행
]

# 2. 플레이어가 게임 중에 보게 될 통합 상태 지도 (출력 맵)
game_map = [
    ['[ ❓ ]', '[ ❓ ]', '[ ❓ ]'],
    ['[ ❓ ]', '[ ❓ ]', '[ ❓ ]'],
    ['[ ❓ ]', '[ ❓ ]', '[ ❓ ]']
]

# 3. 게임 시스템 변수
gold = 500         
move_items = 0     
scan_items = 0     
ITEM_PRICE = 200   
SCAN_PRICE = 100   

print("==================================================")
print("     🐉 드래곤 아일랜드 서식지 매니저에 오신 것을 환영합니다! 🐉")
print("==================================================")
player_name = input(" ▶️  섬을 멋지게 개척해 나갈 매니저님의 이름을 입력해 주세요: ")
print("\n" * 2) 
print(f" 반갑습니다, {player_name} 매니저님! 지금부터 최고의 드래곤 아일랜드를 만들어 주세요.")


# ==========================================
# [2단계] 지도 및 상태 출력 함수 정의
# ==========================================
def display_status(name, turn, current_gold, items, scans, current_map):
    print("\n" * 1) 
    print("=" * 60)
    if turn <= 2:
        print(f" 🔰 [TUTORIAL] 드래곤 아일랜드 가이드 진행 중...")
    else:
        print(f" 🏰 [TURN {turn-2}/10] 드래곤 아일랜드 (매니저: {name})")
    print(f" 💰 보유 코인: {current_gold} Gold | 📦 이동권: {items}개 | 🔍 스캔권: {scans}개")
    print("=" * 60)
    print(" [ 서식지 및 드래곤 통합 현황 ]")
    print("    0        1        2   (열)") 
    
    for i in range(3):
        print(f"{i} ", end="") 
        for j in range(3):
            print(f"{current_map[i][j]}  ", end="")
        print() 
    print("=" * 60)


# ==========================================
# [3단계] 알 배치 함수 정의
# ==========================================
def place_egg(current_map, is_tutorial=False):
    print("\n📦 [인벤토리] 가방에서 '드래곤의 알'을 꺼냅니다.")
    if is_tutorial:
        print("💡 [튜토리얼 가이드] 첫 번째 알은 연습을 위해 (0, 0) 좌표에 배치해 봅시다!")
    else:
        print("-> 알을 배치할 3x3 지도의 빈 칸(❓) 좌표를 입력하세요. (1턴 소모)")
    
    while True:
        try:
            row = int(input("배치할 행 번호(0~2): "))
            col = int(input("배치할 열 번호(0~2): "))
            
            if row < 0 or row > 2 or col < 0 or col > 2:
                print("❌ 범위를 벗어났습니다! 0, 1, 2 중에서 선택해 주세요.")
                continue 
                
            if is_tutorial and (row != 0 or col != 0):
                print("❌ [튜토리얼 알림] 가이드를 따라 (0, 0) 칸에 알을 배치해 주세요!")
                continue
                
            if current_map[row][col] != '[ ❓ ]' and current_map[row][col] != '[🔍空]':
                print("❌ 이미 다른 대상이 배치된 칸입니다! 빈 칸(❓)을 골라주세요.")
                continue
                
            current_map[row][col] = '[ 🥚 ]'
            print(f"-> 🎉 ({row}, {col}) 좌표에 알을 성공적으로 안착시켰습니다!")
            break 
            
        except ValueError:
            print("❌ 잘못된 입력입니다! 정수 숫자가 필요합니다.")


# ==========================================
# [4단계] 부화 및 코인 정산 함수
# ==========================================
def hatch_and_reward(current_map, secret_map, current_gold, force_tutorial_mismatch=False):
    round_income = 0
    properties = {'F': '🔥 불', 'W': '💧 물', 'G': '🌱 흙'} 
    
    print("\n⏳ 턴이 종료되었습니다. 섬의 환경 변화를 분석합니다...")
    
    for i in range(3):
        for j in range(3):
            if current_map[i][j] == '[ 🥚 ]':
                land_type = secret_map[i][j]          
                
                if force_tutorial_mismatch:
                    wrong_pool = ['F', 'W', 'G']
                    wrong_pool.remove(land_type) 
                    dragon_type = random.choice(wrong_pool) 
                else:
                    dragon_type = random.choice(['F', 'W', 'G'])  
                
                land_emoji = properties[land_type][0]
                dragon_emoji = properties[dragon_type][0] + "🐉"
                current_map[i][j] = f"[{land_emoji}|{dragon_emoji}]"
                
                print(f"🎉 [{properties[land_type]} 서식지]에서 [{properties[dragon_type]} 속성 드래곤]이 부화했습니다!")
                
                if land_type == dragon_type:
                    print("   ✨ 대박! 서식지와 드래곤 속성이 일치하여 부화 보너스 100코인을 추가로 얻습니다! (+150 Gold)")
                    round_income += 150  
                else:
                    print("   😅 아쉽게도 서식지와 다른 속성의 드래곤이 깨어났습니다. (+10 Gold)")
                    round_income += 10   
            
            elif "👑" in current_map[i][j]:
                round_income += 300
            elif "🐉" in current_map[i][j]:
                if current_map[i][j] in ['[🔥|🔥🐉]', '[💧|💧🐉]', '[🌱|🌱🐉]']:
                    round_income += 50   
                else:
                    round_income += 10   

    # 고대 드래곤 진화 체크
    for i in range(3):
        if "🐉" in current_map[i][0] and "🐉" in current_map[i][1] and "🐉" in current_map[i][2]:
            d1 = current_map[i][0][4]
            if d1 == current_map[i][1][4] == current_map[i][2][4] and "👑" not in current_map[i][1]:
                print(f"\n✨ [고대 진화!] {i}번 행에 동일한 속성의 드래곤 3마리가 일렬 배치되었습니다!")
                current_map[i][0], current_map[i][1], current_map[i][2] = f"[{d1}| ． ]", f"[{d1}|👑🐉]", f"[{d1}| ． ]"
                print(f"👑 매 턴 300코인을 생산하는 초거대 고대 드래곤({d1}👑🐉) 탄생!")

    for j in range(3):
        if "🐉" in current_map[0][j] and "🐉" in current_map[1][j] and "🐉" in current_map[2][j]:
            d1 = current_map[0][j][4]
            if d1 == current_map[1][j][4] == current_map[2][j][4] and "👑" not in current_map[1][j]:
                print(f"\n✨ [고대 진화!] {j}번 열에 동일한 속성의 드래곤 3마리가 일렬 배치되었습니다!")
                current_map[0][j], current_map[1][j], current_map[2][j] = f"[{d1}| ． ]", f"[{d1}|👑🐉]", f"[{d1}| ． ]"
                print(f"👑 매 턴 300코인을 생산하는 초거대 고대 드래곤({d1}👑🐉) 탄생!")

    if round_income > 0:
        print(f"💰 [턴 정산 완료] 이번 턴에 총 +{round_income} 코인을 획득했습니다!")
    return current_gold + round_income


# ==========================================
# [5단계] 드래곤 이동 함수 (버그 수정 완료)
# ==========================================
def use_move_item(current_map, secret_map, current_items, is_tutorial=False):
    if current_items <= 0 and not is_tutorial:
        print("\n❌ [아이템 사용 실패] 보유 중인 이동권이 없습니다!")
        return False 
        
    print("\n📦 [가방] '드래곤 이동권'을 사용하여 드래곤을 이사시킵니다.")
    
    while True:
        try:
            print("\n[1] 이동할 드래곤이 있는 칸을 선택하세요.")
            if is_tutorial:
                print("💡 (힌트: 방금 태어난 드래곤이 있는 '0'행 '0'열을 고르세요.)")
            start_row = int(input("출발 행 번호(0~2): "))
            start_col = int(input("출발 열 번호(0~2): "))
            
            if "🐉" not in current_map[start_row][start_col]:
                print("❌ 그 칸에는 드래곤이 살고 있지 않습니다!")
                continue
                
            print("\n[2] 드래곤을 보낼 목적지 칸을 선택하세요.")
            if is_tutorial:
                print("💡 [튜토리얼 강제]: 이 드래곤에게 딱 알맞은 속성의 진짜 서식지로 보내봅시다!")
                print("    안전하게 성공 보너스를 얻을 수 있는 '0'행 '1'열로 보내보세요.")
                
            end_row = int(input("목적 행 번호(0~2): "))
            end_col = int(input("목적 열 번호(0~2): "))
            
            if is_tutorial and (end_row != 0 or end_col != 1):
                print("❌ [튜토리얼 가이드] 최고의 효율을 학습하기 위해 가이드대로 '0'행 '1'열을 입력해 주세요!")
                continue
                
            if start_row == end_row and start_col == end_col:
                print("❌ 출발지와 목적지가 같습니다!")
                continue
                
            # 데이터 추출
            target_land_type = secret_map[end_row][end_col]   
            moving_dragon = "👑🐉" if "👑" in current_map[start_row][start_col] else current_map[start_row][start_col][4] + "🐉"
            
            # 🛠️ [버그 수정]: 출발지 칸의 원래 땅 속성을 안전하게 보존하고 드래곤을 삭제합니다.
            start_land_emoji = current_map[start_row][start_col][1] 
            current_map[start_row][start_col] = f"[{start_land_emoji}| ． ]"
            
            # 목적지 세팅
            properties = {'F': '🔥', 'W': '💧', 'G': '🌱'}
            target_land_emoji = properties[target_land_type] 
            
            # 목적지에 기존 드래곤이 있었다면 Swap 처리 (본게임용)
            if "🐉" in current_map[end_row][end_col] and not is_tutorial:
                staying_dragon = "👑🐉" if "👑" in current_map[end_row][end_col] else current_map[end_row][end_col][4] + "🐉"
                current_map[start_row][start_col] = f"[{start_land_emoji}|{staying_dragon}]"
                print("🔄 두 서식지의 드래곤이 서로 위치를 맞바꿨습니다!")
            
            current_map[end_row][end_col] = f"[{target_land_emoji}|{moving_dragon}]"
            print(f"\n✨ 이사 완료! 목적지의 숨겨진 진짜 땅 속성({target_land_emoji})이 투명하게 드러났습니다!")
            return True 
            
        except ValueError:
            print("❌ 숫자를 입력하세요.")


# ==========================================
# [5단계-추가] 지형 스캔권 함수
# ==========================================
def use_scan_item(current_map, secret_map, current_scans):
    if current_scans <= 0:
        print("\n❌ [아이템 사용 실패] 스캔권 부족!")
        return False
    print("\n🔍 [가방] '지형 스캔권'을 사용합니다. (1턴 소모)")
    while True:
        try:
            row, col = int(input("행 번호: ")), int(input("열 번호: "))
            if current_map[row][col] != '[ ❓ ]':
                print("❌ 이미 열려있습니다.")
                continue
            properties = {'F': '🔥', 'W': '💧', 'G': '🌱'}
            land_emoji = properties[secret_map[row][col]]
            current_map[row][col] = f"[{land_emoji}| ． ]" 
            print(f"✨ 스캔 성공! ({row}, {col}) 칸은 {land_emoji} 지형입니다!")
            return True
        except ValueError:
            print("❌ 숫자 입력")


# ==========================================
# [6단계] 상점 함수 (0턴 소모)
# ==========================================
def open_shop(current_gold, current_items, current_scans):
    print("\n🏪 [상점] 중앙 상점에 입장했습니다. (0턴 소모)")
    while True:
        print(f" 보유 자산: 💰 {current_gold} Gold | 📦 이동권 {current_items}개 | 🔍 스캔권 {current_scans}개")
        print(f" 1. 드래곤 이동권 구매 ({ITEM_PRICE} Gold) | 2. 지형 스캔권 구매 ({SCAN_PRICE} Gold) | 3. 퇴장하기")
        choice = input("▶️ 번호 선택: ")
        if choice == '1' and current_gold >= ITEM_PRICE:
            current_gold, current_items = current_gold - ITEM_PRICE, current_items + 1
            print("✨ 이동권 구매 완료!")
        elif choice == '2' and current_gold >= SCAN_PRICE:
            current_gold, current_scans = current_gold - SCAN_PRICE, current_scans + 1
            print("✨ 스캔권 구매 완료!")
        elif choice == '3':
            print("🏪 상점에서 퇴장합니다.")
            break
        else:
            print("❌ 번호 혹은 코인을 확인하세요.")
    return current_gold, current_items, current_scans


# ==========================================
# 🏁 [메인 게임 실행부]
# ==========================================

# ------------------------------------------
# 🔰 [TUTORIAL 1단계: 배치 및 불일치 정산 체험]
# ------------------------------------------
display_status(player_name, 1, gold, move_items, scan_items, game_map)
print("\n📢 [튜토리얼 1단계: 알 배치하기]")
print(" 드래곤 아일랜드 경영을 시작해 봅시다. 정부 지원금으로 첫 알이 가방에 들어왔습니다.")
input(" 👉 [ENTER]를 눌러 가방을 열고 가이드에 따라 알을 배치해 봅시다...")
place_egg(game_map, is_tutorial=True)

display_status(player_name, 1, gold, move_items, scan_items, game_map)
print("\n📢 [알 배치 완료!]")
input(" 👉 [ENTER]를 눌러 1턴 경과를 보고 부화 결과를 확인합시다...")
gold = hatch_and_reward(game_map, hidden_map, gold, force_tutorial_mismatch=True)


# ------------------------------------------
# 🔰 [TUTORIAL 2단계: 상점 구매 및 이동 체험]
# ------------------------------------------
display_status(player_name, 2, gold, move_items, scan_items, game_map)
print("\n📢 [튜토리얼 2단계: 상점과 아이템 꺼내 쓰기]")
print(" 이런! 서식지 속성과 드래곤의 속성이 맞지 않아 턴당 수입 코인이 바닥을 칩니다.")
print(" 드래곤에게 딱 알맞은 집을 선물해 주기 위해 중앙 상점으로 이동해 봅시다.")
input(" 👉 [ENTER]를 눌러 중앙 상점에 입장하여 '드래곤 이동권'을 강제로 구매해 봅시다...")

gold -= ITEM_PRICE
move_items += 1
print(f"\n🏪 [상점 자동 시스템] 이동권 1개를 {ITEM_PRICE}코인에 대리 구매했습니다. (-{ITEM_PRICE} Gold)")
print(f" 현재 매니저 가방 현황: 📦 드래곤 이동권 {move_items}개 보유 중")
input(" 👉 [ENTER]를 눌러 가방을 열고 드래곤을 진짜 서식지로 탈출시킵니다...")

# 🛠️ 여기서 출발지 (0,0) 칸이 정상적으로 비워지도록 내부 연산 로직을 정교화했습니다.
use_move_item(game_map, hidden_map, move_items, is_tutorial=True)
move_items -= 1 

display_status(player_name, 2, gold, move_items, scan_items, game_map)
print("\n📢 [튜토리얼 이사 완료!]")
print(" 드래곤의 서식지 환경이 최적화되었습니다. 이제부터 숨막히는 골드 혜택이 쏟아집니다.")
input(" 👉 [ENTER]를 눌러 2턴 경과 결과를 보고 튜토리얼을 마친 뒤 본게임으로 진입합니다!")
gold = hatch_and_reward(game_map, hidden_map, gold)


# ------------------------------------------
# ⚔️ [MAIN GAME: 본게임 시작]
# ------------------------------------------
print("\n" * 3)
print("==================================================")
print(" 🎉 축하합니다! 드래곤 이주 튜토리얼 가이드를 전원 마쳤습니다. 🎉")
print(" 지금부터 플레이어님의 순수 뇌지컬로 움직이는 진짜 10턴 본게임이 시작됩니다!")
print("==================================================")
input(" 🕹️ [ENTER]를 누르면 진짜 1턴의 막이 올라갑니다. 화이팅!")

scan_items = 1 

for turn in range(3, 13): 
    display_status(player_name, turn, gold, move_items, scan_items, game_map)
    
    while True:
        print("\n🎮 이번 턴에 어떤 경영 지시를 내리시겠습니까?")
        print(" [A타입 - 1턴 소모] 1. 인벤토리에서 새 드래곤 알(🥚) 꺼내서 배치하기")
        print(" [B타입 - 변동 소모] 2. 상점 방문 및 보유 아이템(이동/스캔) 가방에서 꺼내 쓰기")
        print(" [C타입 - 0턴 소모] 3. 행동 없이 안전하게 이번 턴 그냥 넘기기")
        main_choice = input("▶️ 타입을 고르세요 (1, 2, 3): ")
        
        if main_choice == '1':
            place_egg(game_map, is_tutorial=False)
            break
        elif main_choice == '2':
            action_completed = False
            while True:
                print("\n⚙️ [상점 및 가방 관리 메뉴]")
                print(" 🛒 [0턴 소모] 1. 상점 들어가서 아이템 구매하기")
                print(" 📦 [1턴 소모] 2. 가방에서 [드래곤 이동권] 꺼내 쓰기")
                print(" 🔍 [1턴 소모] 3. 가방에서 [지형 스캔권] 꺼내 쓰기")
                print(" ↩️  [0턴 소모] 4. 뒤로 가기 (메인 행동 다시 선택)")
                sub_choice = input("▶️ 번호를 선택하세요: ")
                
                if sub_choice == '1':
                    gold, move_items, scan_items = open_shop(gold, move_items, scan_items)
                    display_status(player_name, turn, gold, move_items, scan_items, game_map)
                elif sub_choice == '2':
                    if use_move_item(game_map, hidden_map, move_items, is_tutorial=False):
                        move_items -= 1
                        action_completed = True
                        break 
                elif sub_choice == '3':
                    if use_scan_item(game_map, hidden_map, scan_items):
                        scan_items -= 1
                        action_completed = True
                        break 
                elif sub_choice == '4':
                    break
            if action_completed:
                break 
        elif main_choice == '3':
            print("▶️ 자원 비축을 선택했습니다.")
            break
        else:
            print("❌ 1, 2, 3 중에서 골라주세요.")
            
    gold = hatch_and_reward(game_map, hidden_map, gold)
    
    if turn < 12:
        print(f"\n🎁 다음 턴에 사용할 보급용 드래곤 알이 인벤토리에 도착했습니다.")

# 최종 엔딩 연출
print("\n" * 3)
print("==================================================")
print(" 🎉 GAME OVER! 드래곤 아일랜드의 모든 개척이 종료되었습니다. 🎉")
print("==================================================")
print(f" 매니저 성함: {player_name} | 최종 정산 자산: 💰 {gold} Gold")

if gold >= 2800: 
    grade = "🏆 S등급 (대륙의 지배자)"
elif gold >= 1600:
    grade = "🥇 A등급 (프로 매니저)"
else:
    grade = "🥈 B등급 (평범한 섬 개척자)"
print(f" 최종 랭크: {grade}\n==================================================")