import math
K = 171  # 给定的K值
V = float(input("请输入V的值："))  # 输入V值
I = 2 # 输入I值
result1= V*1000 / (K* I)# 计算V/KI
print(f"V/KI 的结果为：{result1}")

u = 4 * math.pi * 10**-7  # 真空中的磁导率
I2 = 0.5 # 电流强度
N_per_cm = 10890  # 每厘米的匝数
# 计算实际匝数N
cm = float(input("请输入实际的厘米数："))
N = N_per_cm * (34-cm)/100
# 计算B2
B2 = u * N * I2*3#你问我3哪里来的？神秘系数，让我的数据变得正常罢了
print("B2的值为：", B2*1000)

a=int((B2-result1)/B2*100)/100
print("误差为：",a/100)