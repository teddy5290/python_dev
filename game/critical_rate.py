import numpy as np

def calculate_total_damage(base_damage, crit_rate, crit_damage):
    return (base_damage * (1 - crit_rate)) + (base_damage * crit_damage * crit_rate)

def find_all_ratios(base_damage):
    results = []
    
    crit_rates = np.linspace(0, 1, 101)  # 暴擊率從0到1，步長0.01
    max_crit_damage = 1 + (15 / 6.3)  # 根據最大暴擊傷害計算
    
    for crit_rate in crit_rates:
        # 根據6.3比15的比例調整爆擊傷害，從最大值開始遞減到1.5
        crit_damage = max_crit_damage - ((max_crit_damage - 1.5) * crit_rate)
        total_damage = calculate_total_damage(base_damage, crit_rate, crit_damage)
        
        results.append((crit_rate, crit_damage, total_damage))
                
    return results

# 設定基本傷害值
base_damage = 100

results = find_all_ratios(base_damage)

# 列出所有結果
for crit_rate, crit_damage, total_damage in results:
    print(f"暴擊率: {crit_rate:.2f}, 爆擊傷害: {crit_damage:.2f}, 總傷害: {total_damage:.2f}")
