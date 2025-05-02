# Two-levels-controller

## Sistema IoT de Monitoreo de Temperatura – ESP32 + Arduino Uno

Este proyecto implementa un sistema de monitoreo de temperatura basado en un sensor LM35 conectado a un ESP32. El ESP32 actúa como esclavo I2C y transmite la temperatura al Arduino Uno (maestro), que enciende un LED si supera un umbral crítico (30 °C). Además, el ESP32 se conecta a WiFi y publica los datos en tiempo real en ThingSpeak para visualización remota.

###Tecnologías usadas:
- I2C entre ESP32 y Arduino Uno
- Sensor LM35
- WiFi con ESP32
- Plataforma ThingSpeak

