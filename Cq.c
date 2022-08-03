#include<stdio.h>
#include<stdlib.h>
#include "Cq.h"

CircleQueue* createQueue(void){
    CircleQueue* q;
    q = (CircleQueue*)malloc(sizeof(CircleQueue));
    q->front = 0;
    q->rear = 0;
    return q;
}

int isQueueEmpty(CircleQueue* q){
    if(q->front == q->rear){
        printf("해당 원형 큐는 비어있다.");
        return 1;
    }
    else{
        return 0;
    }
}

int isQueueFull(CircleQueue* q){
    if(((q->rear+1) % Q_SIZE) == q->front){
        print("해당 원형 큐는 완전히 채워져 있다.");
        return 1;
    }
    else return 0;
}
void enQueue(CircleQueue* q, element item){
    if(isQueueFull(q)){
        return;
    }else{
    q->rear = (q->rear + 1) % Q_SIZE;
    q->queue[q->rear] = item;
    }
}
element deQueue(CircleQueue* q){
    if(isQueueEmpty(q)){
        return;
    }else{
        q->front = (q->front + 1)% Q_SIZE;
        return q->queue[q->front];
    }
}
element peekCQ(CircleQueue* q){
    if(isQueueEmpty(q)){
        return;
    }else{
        return q->queue[q->front + 1 %Q_SIZE];
    }
}
void printCQ(CircleQueue* q){
    int i;
    int first;
    int last;
    first = (q->front+1) % Q_SIZE;
    last = (q->rear + 1) % Q_SIZE;
    printf("원형 큐 [");
    i = first;
    while(i != last){
        printf("%3c", q->queue[i]);
        i = (i+1) % Q_SIZE;
    }
    printf("]");
}


