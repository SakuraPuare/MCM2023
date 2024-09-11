import random

import numpy as np
from matplotlib.pyplot import xlabel, ylabel, title, show, scatter

p0 = 0.5
k = 30
r = 5
a = 0.05
t = np.linspace(0, 25, 100)

p_u = a * k * p0 * np.exp(a * r * t)
p_l = a * k + p0 * (np.exp(a * r * t) - 1)

p = p_u / p_l / a
# plot(t, p);
xlabel('time/year')
ylabel('w(t)');
title('weight-time');
# 在函数周围生成一系列散点
scatter(t, np.array([(random.uniform(-2, 2) + i) * 0.5 for i in np.nditer(p)]))
print([(random.uniform(-2, 2) + i) * 1 for i in np.nditer(p)])
print([(random.uniform(-2, 2) + i) * 0.6 for i in np.nditer(p)])
print([(random.uniform(-2, 2) + i) * 1.1 for i in np.nditer(p)])
# plot(t, 2.234 ** -5 * t ** 3 - 0.006 * t ** 2 + 0.6637 * t + 8.18)

show()
