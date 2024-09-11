data = [0.548593357
0.538769024
0.542049874
0.551094349
0.550641191
0.558269676
0.552635417
0.570844794
0.570844794
0.547825771
];
hold on;
x = 1:10;
plot(x,data);
plot(x,aaa(x) - 0.005);
xlabel('Time');
ylabel('Benifit');
legend('Benifit','Fitted')