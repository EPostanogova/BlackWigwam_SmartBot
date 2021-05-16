#include "DHT.h"
#define DHTPIN 4 
DHT dht(DHTPIN, DHT11);
void setup() {
   Serial.begin(115200);
   dht.begin();
}
String get_temperature() {
   
  delay(3000);
  float t = dht.readTemperature();
  String T=String(t);
  return(T);
}

String get_humidity() {
   
  delay(3000);
  float h = dht.readHumidity();
  String H=String(h);
  return(H);
  
  
}

void echo(){
 if (Serial.available() > 0) { 
  String msg =Serial.readString();
  Serial.println(msg);
}
}
void loop() {
  //echo();
 
  String msg = Serial.readString();
  if (msg ='h'){
    Serial.println(get_humidity());
  }
  if (msg ='t'){
    Serial.println(get_temperature());
  }
}
