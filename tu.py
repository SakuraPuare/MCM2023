import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# 定义方程组
def LVmodel(y, t, r1, r2, K1, K2, alpha, beta):
    N1, N2 = y
    dN1dt = r1 * N1 * (1 - (N1 + alpha * N2) / K1)
    dN2dt = r2 * N2 * (1 - (N2 + beta * N1) / K2)
    return [dN1dt, dN2dt]

# 设置模型参数
r1 = 1.0
r2 = 1.0
K1 = 500
K2 = 400
alpha = 0.01
beta = 0.01

# 设置初值
N0 = [200, 200]

# 设置时间点
t = np.linspace(0, 20, 1000)

# 使用odeint函数对方程组进行求解
sol = odeint(LVmodel, N0, t, args=(r1, r2, K1, K2, alpha, beta))

# 绘制结果
plt.plot(t, sol[:, 0], 'r', label='N1(t)')
plt.plot(t, sol[:, 1], 'b', label='N2(t)')
plt.xlabel('Time')
plt.ylabel('Population size')
plt.title('Lotka-Volterra competition model')
plt.legend(loc='best')
plt.show()
