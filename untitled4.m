% 生成数据
t = linspace(0, 10, 100); % 时间
N = 500 * exp(0.1 * t) ./ (1 + 0.01 * exp(0.1 * t)); % 数量
data = [t', N'];

% 设置初始值和范围
r0 = 0.1;
K0 = 1000;
p0 = 1;
P0 = 1;
initialGuess = [r0, K0, p0, P0];

lowerBounds = [0, 0, 0, 0];
upperBounds = [Inf, Inf, Inf, Inf];

% 使用 curve fitting 工具箱拟合数据
f = fittype('r*N*(1-N/K)*p/P0', 'independent', "t'", 'dependent', 'N');
[fitresult, gof] = fit(data(:,1), data(:,2), f, 'StartPoint', initialGuess, 'Lower', lowerBounds, 'Upper', upperBounds);

% 显示拟合结果
disp(fitresult)
disp(gof)

% 绘制原始数据和拟合结果
figure;
plot(t, N, 'bo', 'DisplayName', '原始数据');
hold on;
plot(fitresult, 'r-', t, N, 'DisplayName', '拟合结果');
xlabel('时间');
ylabel('数量');
legend;