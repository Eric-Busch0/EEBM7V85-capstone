clc 
clear all
close all


comport = 'COM6';
data = 1 : 180;
data = data.*2;
disp(data)

esp = serialport(comport, 9600, "FlowControl","none");
%The esp32 dev board has hardware has some flow control connected to the
%reset line. So whenever the socket to the esp gets opened it toggles the
%reset hence resetting the board and killing any bluetooth connection so
%this is the easiest way to deal with it.
disp('10 Seconds to connect')
pause(10);

disp('Writing data')

while true
write(esp, data, "uint8");
pause(1)
end
x = read(esp, 1, "char");
disp(x);
delete(esp);
