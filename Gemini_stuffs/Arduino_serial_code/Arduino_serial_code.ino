#define LEDPIN 2
void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  pinMode(LEDPIN, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available()) {

    String input = Serial.readStringUntil('\n');
    input.trim();
      input=="ON"? digitalWrite(LEDPIN, HIGH) : digitalWrite(LEDPIN, LOW);
  }
  
}
