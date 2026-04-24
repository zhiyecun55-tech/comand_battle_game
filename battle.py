import random
player_hp = 100
enemy_hp = 100
player_action = [1, 2, 3]
enemy_action = [1, 2, 3]
turn = 1

import time
def slow_print(text, delay=0.05):
    for c in text:
        print(c, end="", flush=True)
        time.sleep(delay)
    print()  # 最後に改行

while player_hp > 0 and enemy_hp > 0 :
    print()
    print(f"ー{turn}ターン目ー")
    print()
    print(f"あなたのHP: {player_hp}")
    print(f"相手のHP: {enemy_hp}")
    print("行動を選択してください")
    print("1.攻撃")
    print("2.回避")
    print("3.チャージ攻撃")
    print()
    while True:
     player = input("番号を入力: ")

     if player in ["1", "2", "3"]:
        player = int(player)
        break
     else:
        print("1〜3で入力してください")
    enemy = random.choice(enemy_action)

    if player == 1 and enemy == 1:
            print()
            slow_print("あなたの攻撃！")
            time.sleep(1)
            slow_print("相手に10ダメージ!")
            enemy_hp -= 10
            if enemy_hp <= 0:
                break
            time.sleep(1)
            slow_print("相手の攻撃！")
            time.sleep(1)
            slow_print("自分に10ダメージ!")
            player_hp -= 10
            if player_hp <= 0:
                break
            turn += 1
            time.sleep(1)
            print()
            input("Enterで次へ")

    elif player == 1 and enemy == 2:
            print()
            slow_print("相手は回避の構えだ")
            time.sleep(1)
            slow_print("あなたの攻撃！")
            time.sleep(1)
            slow_print("回避された") 
            time.sleep(1)
            slow_print("回避ボーナスで相手のHPが10回復")
            enemy_hp += 10
            min(enemy_hp, 100)  # HPが100を超えないようにする
            time.sleep(1)
            turn += 1
            print()
            input("Enterで次へ")
            
    elif player == 1 and enemy == 3:
            print()
            slow_print("相手は詠唱をしている")
            time.sleep(1)
            slow_print("あなたの攻撃！")
            time.sleep(1)
            slow_print("相手に10ダメージ!")
            enemy_hp -= 10
            if enemy_hp <= 0:
                break
            time.sleep(1)
            slow_print("詠唱が中断された") 
            time.sleep(1)
            turn += 1
            print()
            input("Enterで次へ")

    elif player == 2 and enemy == 1:
            print()
            slow_print("あなたは回避の構え！") 
            time.sleep(1)
            slow_print("相手の攻撃！")
            time.sleep(1)
            slow_print("回避成功！") 
            time.sleep(1)
            slow_print("回避ボーナスでHPが10回復")
            player_hp += 10
            min(player_hp, 100)  # HPが100を超えないようにする
            time.sleep(1)
            turn += 1
            print()
            input("Enterで次へ")

    elif player == 2 and enemy == 2:
            print()
            slow_print("あなたは回避の構え！") 
            time.sleep(1)
            slow_print("相手も回避の構え！")
            time.sleep(1)
            slow_print("何も起こらない")
            time.sleep(1)
            turn += 1
            print()
            input("Enterで次へ")

    elif player == 2 and enemy == 3:
            print()
            slow_print("あなたは回避の構え！") 
            time.sleep(1)
            slow_print("相手は詠唱をしている")
            time.sleep(1)
            slow_print("回避の構えは解かれた")
            time.sleep(1)
            slow_print("相手のチャージ攻撃！")
            time.sleep(1)
            slow_print("あなたに20ダメージ!")
            player_hp -= 20
            if player_hp <= 0:
                break
            time.sleep(1)
            turn += 1
            print()
            input("Enterで次へ")

    elif player == 3 and enemy == 1:
            print()
            slow_print("あなたは詠唱をしている")
            time.sleep(1)
            slow_print("相手の攻撃！")
            time.sleep(1)
            slow_print("あなたに10ダメージ!")
            player_hp -= 10
            if player_hp <= 0:
                break
            time.sleep(1)
            slow_print("詠唱が中断された")
            time.sleep(1)
            turn += 1
            print()
            input("Enterで次へ")

    elif player == 3 and enemy == 2:
            print()
            slow_print("あなたは詠唱をしている")
            time.sleep(1)
            slow_print("相手は回避の構え！")
            time.sleep(1)
            slow_print("回避の構えは解かれた")
            time.sleep(1)
            slow_print("チャージ攻撃！")
            time.sleep(1)
            slow_print("相手に20ダメージ!")
            enemy_hp -= 20
            if enemy_hp <= 0:
                break
            time.sleep(1)
            turn += 1
            print()
            input("Enterで次へ")

    elif player == 3 and enemy == 3:
            print()
            slow_print("あなたは詠唱をしている")
            time.sleep(1)
            slow_print("相手も詠唱をしている")
            time.sleep(1)
            slow_print("チャージ攻撃!")
            time.sleep(1)
            slow_print("相手に20ダメージ!")
            enemy_hp -= 20
            if enemy_hp <= 0:
                break
            time.sleep(1)
            slow_print("相手のチャージ攻撃!")
            time.sleep(1)
            slow_print("あなたに20ダメージ!")
            player_hp -= 20
            if player_hp <= 0:
                break
            time.sleep(1)
            turn += 1
            print()
            input("Enterで次へ")

if player_hp <= 0:
    time.sleep(1)
    slow_print("体力が尽きて目の前が真っ暗になった...")
elif enemy_hp <= 0:
    time.sleep(1)
    slow_print("相手が倒れた！あなたの勝ちだ！")