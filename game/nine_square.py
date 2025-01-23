import random
from decimal import Decimal

# 模擬九宮格，計算123和789連線的機率
nine_square = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = Decimal(0)  # 使用 Decimal 提高精度

def sort_line(tup1, tup2, tup3):
    line_list = sorted([nine_square[tup1], nine_square[tup2], nine_square[tup3]])
    if line_list == [1, 2, 3]:
        return Decimal(1)
    elif line_list == [7, 8, 9]:
        return Decimal('0.000001')  # 精度問題透過 Decimal 解決
    return Decimal(0)

for i in range(1, 10000):
    random.shuffle(nine_square)
    result += sort_line(0, 1, 2)
    result += sort_line(3, 4, 5)
    result += sort_line(6, 7, 8)
    result += sort_line(0, 3, 6)
    result += sort_line(1, 4, 7)
    result += sort_line(2, 5, 8)
    result += sort_line(0, 4, 8)

result_1 = int(result)
result_2 = int((result - result_1) * 1000000)

print(f"i: {i}")
print(f"result: {result}")
print(f"result_1: {result_1}, result_2: {result_2}")
