"""
此程式在模擬暴率暴傷最大值

觀察結論:
基本上就是保持平衡成長
舉例 假設一次成長+10暴率 或+40暴傷 二選一
那分配上還是選一次暴率 一次暴傷 讓選的次數維持1:1 數值維持1:4?

"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# 指定微軟正黑體的字體路徑
msjh_font = FontProperties(fname=r"C:\Windows\Fonts\msjh.ttc")

# 定義參數
resource_limit = 50  # x + y/2 = resource_limit
x_values = np.linspace(0, 100, 500)  # 限制 x 最大值為 100
y_values = 10000 * (resource_limit - x_values)  # 根據條件計算對應的 y

# 計算目標函數值
output_values = (100 - x_values) * 100 + x_values * (100 + y_values)

# 找到最大值及其對應的 x 和 y
max_index = np.argmax(output_values)
max_x = x_values[max_index]
max_y = y_values[max_index]

# 繪圖
plt.figure(figsize=(8, 6))
plt.plot(x_values, output_values, label="目標函數", color='blue')  # 曲線圖的標籤
plt.title("暴擊率與爆擊傷害分配的曲線圖", fontsize=14, fontproperties=msjh_font)
plt.xlabel("暴擊率 x", fontsize=12, fontproperties=msjh_font)
plt.ylabel("目標函數值", fontsize=12, fontproperties=msjh_font)
plt.axvline(resource_limit / 2, color='red', linestyle='--', label="資源均分點 (x = y/2)", linewidth=1.5)
plt.legend(prop=msjh_font)
plt.grid()

# 標註最大值節點，顯示 x 和 y 的值
plt.scatter(max_x, (100 - max_x) * 100 + max_x * (100 + max_y), color='orange', label="最大值節點", zorder=5)
plt.text(max_x, (100 - max_x) * 100 + max_x * (100 + max_y), 
         f"({max_x:.1f}, {max_y:.1f})", fontsize=10, fontproperties=msjh_font, 
         color="black", ha="center", va="bottom")

# 顯示圖表
plt.show()
