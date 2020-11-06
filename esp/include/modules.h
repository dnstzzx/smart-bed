#pragma once

#include "includes.h"
#include "pins.h"


//Button functions
bool btn_clicked(uint8_t pin=PIN_BUTTON);
void btn_wait_for_click(uint8_t pin=PIN_BUTTON);
void btn_wait_for_release(uint8_t pin=PIN_BUTTON);
void btn_detect_continous_click(uint8_t pin=PIN_BUTTON);

//Ultrasonic sensor
int ultrasonic_measure(uint8_t pin_trig=PIN_ULTRASONIC_TRIG, uint8_t pin_echo=PIN_ULTRASONIC_ECHO);
/*  ultrasonic sensor measure
    @returns: distance(mm)
*/

// Humidiy sensor
bool detect_bed_wet(uint8_t pin=PIN_HUMIDITY);

// DHT11
void dht11_read(float &temperature, float &humidity);