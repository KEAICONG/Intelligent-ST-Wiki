import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# 原始数据
U = np.array([0.000, 0.500, 1.000, 1.500, 2.000, 2.500, 3.000, 3.500, 4.000, 4.500, 5.000, 5.500, 6.000, 6.500, 7.000])
I = np.array([0, 29.75, 39.96, 47.32, 53.92, 60.16, 65.92, 71.39, 76.6, 81.53, 86.35, 90.9, 95.28, 99.51, 103.16]) / 1000  # 转换为安培

# 定义拟合函数
def fit_func(U, K, n):
    return K * U**n

# 初始猜测值
initial_guess = [1, 1]

# 进行拟合
popt, pcov = curve_fit(fit_func, U, I, p0=initial_guess)

# 获取拟合参数
K, n = popt

# 打印拟合参数
print(f"K = {K:.4f}, n = {n:.4f}")

# 绘制数据和拟合曲线
U_fit = np.linspace(0, 7, 100)
I_fit = fit_func(U_fit, K, n)

plt.scatter(U, I, label='Original Data')
plt.plot(U_fit, I_fit, label=f'Fitted Curve\n$K={K:.4f}, n={n:.4f}$', color='red')
plt.xlabel('Voltage (V)')
plt.ylabel('Current (A)')
plt.legend()
plt.title('V-I Characteristics of Light Bulb')
plt.grid(True)
plt.show()

U_small = 0.001
dI_dU_at_small_U = K * n * U_small**(n-1)
print(f"斜率在 U=0.001 处为: {dI_dU_at_small_U:.4f}")
