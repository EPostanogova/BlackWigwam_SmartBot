void setup() {
   Serial.begin(115200);
   
}

void loop() {
String msg=Serial.readString();
 Serial.print(msg);

}
