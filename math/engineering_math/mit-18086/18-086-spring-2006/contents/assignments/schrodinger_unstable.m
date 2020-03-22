%2006 srping 18.086 TA Yeunwoo Cho
%HW2-(2) Explicit Method
L=10;
dx=0.1;
dt=0.05;
x=[-L+dx:dx:L-dx];
%Initial value
y=exp(-x.^2)/(pi^0.25);

n=length(x);


R=dt/(dx^2);
xx=x';
u=y';
%algorithm
A_su=sparse(diag(R*i*ones(n-1,1),1)+...
             diag((1+2*i*R)*ones(n,1))+...
             diag(R*i*ones(n-1,1),-1));
         
plot(xx,real(u));
hold on;
for t=dt:dt:7
    u=A_su*u;
    if fix(t)==t;
        plot(xx,real(u))
        axis([-10 10 0 1.1]);
    end
end
xlabel('position')
ylabel('u(x,t)')
title('Explicit method')
hold off