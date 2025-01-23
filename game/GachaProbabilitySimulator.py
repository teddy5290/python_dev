"""
這個程式模擬抽卡機制，計算抽中「限定角色」的累積機率，並繪製機率曲線。
適用於像《原神》這樣的抽卡系統，考慮以下規則：
1. 單抽有固定機率（如 0.8%）出現5星角色。
2. 抽中5星角色有50%機率是限定角色。
3. 若80抽內都沒出現5星角色，第80抽保底出現5星角色（小保底）。
4. 抽到非限定角色後，下一次出5星必定出限定角色（大保底）。
5. 曲線顯示每個抽數時，累積抽中限定角色的機率。

輸出：累積機率曲線圖，顯示從1抽到160抽的結果。
"""
import numpy as np
import matplotlib.pyplot as plt

def calculate_limited_probability_curve(single_rate, max_guaranteed, total_pulls, simulations=100000):
    probabilities = np.zeros(total_pulls)

    for _ in range(simulations):
        guarantee_limited = False
        pulls = 0
        got_limited = False

        while pulls < total_pulls and not got_limited:
            pulls += 1
            if pulls % max_guaranteed == 0:  # 保底出5星
                if guarantee_limited or np.random.rand() < 0.5:
                    probabilities[pulls - 1:] += 1  # 從當前抽數起累積成功
                    got_limited = True
                else:
                    guarantee_limited = True  # 下一次必限定
            elif np.random.rand() < single_rate:  # 普通抽中5星
                if guarantee_limited or np.random.rand() < 0.5:
                    probabilities[pulls - 1:] += 1
                    got_limited = True
                else:
                    guarantee_limited = True  # 下一次必限定

    probabilities /= simulations  # 計算機率
    return probabilities

# 設定參數
single_rate = 0.008  # 單次抽5星的概率（0.8%）
max_guaranteed = 80  # 小保底次數
total_pulls = 180  # 繪製到180抽
simulations = 10000  # 模擬次數

# 計算結果
probabilities = calculate_limited_probability_curve(single_rate, max_guaranteed, total_pulls, simulations)

# 繪製曲線圖
plt.figure(figsize=(10, 6))
plt.plot(range(1, total_pulls + 1), probabilities, label="累積抽中限定角色的機率")
plt.xlabel("抽數")
plt.ylabel("累積機率")
plt.title("限定角色累積抽中機率曲線")
plt.grid(True)
plt.legend()
plt.show()
