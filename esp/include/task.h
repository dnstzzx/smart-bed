#pragma once
#include "includes.h"

#define TASK_POOL_SIZE 30

struct Task{
    bool enabled;
    String name;
    void (* func)(Task*);

    unsigned long interval;  //in ms
    unsigned long last_call;
};

extern Task *task_pool[];

inline Task *init_task(const String name,void (* func)(Task*), unsigned long interval){
    Task *task = (Task*)malloc(sizeof(Task));
    task->enabled = true;
    task->name = name;
    task->func = func;
    task->interval = interval;
    task->last_call = 0;
    return task;
}

bool add_task(Task *task);
void task_loop();
void tasks_reg();
