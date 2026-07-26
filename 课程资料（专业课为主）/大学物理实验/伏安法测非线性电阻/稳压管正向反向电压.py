import numpy as np
import matplotlib.pyplot as plt

# 原始数据
U = np.array([0.0000, 0.2941, 0.4464, 0.4908, 0.5635, 0.5864, 0.6073, 0.6275, 0.6389, 0.6469, 0.6531, 0.6643, 0.6722, 0.6832, 0.6910, 0.6971, 0.7020, 0.7061, 0.7069, 0.7130, -5.5950, -6.0550, -6.3440, -7.0380, -7.2460, -7.3830, -7.4590, -7.4770, -7.4840, -7.4880, -7.4990, -7.5070, -7.5230, -7.5390, -7.5560, -7.5680, -7.5860, -7.6060, -7.6210])
I = np.array([0.000, 0.003, 0.006, 0.010, 0.050, 0.100, 0.200, 0.400, 0.600, 0.800, 1.000, 1.500, 2.000, 3.000, 4.000, 5.000, 6.000, 7.000, 8.000, 9.000, -0.003, -0.006, -0.010, -0.050, -0.100, -0.200, -0.400, -0.600, -0.800, -1.000, -1.500, -2.000, -3.000, -4.000, -5.000, -6.000, -7.000, -8.000, -9.000])

# 找到电流变化时电压变化最小的区域
def find_stable_voltage(U, I):
    diff_I = np.diff(I)
    diff_U = np.diff(U)
    ratio = np.abs(diff_U / diff_I)
    stable_index = np.argmin(ratio)
    return (U[stable_index] + U[stable_index + 1]) / 2

stable_voltage_pos = find_stable_voltage(U[U >= 0], I[U >= 0])
stable_voltage_neg = find_stable_voltage(U[U < 0], I[U < 0])

# 绘制数据和稳压点
plt.scatter(U, I, label='Original Data')
plt.axvline(x=stable_voltage_pos, color='green', linestyle='--', label=f'Stable Voltage (Positive): {stable_voltage_pos:.4f} V')
plt.axvline(x=stable_voltage_neg, color='purple', linestyle='--', label=f'Stable Voltage (Negative): {stable_voltage_neg:.4f} V')
plt.xlabel('Voltage (V)')
plt.ylabel('Current (mA)')
plt.legend()
plt.title('V-I Characteristics of Zener Diode')
plt.grid(True)
plt.show()

# 打印稳压电压
stable_voltage_pos, stable_voltage_neg