#include "include/includes.h"
#include "include/pins.h"
#include "include/ota.h"
#include "include/network.h"
#include "include/task.h"
#include "include/msg.h"
#include "include/modules.h"



void setup(){
    Serial.begin(9600);
    pins_init();
    tasks_reg();
    connect();

    debug_print("hey");

}

void loop(){
    if(ota_mode){
        ota_loop();
        return;
    }
    task_loop();
    delay(10);

}
