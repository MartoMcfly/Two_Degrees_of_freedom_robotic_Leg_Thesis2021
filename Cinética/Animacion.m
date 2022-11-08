%% Animacion

%Condiciones
t=0:0.1:2;
tmax=2;

%Solución
DinamicaDirecta=zeros(2,length(t));
DinamicaInversa=[];

%Condiciones Geométricas
L1=1;
L2=1;
Q1=0-70*(10*(t/tmax).^3 -15*(t/tmax).^4 +6*(t/tmax).^5);
Q2=0-15*(10*(t/tmax).^3 -15*(t/tmax).^4 +6*(t/tmax).^5);
Lx=L1*cosd(Q1);
Ly=L1*sind(Q1);
Lim=L1+L2+0.2;

for i=1:length(t)
    [DinamicaDirecta(:,i)]=Cinematica(L1,L2,Q1(i),Q2(i));
end

plot(0,0,'^')
hold on
plot(Lx,Ly,'o')
plot(DinamicaDirecta(1),DinamicaDirecta(2),'*')
hold off
axis([-Lim Lim -Lim Lim])