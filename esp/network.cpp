#include "include/network.h"

bool wifi_connected;
bool cloud_connected;

Http_Result http_get(HTTPClient& http, String &path){
    String url = String("http://") + REMOTE_IP + "/" + path;
    http.begin(url);
    Http_Result result;
    result.status_code = http.GET();
    if (result.status_code == 200) {
        const String *payload = &http.getString();
        result.payload = payload;
    }
    return result;
}

Http_Result http_get(HTTPClient& http, const char *path){
    String p = String(path);
    return http_get(http,p);
}

Http_Result http_post(HTTPClient& http, String &path,String &payload){
    String url = String("http://") + REMOTE_IP + "/" + path;
    http.begin(url);
    Http_Result result;
    result.status_code = http.POST(payload);
    if (result.status_code == 200) {
        const String *payload = &http.getString();
        result.payload = payload;
    }
    return result;
}

Http_Result http_post(HTTPClient& http, const char *path,String &payload){
    String p = String(path);
    return http_post(http, p, payload);
}

bool connect(){
    WiFi.mode(WIFI_STA);
    IPAddress local_ip(LOCAL_IP), getway(GETWEY), netmask(SUB_NET_MASK);

    WiFi.config(local_ip, getway, netmask);
    while(true){
        WiFi.begin(WIFI_SSID, WIFI_PASSWD);
        if(WiFi.waitForConnectResult() == WL_CONNECTED) break;
        delay(10000);
    }
    wifi_connected = true;

    delay(5000);

    HTTPClient http;
    Http_Result result = http_get(http, "hello");
    cloud_connected = result.status_code == 200 && *result.payload == "hello";
    http.end();
    
    result = http_get(http, "pop_msgs/esp");// 清空以前信息
    http.end();

}

