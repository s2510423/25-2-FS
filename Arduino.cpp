void setup() {
  Serial.begin(115200);
}

void loop() {
  int rawValue = analogRead(A0);
  Serial.println(rawValue);
  delay(1); 
}