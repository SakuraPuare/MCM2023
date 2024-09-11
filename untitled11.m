% 定义微分方程
r = 0.1; % 植物的增长速率
K = 1000; % 生态系统的容量
f = @(t) sin(t); % 光照强度在时间t的变化率
eq = @(t, N) r * N * (1 - N / K) * f(t); % 微分方程

% 定义模拟参数
tspan = [0, 10]; % 模拟的时间区间
N0 = 100; % 初始植物数量

% 使用ode45函数数值求解微分方程
[t, N] = ode45(eq, tspan, N0); % 时间从0到10，初始植物数量为100

% 绘制曲线
yyaxis left % 左边的坐标轴表示植物数量
plot(t, N);
ylabel('Number of plants');

yyaxis right % 右边的坐标轴表示光照强度
fplot(f, tspan, 'r');
ylabel('Sunlight');

xlabel('Time');
