import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint


# 定义模型的微分方程
def model(state, t, r, K, a):
    N1, N2, N3 = state
    dN1dt = r[0] * N1 * (1 - N1 / K[0] - a[1, 0] * N2 / K[1] - a[2, 0] * N3 / K[2])
    dN2dt = r[1] * N2 * (1 - N2 / K[1] - a[0, 1] * N1 / K[0] - a[2, 1] * N3 / K[2])
    dN3dt = r[2] * N3 * (1 - N3 / K[2] - a[0, 2] * N1 / K[0] - a[1, 2] * N2 / K[1])
    return [dN1dt, dN2dt, dN3dt]


# 定义模拟参数
t = np.linspace(0, 25, 20)  # 模拟时间范围
state0 = [5, 3, 2]  # 初始状态
r = [0.4, 0.7, 0.5]  # 自然增长率
K = [10, 9.55, 10]  # 环境容量
a = np.array([
    [0, 0.1, 0.2],
    [0.3, 0, 0.1],
    [0.5, 0.3, 0]
])  # 相互作用系数矩阵

# 定义模拟参数
# t = np.linspace(0, 25, 1000) # 模拟时间范围
# state0 = [1, 1, 1] # 初始状态
# r = [1.5, 1.0, 0.5] # 自然增长率
# K = [10, 10, 10] # 环境容量
# a = np.array([[0, 0.2, 0.1], [0.3, 0, 0.1], [0.2, 0.1, 0]]) # 相互作用系数矩阵
# b = np.array([[0, 0.2, 0.3], [0.3, 0, 0.2], [0.1, 0.3, 0]]) # 能量转移系数矩阵
# c = [0.5, 0.5, 0.5] # 自然死亡率


# 求解微分方程
states = odeint(model, state0, t, args=(r, K, a))

# 绘制结果
plt.plot(t, states[:, 0], label='Species 1')
plt.plot(t, states[:, 1], label='Species 2')
plt.plot(t, states[:, 2], label='Species 3')
# 三条曲线求和
plt.plot(t, states[:, 0] + states[:, 1] + states[:, 2], label='Total')
print((states[:, 0] + states[:, 1] + states[:, 2]).tolist())
# 隐藏xy数值
# plt.xticks([])
# plt.yticks([])

plt.xlabel('Time')
plt.ylabel('Population')
plt.legend()

# 减小空白
plt.tight_layout()
# 保存为svg
plt.savefig('population.svg', format='svg')
plt.show()
# 常规模型 Exp2:
#      f(x) = a*exp(b*x) + c*exp(d*x)
# 系数(置信边界为 95%):
#        a =       20.43  (20.41, 20.45)
#        b =  -8.125e-06  (-8.234e-06, -8.016e-06)
#        c =      -11.17  (-11.19, -11.15)
#        d =  -0.0009358  (-0.0009395, -0.0009321)
#
# 拟合优度:
#   SSE: 197.8
#   R 方: 0.995
#   调整 R 方: 0.995
#   RMSE: 0.1407


# 线性模型 Poly3:
#      f(x) = p1*x^3 + p2*x^2 + p3*x + p4
# 系数(置信边界为 95%):
#        p1 =      0.0237  (-0.003217, 0.05061)
#        p2 =     -0.5583  (-1.048, -0.06846)
#        p3 =       4.058  (1.473, 6.644)
#        p4 =       22.18  (18.43, 25.93)
#
# 拟合优度:
#   SSE: 5.602
#   R 方: 0.8473
#   调整 R 方: 0.7818
#   RMSE: 0.8946
