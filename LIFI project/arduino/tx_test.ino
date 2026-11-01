//tranmitter code
#define LED_PIN 5
#define PERIOD 180

String base64String = "";

void setup() {
  Serial.begin(115200);
  pinMode(LED_PIN, OUTPUT);
  digitalWrite(LED_PIN, HIGH);
}

void loop() {
  // Receive Base64 data over serial
  while (Serial.available() > 0) {
    char c = Serial.read();
    if (c == '#') {  // end marker received
      base64String += c;
      transmitData();
      base64String = "";
      delay(2000);
    } else {
      base64String += c;
    }
  }
}

void transmitData() {
  for (int i = 0; i < base64String.length(); i++) {
    sendByte(base64String[i]);
  }
}

void sendByte(char b) {
  digitalWrite(LED_PIN, LOW);
  delayMicroseconds(PERIOD);

  for (int i = 0; i < 8; i++) {
    digitalWrite(LED_PIN, (b >> i) & 1);
    delayMicroseconds(PERIOD);
  }

  digitalWrite(LED_PIN, HIGH);
  delayMicroseconds(PERIOD);
}