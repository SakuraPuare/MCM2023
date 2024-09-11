p0=0.5;
k=30;
r=5;
a=0.05; 
t=0:0.1:25;

p_u=a*k*p0*exp(a*r*t);
p_l=a*k+p0*(exp(a*r*t)-1);

p=p_u./p_l/a;
plot(t,p);
xlabel('time/year');
ylabel('w(t)');
title('weight-time');
