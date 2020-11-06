#pragma once
#include "task.h"

void deal_msg(const String &msg);
void receive_and_deal_msgs(Task *task);

void debug_print(const char *msg);
void debug_print(String &msg);
void debug_print(unsigned long n, uint8_t base=10);
void debug_print(double number, uint8_t digits);