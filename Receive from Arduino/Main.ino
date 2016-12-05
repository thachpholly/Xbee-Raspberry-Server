#include <SoftwareSerial.h>
   
String data = "(This is my program)";
int lastStringLength;
int i;
byte charIdControl = 101;
SoftwareSerial xBee(2, 3); // RX, TX
      
void setup()
{
     Serial.begin(9600);          //enable the hardware serial port
     xBee.begin(9600);    
  }    
void loop(){
  
  if (xBee.available()) {

      //to check value recieving to be a first value list
      byte charControl = xBee.read();
      
      if (charControl == charIdControl) { 
          sendStatus(data);                                  
      }
  }
  
 }  

void sendStatus(String data) {
  lastStringLength = data.length();

  for(i = 0; i < lastStringLength; i++)
  {
     xBee.write(data.charAt(i));
     Serial.print(data.charAt(i));
    }
    Serial.println("");
}
