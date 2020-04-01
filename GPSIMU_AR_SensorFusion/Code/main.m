%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                                                                           
% Main script for the loosely-coupled feedback GNSS-aided INS system. 
%  
% Edit: Isaac Skog (skog@kth.se), 2016-09-01,  
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


%% Load data
disp('Loads data')
%load('GNSSaidedINS_data.mat');
in_data = prepare_data();
%% Load filter settings
disp('Loads settings')
settings=get_settings();

%% Run the GNSS-aided INS
disp('Runs the GNSS-aided INS')
out_data=GPSaidedINS2(in_data,settings);

%% Plot the data 
% disp('Plot data')
% %plot_data(in_data,out_data,'True');drawnow
% figure(1)
% plot(in_data.IMU.t,out_data.x_h(1,:))
% hold on
% plot(in_data.IMU.t,out_data.x_h(2,:))
% hold on
% plot(in_data.IMU.t,out_data.x_h(3,:))
% legend('p_x','p_y','p_z')
% hold off
% 
% figure(2)
% plot(in_data.IMU.t,out_data.x_h(4,:))
% hold on
% plot(in_data.IMU.t,out_data.x_h(5,:))
% hold on
% plot(in_data.IMU.t,out_data.x_h(6,:))
% legend('v_x','v_y','v_z')
% hold off
% 
% figure(3)
% plot(in_data.IMU.t,out_data.x_h(7,:))
% hold on
% plot(in_data.IMU.t,out_data.x_h(8,:))
% hold on
% plot(in_data.IMU.t,out_data.x_h(9,:))
% hold on
% plot(in_data.IMU.t,out_data.x_h(10,:))
% legend('q1','q2','q3','q4')
% hold off
%%
pos = [out_data.x_h(1,:);out_data.x_h(2,:);out_data.x_h(3,:)];
vel = [out_data.x_h(4,:);out_data.x_h(5,:);out_data.x_h(6,:)];
quaternion = [out_data.x_h(7,:);out_data.x_h(8,:);out_data.x_h(9,:);out_data.x_h(10,:)];
writematrix(out_data.x_h','out.csv') 
