#pragma once
#include "DHT.h"
#include "arduino.h"

#define D0 16 //BUTTON
#define D1 5  //UltraSonic Trig
#define D2 4 //PWM //UltraSonic Echo
#define D3 0    //DHT11
#define D4 2    //Humidity
#define D5 14 //PWM
#define D6 12 //PWM
#define D7 13
#define D8 15 //PWM

#define PIN_RX 3
#define PIN_TX 1

#define PIN_BUTTON D0
#define PIN_ULTRASONIC_TRIG D1
#define PIN_ULTRASONIC_ECHO D2
#define PIN_DHT11 D3
#define PIN_HUMIDITY D5

extern DHT dht11;

inline void pins_init(){
    pinMode(PIN_BUTTON, INPUT);
    pinMode(PIN_ULTRASONIC_TRIG, OUTPUT);
    pinMode(PIN_ULTRASONIC_ECHO, INPUT);
    pinMode(PIN_DHT11, INPUT);
    pinMode(PIN_DHT11, PIN_HUMIDITY);
    dht11.begin();
}



