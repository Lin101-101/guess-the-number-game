# 文件名: main.py
# 描述: 一个简单的猜数字小游戏
# 作者: 林坚涛
# 日期: 2026-09-19

import random  # 导入随机数模块

def get_difficulty():
    """
    获取用户输入的难度选择
    """
    print("请选择难度:")
    print("1. 简单 (1-50)")
    print("2. 普通 (1-100)")
    print("3. 困难 (1-200)")
    
    while True:
        choice = input("请输入 1, 2 或 3: ")
        if choice in ['1', '2', '3']:
            return int(choice)
        else:
            print("输入无效，请重新输入。")

def play_game():
    """
    主游戏逻辑
    """
    # 1. 获取难度
    difficulty = get_difficulty()
    
    # 2. 根据难度设置范围
    if difficulty == 1:
        max_num = 50
        max_attempts = 10
    elif difficulty == 2:
        max_num = 100
        max_attempts = 7
    else:
        max_num = 200
        max_attempts = 5
        
    # 3. 生成随机答案
    answer = random.randint(1, max_num)
    
    print(f"\n游戏开始！数字范围是 1 到 {max_num}。")
    print(f"你有 {max_attempts} 次机会来猜对数字。")
    
    attempts = 0  # 记录猜测次数
    
    # 4. 游戏循环
    while attempts < max_attempts:
        try:
            guess = int(input(f"\n第 {attempts + 1} 次猜测，请输入你的数字: "))
        except ValueError:
            print("请输入一个整数！")
            continue
            
        attempts += 1
        
        if guess < 1 or guess > max_num:
            print(f"请输入 1 到 {max_num} 之间的数字！")
            continue
            
        if guess < answer:
            print("太小了！")
        elif guess > answer:
            print("太大了！")
        else:
            print(f"\n恭喜你！猜对了！答案就是 {answer}。")
            print(f"你总共用了 {attempts} 次机会。")
            return  # 游戏成功，跳出函数
            
    # 5. 机会用完了
    print(f"\n很遗憾，{max_attempts} 次机会用完了。")
    print(f"正确答案是 {answer}。再接再厉！")

# 程序入口
if __name__ == "__main__":
    print("=" * 30)
    print("欢迎来到猜数字游戏！")
    print("=" * 30)
    play_game()
# 加1行说明
# 加2行说明
# 加3行说明
# 加4行说明
# 加5行说明
# 加6行说明
# 加7行说明
# 加8行说明
# 加9行说明
# 加10行说明
# 加11行说明
# 加12行说明
# 加13行说明
# 加14行说明
# 加15行说明
# 加16行说明
# 加17行说明
# 加18行说明

