
void setup() {
   Serial.begin(115200);
   
}
void echo(){
  
 if (Serial.available() > 0) { 
  String msg =Serial.readString();
  Serial.print(msg);

  
}
}
void loop() {
echo();

}
