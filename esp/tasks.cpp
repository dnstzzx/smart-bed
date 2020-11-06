#include "include/includes.h"
#include "include/task.h"
#include "include/network.h"
#include "include/msg.h"
#include "include/modules.h"
#include "include/state.h"


void update_dht(Task *task){
    float t, h;
    dht11_read(t, h);
    int distance = ultrasonic_measure();
    sensor_state.temperature = t;
    sensor_state.humidity = h;
    sensor_state.baby_outbed = distance <= 400;
}

void upload_state(Task *task){
    String line = "{\"temperature\":";
    line += sensor_state.temperature;
    line += ",\"humidity\":";
    line += sensor_state.humidity;
    line += ",\"bed_wet\":";
    line += sensor_state.bed_wet ? "true":"false";
    line += ",\"baby_outbed\":";
    line += sensor_state.baby_outbed ? "true}":"false}";
    //debug_print("upload state dict");
    //debug_print(line);
    Http http;
    Http_Result result = http_post(http, "sensor_state", line);
    //debug_print(String("status code: ") + result.status_code);
    
}

void tasks_reg(){
    add_task(init_task("msg", receive_and_deal_msgs, 1000));
    add_task(init_task("update_sensor_state", update_dht, 1000));
    add_task(init_task("upload_state", upload_state, 500));
}