clc
clear all
close all

write_api_key = 'MLPMZRWLP46PA76S';
channelId = 1794957
data = [1 2 3 4];
thingSpeakWrite(channelId, 'Fields', 1, 'Values', data, 'WriteKey', write_api_key);
% thingSpeakWrite(channelId, ,"Fields", 1,"Values",data ,'WriteKey',  write_api_key);
