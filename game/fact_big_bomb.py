#
#計算機率的程式 (真相大爆炸)
#機制是牌堆總共28張牌 分別是黑桃 紅心 方塊 梅花四種花色的數字1到7
#每人發2張牌
#依照每人得到的黑桃數字總和進行排名
#計算各個數字當第一,二,三名的機率


import random
from collections import defaultdict

# 定義變數
num_players = 8  # 設定人數
num_simulations = 100000  # 設定模擬次數

# 定義牌堆
suits = ['黑桃', '紅心', '方塊', '梅花']
numbers = list(range(1, 8))
deck = [(suit, number) for suit in suits for number in numbers]

def calculate_probabilities(num_players, num_simulations):
    rank_counts = {i: defaultdict(int) for i in range(1, num_players + 1)}
    sum_counts = defaultdict(int)

    for _ in range(num_simulations):
        random.shuffle(deck)
        hands = [deck[i*2:(i+1)*2] for i in range(num_players)]  # 每人發2張牌
        spades_sums = [sum(card[1] for card in hand if card[0] == '黑桃') for hand in hands]
        
        sorted_sums = sorted(spades_sums, reverse=True)  # 依照黑桃總和排序

        for sum_value in spades_sums:
            sum_counts[sum_value] += 1
        
        # 計算排名
        for i, sum_value in enumerate(sorted_sums):
            rank = i + 1 if i < num_players - 1 else num_players  # 最後一名及之後都歸為最後一名
            rank_counts[rank][sum_value] += 1

    probabilities = {rank: {sum_value: count / sum_counts[sum_value] for sum_value, count in rank_counter.items()} for rank, rank_counter in rank_counts.items()}
    
    return probabilities

# 計算機率
probabilities = calculate_probabilities(num_players, num_simulations)

# 輸出結果
print("各個數字總和在不同排名的機率:")
for sum_value in range(1, 14):
    print(f"黑桃總和 {sum_value}:")
    total_prob = sum(probabilities[rank].get(sum_value, 0) for rank in range(1, num_players + 1))
    if total_prob > 0:
        for rank in range(1, num_players + 1):
            probability = probabilities[rank].get(sum_value, 0)
            rank_name = f"排名 {rank}" if rank < num_players else f"排名 {rank}及之後"
            print(f"  {rank_name}: {probability:.2%}")
