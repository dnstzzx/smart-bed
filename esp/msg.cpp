#include "include/network.h"
#include "include/msg.h"
#include "include/ota.h"
#include "include/utils.h"
#include "cstring"
#include "include/state.h"
#include "include/task.h"

Sensor_State sensor_state;

void deal_msg(const String &msg){
    debug_print("message resceived: " + msg);
    if(msg == "ota"){
        debug_print("entering ota mode...");
        ota_setup();
    }else if(msg == "rst"){
        debug_print("restarting...");
        ESP.restart();
    }
}

void receive_and_deal_msgs(Task *task){
    while (true){
        HTTPClient http;
        // 检查数量
        Http_Result result = http_get(http, "msg_count/esp");
        assert(result.status_code == 200);
        int count = atoi((*result.payload).c_str());
        http.end();
        if(count == 0) return;
        // 处理
        for(int i=0;i<count;i++){
            HTTPClient http1;
            Http_Result result1 = http_get(http1, "pop_msg/esp");
            assert(result1.status_code == 200);
            deal_msg(*result1.payload);
            http1.end();
        }
    }
}

void debug_print(String &msg){
    String line = String("[Debug] :") + msg;
    Serial.println(line);
    if(cloud_connected){
        Http http;
        http_post(http, "send_msg/cloud", line);
    }
}

void debug_print(const char *msg){
    String line = String("[Debug] :") + msg;
    Serial.println(line);
    if(cloud_connected){
        Http http;
        http_post(http, "send_msg/cloud", line);
    }

}

void debug_print(unsigned long n, uint8_t base) {
    char buf[8 * sizeof(long) + 1]; // Assumes 8-bit chars plus zero byte.
    char *str = &buf[sizeof(buf) - 1];

    *str = '\0';

    // prevent crash if called with base == 1
    if(base < 2)
        base = 10;

    do {
        unsigned long m = n;
        n /= base;
        char c = m - base * n;
        *--str = c < 10 ? c + '0' : c + 'A' - 10;
    } while(n);

    debug_print(str);
}

void debug_print(double number, uint8_t digits) {
    char buf[40];
    debug_print(dtostrf(number, 0, digits, buf));
}