%%% %%% TASKS %%% %%%
clc;clear
%%% Task 1
lat_lund = 55.706;
lat_stok = 59.334;
lat = lat_stok;
error_growth
pos_stok = pos;
lat = lat_lund;
error_growth;
pos_lund = pos;
figure()
plot(t, (pos_stok(3,:)-pos_lund(3,:))')
[r,m,b] = regression(t3,pos_lund(2,:))
t3 = t.^3;
figure()
plot(t, abs(pos_lund(2,:)-m*t.^3+b))
grid on
ylabel('Modeling aboslute error of the position error modeling [m]')
xlabel('Time [s]')

%%%% Task 2



