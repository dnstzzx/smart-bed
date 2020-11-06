#pragma once
#include "includes.h"
#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>

#include "wifi_info.h"

#ifndef HEADER_WIFI_INFO
#define WIFI_SSID "WE_ARE_THE_CHAMPION"
#define WIFI_PASSWD "PASSWD"
#endif


#define GETWEY 192,168,43,1
#define SUB_NET_MASK 255,255,255,0

#define LOCAL_IP 192,168,43,168

#define REMOTE_IP "192.168.43.195:5000"

typedef struct{
    int status_code;
    const String *payload;
}Http_Result;

extern bool wifi_connected;
extern bool cloud_connected;

typedef HTTPClient Http;

bool connect();

Http_Result http_get(HTTPClient& http, String &path);
Http_Result http_get(HTTPClient& http, const char *path);
Http_Result http_post(HTTPClient& http, String &path, String &payload);
Http_Result http_post(HTTPClient& http, const char *path, String &payload);

