#pragma once

inline void go_wrong(){
    Serial.println("something went wrong");
    ota_setup();
}

inline void assert(bool condition){
    if(!condition) go_wrong();
}

inline String json_msg_wrap(String msg){
    
    msg.replace("\"", R"(\")");
    String line = R"({"value:",")" + msg + "\"}";
    return line;
}