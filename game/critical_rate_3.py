import numpy as np
import matplotlib.pyplot as plt

# 定義參數
resource_pool = 200  # 總資源池值
allocation_range = np.linspace(0, resource_pool, 100)  # 分配範圍

# 三種分配方式
# 1. 三者平均成長（基傷:暴率:爆傷 = 1:1:1，爆傷值兩倍資源）
def balanced_growth(resource):
    base_damage = 100 + resource / 3  # 基傷成長
    crit_rate = resource / 3   # 暴率成長（百分比）
    crit_damage = 150 + 2 * resource / 3  # 爆傷成長（兩倍資源）
    expected_value = (1 - crit_rate / 100) * base_damage + (crit_rate / 100 * (base_damage * crit_damage / 100))
    return base_damage, crit_rate, crit_damage, expected_value

# 2. 爆傷與暴率平均成長，基傷固定（基傷:暴率:爆傷 = 0:1:1，爆傷值兩倍資源）
def crit_focused_growth(resource):
    base_damage = 100  # 基傷固定
    crit_rate = resource / 2   # 暴率成長（百分比）
    crit_damage = 150 + 2 * resource / 2  # 爆傷成長（兩倍資源）
    expected_value = (1 - crit_rate / 100) * base_damage + (crit_rate / 100 * (base_damage * crit_damage / 100))
    return base_damage, crit_rate, crit_damage, expected_value

# 3. 全部資源分配給基傷（基傷:暴率:爆傷 = 1:0:0）
def base_damage_growth(resource):
    base_damage = 100 + resource  # 基傷成長
    crit_rate = 0  # 暴率不變
    crit_damage = 150  # 爆傷不變
    expected_value = (1 - crit_rate / 100) * base_damage + (crit_rate / 100 * (base_damage * crit_damage / 100))
    return base_damage, crit_rate, crit_damage, expected_value

# 計算結果
balanced_result = [balanced_growth(r) for r in allocation_range]
crit_focused_result = [crit_focused_growth(r) for r in allocation_range]
base_damage_result = [base_damage_growth(r) for r in allocation_range]

# 需要顯示的資源池點
specific_points = [50, 100, 150, 200]

# 顯示這些點的資源值
for point in specific_points:
    bd_b, cr_b, cd_b, ev_b = balanced_growth(point)
    bd_c, cr_c, cd_c, ev_c = crit_focused_growth(point)
    bd_bd, cr_bd, cd_bd, ev_bd = base_damage_growth(point)
    
    print(f"資源池 {point} 的三者平均成長: 基傷={bd_b:.2f}, 爆率={cr_b:.2f}, 爆傷={cd_b:.2f}")
    print(f"資源池 {point} 的爆傷與暴率平均成長: 基傷={bd_c:.2f}, 爆率={cr_c:.2f}, 爆傷={cd_c:.2f}")
    print(f"資源池 {point} 的全部資源分配給基傷: 基傷={bd_bd:.2f}, 爆率={cr_bd:.2f}, 爆傷={cd_bd:.2f}")
    print("-" * 50)

# 繪製圖表
plt.figure(figsize=(10, 6))
plt.plot(allocation_range, [r[3] for r in balanced_result], label="三者平均成長 (1:1:1)", color="blue")
plt.plot(allocation_range, [r[3] for r in crit_focused_result], label="爆傷與暴率平均成長 (0:1:1)", color="green")
plt.plot(allocation_range, [r[3] for r in base_damage_result], label="全部資源分配給基傷 (1:0:0)", color="red")

# 圖表格式
plt.title("資源分配對期望值的影響", fontsize=14)
plt.xlabel("分配資源值", fontsize=12)
plt.ylabel("期望值", fontsize=12)
plt.legend(fontsize=10)
plt.grid()
plt.show()
