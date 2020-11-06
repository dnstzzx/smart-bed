#include "include/task.h"
#include <stdlib.h>
#include <string>

/*
typedef struct{
    bool enabled;
    const String name;
    void (* func)(struct Task*);

    unsigned long interval;  //in ms
    unsigned long last_call;
}Task;

*/

Task *task_pool[TASK_POOL_SIZE];
int task_count = 0;


bool add_task(Task *task){
    task_pool[task_count] = task;
    task_count ++;
}
void task_loop(){
    unsigned long now = 0;
    for(int i=0;i<task_count;i++){
        now = millis();
        Task* task = task_pool[i];
        if(now >= task->interval + task->last_call){
            task->func(task);
            now = millis();
            task->last_call = now;
        }
    }
}
