#include<stdio.h>
#include<stdlib.h>
#define MAX 100
typedef char element;
typedef struct{
    element queue_size[100];
    int front;
    int rear
}queue_type;

queue_type* createQueue(void);
int isqueueEmpty(queue_type* q);
int isqueuefull(queue_type* q);
void enqueue(queue_type* q, element item);
element dequeue(queue_type* q);
element peekq(queue_type* q);

queue_type* createQueue(void){
    queue_type *q;
    q->front = 0;
    q->rear = 0;
    return q;
}

int isqueueEmpty(queue_type * q){
    if(q->front == q->rear){
        return 1;
    }else{
        printf("현재 원형 큐가 비어있지 않습니다.");
        return 0;
    }
}

int isqueuefull(queue_type* q){
    if(q->front == (q->rear + 1) % 100){
        return 1;
    }else{
        printf("현재 원형 큐가 전부 채워져있습니다.");
        return 0;
    }
}

void enqueue(queue_type* q, element item){
    if(isqueuefull(q)){
        return;
    }else{
    q->rear = (q->rear+1) % 100;
    q->queue_size[q->rear] = item;
    }
}

element dequeue(queue_type* q){
    if(isqueueEmpty(q)){
        return;
    }else{
        q->front = (q->front+1)%100;
        return q->queue_size[q->front];
    }
}

element peekq(queue_type* q){
    if(isqueueEmpty(q)){
        return;
    }else{
        return q->queue_size[(q->front+1)%100];
    }
}

void printQ(queue_type* q){
    int i;
    int first;
    int last;

    first = (q->front+1)%100;
    last = (q->rear + 1)%100;

    i = first;
    printf("[");
    while(i != last){
        printf("%3c", q->queue_size[i]);
        i = (i+1)%100;
    }
    printf("]");
}
