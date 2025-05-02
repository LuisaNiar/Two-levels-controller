#include <Wire.h>

#define I2C_SLAVE_ADDR 0x08
#define LED_PIN 2

void setup() {
  Wire.begin();           // Iniciar como master
  Serial.begin(9600);
  pinMode(LED_PIN, OUTPUT);
  digitalWrite(LED_PIN, LOW);
}

void loop() {
  Wire.requestFrom(I2C_SLAVE_ADDR, 1);  // Pedir 1 byte al esclavo

  if (Wire.available()) {
    int temperature = Wire.read();     // Leer temperatura enviada
    Serial.print("Temperatura recibida: ");
    Serial.println(temperature);

    if (temperature > 30) {
      digitalWrite(LED_PIN, HIGH);
    } else {
      digitalWrite(LED_PIN, LOW);
    }
  }

  delay(1000);
}
