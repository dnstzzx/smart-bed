#pragma once
struct Sensor_State{
    int temperature = 0;
    int humidity = 0;
    bool bed_wet = false;
    bool baby_outbed = false;
};

extern Sensor_State sensor_state;
