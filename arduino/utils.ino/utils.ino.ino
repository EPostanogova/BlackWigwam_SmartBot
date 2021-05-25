#include "DHT.h"
#define DHTPIN 4 
#define CONPIN 5

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
void con(){
  String msg =Serial.readString();
  if (digitalRead(CONPIN)==0){
    Serial.println("open");
   if (digitalRead(CONPIN)==1) {
      Serial.println("close");
    }
    }
  }


void echo(){
 if (Serial.available() > 0) { 
  String msg =Serial.readString();
  Serial.println(msg);
}
}
void loop() {
  String msg =Serial.readString();
  if (msg.equals("h")){
   Serial.println(get_humidity());
 }
   else if (msg.equals("t")){
    Serial.println(get_temperature());
 }
 else if (msg.equals("c")) {
    con();
 }
 }
