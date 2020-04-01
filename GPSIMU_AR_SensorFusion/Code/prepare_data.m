function [in_data] = prepare_data()
T= readtable('walking20sec.csv'); %To read the type of sensor
sensor_type = T.Var2;
clear T;
T = readmatrix('walking20sec.csv');
isequal(sensor_type(1),{'ACC'});
N = length(sensor_type);

time_start = T(1,1);

in_data.IMU.t = [];
in_data.IMU.acc= [];
in_data.IMU.gyro= [];
in_data.GNSS.t= [];
in_data.GNSS.pos_ned = [];

for i = 1:N
    if isequal(sensor_type(i),{'ACC'})
       % in_data.IMU.t = [in_data.IMU.t; T(i,8)];
       in_data.IMU.t = [in_data.IMU.t; (T(i,1)-time_start)/1000];
        in_data.IMU.acc = [in_data.IMU.acc  T(i,3:5)'];
    elseif isequal(sensor_type(i),{'GYR'})
        in_data.IMU.gyro = [in_data.IMU.gyro  T(i,3:5)']; %time truncated
    elseif isequal(sensor_type(i),{'GPS'})
        %in_data.GNSS.t = [in_data.GNSS.t; T(i,8)];
        in_data.GNSS.t = [in_data.GNSS.t; (T(i,1)-time_start)/1000];
        in_data.GNSS.pos_ned = [in_data.GNSS.pos_ned  T(i,3:5)'];
    end
end
end