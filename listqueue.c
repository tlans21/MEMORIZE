#include<stdio.h>
#include<stdlib.h>

typedef struct node{

    int data;
    struct node* next;
}Node;

typedef struct {
    Node* front;
    Node* rear;
}LqueueType;

LqueueType* createLinkedQueue(void){
    LqueueType* LQ;
    LQ =(LqueueType*)malloc(sizeof(LqueueType));
    LQ->front = NULL;
    LQ->rear = NULL;
    return LQ;
}

int isEmpty(LqueueType* LQ){
    if(LQ->front == NULL){
        return 1;
    }else{
        return 0;
    }
}

void enqueue(LqueueType* LQ, char item){
    Node* new =(Node*)malloc(sizeof(Node));
    //새로운 노드 생성
    new->data = item;
    new->next = NULL;

    if(isEmpty(LQ)){
        //front, rear 노드포인터를 새로 생성한 노드로 가리킴.
        LQ->front = new;
        LQ->rear = new;
    }else{
        LQ->rear->next = new;
        LQ->rear = new;
    }
}

char dequeue(LqueueType* LQ){
    //삭제할 노드 확인

    if(LQ->front == NULL){
        return 0;
    }else{
    //Old라는 노드 생성후 front와 old가 동일하게 가리키게한다.
    Node* old = (Node*)malloc(sizeof(Node));

    old = LQ->front;
    int item = LQ->front->data;
    }
}