T = 0:25; % 创建温度向量
B = 100./(1+exp(10-0.2*T)); % 计算对应的生物量向量

plot(T, B); % 绘制生物量和温度之间的关系图像
xlabel('Temperature');
ylabel('Biomass');

set(gca,'xtick',[],'xticklabel',[]);
set(gca,'ytick',[],'yticklabel',[])