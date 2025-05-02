#include <Wire.h>
#include <WiFi.h>
#include <HTTPClient.h>

// Configuración
#define I2C_SLAVE_ADDR 0x08
#define SENSOR_PIN 34 // LM35 conectado a GPIO34

const char* ssid = "FAMILIA NINO ARDILA_2.4GHz";
const char* password = "#Luisa1128";
String apiKey = "4BCFW5PPP3RJYZDZ";

unsigned long lastSendTime = 0;
const unsigned long sendInterval = 30000; // 30 segundos

float lastTemperature = 0;

// Prototipo
void sendToThingSpeak(float temperature);

void setup() {
  Serial.begin(115200);

  // I2C como esclavo
  Wire.begin((uint8_t)I2C_SLAVE_ADDR);
  Wire.onRequest(onRequest);

  // Leer temperatura inicial para evitar que sea 0
  int raw = analogRead(SENSOR_PIN);
  float voltage = raw * (3.3 / 4095.0);
  lastTemperature = voltage * 100.0;

  // Conexión WiFi
  Serial.println("Conectando a WiFi...");
  WiFi.begin(ssid, password);

  int attempts = 0;
  while (WiFi.status() != WL_CONNECTED && attempts < 30) {
    delay(500);
    Serial.print(".");
    attempts++;
  }

  if (WiFi.status() == WL_CONNECTED) {
    Serial.println("\nWiFi conectado");
  } else {
    Serial.println("\nERROR: No se pudo conectar a WiFi");
  }
}

void loop() {
  // Leer LM35
  int raw = analogRead(SENSOR_PIN);
  float voltage = raw * (3.3 / 4095.0);   // ADC 12 bits, 3.3V
  float temperature = voltage * 100.0;    // LM35 entrega 10 mV/°C
  lastTemperature = temperature;

  Serial.print("Temperatura LM35: ");
  Serial.print(temperature);
  Serial.println(" °C");

  // Enviar a ThingSpeak cada 30s
  if (millis() - lastSendTime > sendInterval && WiFi.status() == WL_CONNECTED) {
    sendToThingSpeak(temperature);
    lastSendTime = millis();
  }

  delay(500);
}

// Enviar al Arduino Uno por I2C cuando lo solicita
void onRequest() {
  int tempInt = int(lastTemperature);
  Wire.write(tempInt);
  Serial.print("I2C: Enviando a master -> ");
  Serial.println(tempInt);
}

// Función para enviar a ThingSpeak
void sendToThingSpeak(float temperature) {
  HTTPClient http;
  String url = "http://api.thingspeak.com/update?api_key=" + apiKey + "&field1=" + String(temperature, 2);

  http.begin(url);
  int httpCode = http.GET();

  if (httpCode > 0) {
    Serial.println("Dato enviado a ThingSpeak.");
  } else {
    Serial.print("Error al enviar: ");
    Serial.println(httpCode);
  }

  http.end();
}
