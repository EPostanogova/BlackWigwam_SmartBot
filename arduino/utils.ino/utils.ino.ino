#include "DHT.h"
#define DHTPIN 4 
DHT dht(DHTPIN, DHT11);
void setup() {
   Serial.begin(115200);
   dht.begin();
}
void get_temperature() {
   
  delay(2000);
  float t = dht.readTemperature();
  String T=String(t);
  String msg = String("Температура:" + T +"*C");
  Serial.println(msg);
}

void get_humidity() {
   
  delay(2000);
  float h = dht.readHumidity();
  Serial.print(h);
  String H=String(h);
  String msg = String("Влажность:" + H +"%\t");
  Serial.println(msg);
}

void echo(){
 if (Serial.available() > 0) { 
  String msg =Serial.readString();
  Serial.println(msg);
}
}
void loop() {
  //echo();
  get_temperature();
  get_humidity();

}
