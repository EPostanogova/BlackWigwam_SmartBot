 
void setup() {
   Serial.begin(115200);
   
}
void echo(){
  
 if (Serial.available() > 0) { 
  String msg =Serial.readString();
  Serial.println(msg);
   
  
}
}
void loop() {
  echo();

}
