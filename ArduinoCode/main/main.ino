
#include "BluetoothSerial.h"
#include <string.h>
#if !defined(CONFIG_BT_ENABLED) || !defined(CONFIG_BLUEDROID_ENABLED)
#error Bluetooth is not enabled! Please run `make menuconfig` to and enable it
#endif




BluetoothSerial SerialBT;



int arr[512] = {0};
void setup() {
  Serial.begin(9600);
  SerialBT.begin("ESP32test"); //Bluetooth device name
  pinMode(13, OUTPUT);
  

}

void loop() {

  bool sent = false;

  if(Serial.available() > 0)
  {
    
    int numBytes = Serial.available();    
    Serial.readBytes(arr, numBytes);
    int bytesWritten = SerialBT.write(arr, numBytes);

    Serial.print(bytesWritten);
 }


}
