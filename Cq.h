#pragma once
#define Q_SIZE 4

typedef char element;

typedef struct{
    element queue[Q_SIZE];
    int front;
    int rear;
}CircleQueue;

CircleQueue* createQueue(void);
int isQueueEmpty(CircleQueue* q);
int isQueueFull(CircleQueue* q);
void enQueue(CircleQueue* q, element item);
element deQueue(CircleQueue* q);
element peekCQ(CircleQueue* q);
void printCQ(CircleQueue* q);
