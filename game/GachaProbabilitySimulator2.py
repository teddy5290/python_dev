import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties
import matplotlib

# 設置全局字體
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei', 'DFKai-SB', 'SimSun', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

def simulate_limited_character(p=0.008, max_draws=160, trials=100000):
    """
    模擬抽卡機制，計算抽中限定角色的機率。
    當抽到限定角色後即停止抽卡。

    參數：
    p: 單抽出現5星角色的機率
    max_draws: 最大模擬抽數
    trials: 模擬次數

    返回：
    抽數陣列、各抽數機率、累積機率
    """
    draws_needed = np.zeros(trials, dtype=np.int32)  # 記錄每次試驗需要的抽數

    for trial in range(trials):
        draws = 0
        guaranteed = False  # 是否進入大保底狀態
        pity_counter = 0   # 保底計數器
        got_character = False  # 是否抽到限定角色
        
        while not got_character and draws < max_draws:
            draws += 1
            pity_counter += 1

            # 檢查是否達到80抽保底
            if pity_counter >= 80:
                if guaranteed:  # 大保底必定得到限定角色
                    got_character = True
                elif np.random.random() < 0.5:  # 小保底50%機率
                    got_character = True
                else:  # 小保底歪掉
                    guaranteed = True
                pity_counter = 0
            # 一般抽卡
            elif np.random.random() < p:  # 抽到5星
                if guaranteed:  # 大保底狀態必定得到限定角色
                    got_character = True
                elif np.random.random() < 0.5:  # 一般狀態50%機率
                    got_character = True
                else:  # 歪掉進入大保底
                    guaranteed = True
                pity_counter = 0
            
            if got_character:
                draws_needed[trial] = draws

    # 計算每個抽數的次數
    draws_count = np.bincount(draws_needed)[1:max_draws+1]
    # 計算機率
    prob = draws_count / trials
    # 計算累積機率
    cumulative_prob = np.cumsum(prob)
    
    return np.arange(1, max_draws + 1), prob, cumulative_prob

# 模擬參數
p = 0.008
max_draws = 160
trials = 100000

# 執行模擬
x, prob, cumulative_prob = simulate_limited_character(p, max_draws, trials)

# 建立字型物件
font = FontProperties(family=['Microsoft JhengHei', 'DFKai-SB', 'SimSun'])

# 創建圖表
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), height_ratios=[2, 1])
plt.subplots_adjust(hspace=0.3)

# 繪製累積機率圖
ax1.plot(x, cumulative_prob, label="限定角色累積機率", color="b")
ax1.axvline(80, color="r", linestyle="--", label="小保底 (80抽)")
ax1.axvline(160, color="g", linestyle="--", label="大保底 (160抽)")
ax1.set_xticks(np.arange(0, 161, 10))
ax1.set_xlabel("抽數", fontproperties=font, fontsize=12)
ax1.set_ylabel("累積機率", fontproperties=font, fontsize=12)
ax1.set_title("限定角色累積機率曲線", fontproperties=font, fontsize=14)
ax1.legend(prop=font)
ax1.grid(True)

# 繪製單抽機率圖
ax2.plot(x, prob, label="限定角色獲得機率", color="r")
ax2.axvline(80, color="r", linestyle="--", label="小保底 (80抽)")
ax2.axvline(160, color="g", linestyle="--", label="大保底 (160抽)")
ax2.set_xticks(np.arange(0, 161, 10))
ax2.set_xlabel("抽數", fontproperties=font, fontsize=12)
ax2.set_ylabel("機率", fontproperties=font, fontsize=12)
ax2.set_title("限定角色獲得機率分布", fontproperties=font, fontsize=14)
ax2.legend(prop=font)
ax2.grid(True)

plt.show()