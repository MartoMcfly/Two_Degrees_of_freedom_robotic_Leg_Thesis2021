%% Cinematica
function [Dd] = Cinematica(L1,L2,Q1,Q2)

%Dinámica Directa
Px=L1*cosd(Q1)+L2*cosd(Q1+Q2);
Py=L1*sind(Q1)+L2*sind(Q1+Q2);
Dd=[Px,Py]';


%Dinámica Inversa
% FI=@(x) [L1*cosd(x(1))+L2*cosd(x(1)+x(2))-Px;
%          L1*sind(x(1))+L2*sind(x(1)+x(2))-Py];
% CI=[0;0];
% R=fsolve(FI,CI);
% Di=[R(1),R(2)];
end
