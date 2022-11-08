%% Cinética

close all
clear all


% Trayectoria y Condiciones Iniciales
T = 10; 
Theta1 = pi; 
th10 = 0; 
Theta2 = pi/2; 
th20 = 0;
m1 = 1; 
a1 = 1; m2 = 1; 
a1 = 1; a2 = 1; 
g = 9.81;
con = 2*pi/T;
delth1 = Theta1 - th10; 
delth2 = Theta2 - th20; 
iner21 = m2*a1*a2;

for i = 1:51,
ti (i) = (i-1)*T/50; 
ang = con*ti(i);

%Trayectoria en cada Joint
th1 (i) = th10 + (delth1/T)*(ti (i) - sin(ang)/con);
th1d (i) = delth1*(1 - cos(ang))/T; th1dd (i) = delth1*con*sin(ang)/T; th2 (i) = th20 + (delth2/T)*(ti (i) - sin(ang)/con);
th2d (i) = delth2*(1 - cos(ang))/T; th2dd (i) = delth2*con*sin(ang)/T; thdd = [th1dd(i);th2dd(i)];

%Matriz Inercial
sth2= sin(th2(i)); cth2 = cos(th2(i));
i22= m2*a2*a2/3;
i21= i22 + iner21*cth2/2;
i12= i21;
i11= i22 + m1*a1*a1/3 + m2*a1*a1 + iner21*cth2;
im=[i11, i12; i21, i22];

%Vector H
h1= - (m2*a1*a2*th1d(i) + iner21/2*th2d(i))*th2d(i)*sth2; 
h2= iner21/2*sth2*th1d(i)*th1d(i);

%gamma-vector
hv=[h1;h2]; 
cth1= cos(th1(i)); 
cth12= cos(th1(i) + th2(i));
gam1= m1*g*a1/2*cth1 + m2*g*(a1*cth1 + a2/2*cth12); 
gam2= m1*g*a2/2*cth12; 
gv =[gam1;gam2];

%Joint torque
tau=im*thdd + hv + gv; 
tor1(i) = tau(1); 
tor2(i)=tau(2); 
end

%Gráficas: Posición y Torque
figure(1)
plot(ti,th1)
hold on
plot(ti,th2)
hold off
xlabel('Tiempo [s]')
ylabel('Ángulo [\theta]')
title('Ángulo vs Tiempo')
legend('\theta_{1}','\theta_{2}')
grid on
grid minor

figure(2)
plot (ti, tor1)
hold on
plot(ti,tor2)
hold off
xlabel('Tiempo [s]')
ylabel('\tau [Nm]')
title('Torque vs Tiempo')
legend('\tau_{1}','\tau_{2}')
grid on
grid minor
