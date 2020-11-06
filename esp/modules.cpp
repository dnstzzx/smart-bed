#include "include/includes.h"
#include "include/modules.h"
#include "include/pins.h"

DHT dht11(PIN_DHT11, DHT11);

int ultrasonic_measure(uint8_t pin_trig, uint8_t pin_echo){
    pin_trig = PIN_ULTRASONIC_TRIG;
    pin_echo = PIN_ULTRASONIC_ECHO;
    int duration, distance;
    digitalWrite(pin_trig, LOW);
    delayMicroseconds(2);
    digitalWrite(pin_trig, HIGH);
    delayMicroseconds(10);
    digitalWrite(pin_trig, LOW);
    duration = pulseIn(pin_echo, HIGH);
    distance = duration * 0.17;
    return distance;
}

bool btn_clicked(uint8_t pin)
{
    return digitalRead(pin);
}

void btn_wait_for_click(uint8_t pin)
{
    while(digitalRead(pin));
    while(!digitalRead(pin));
}

void btn_wait_for_release(uint8_t pin)
{
    while(!digitalRead(pin));
    while(digitalRead(pin));
}

void btn_detect_continous_click(uint8_t pin)
{
    
}

// Humidiy sensor
bool detect_bed_wet(uint8_t pin){
    return digitalRead(pin);
}

// DHT11
void dht11_read(float &temperature, float &humidity){
    temperature = dht11.readTemperature();
    humidity = dht11.readHumidity();

}