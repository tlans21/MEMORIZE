#include<stdio.h>
#include<stdlib.h>

#define Q_SIZE 6


typedef struct{
    char queue[Q_SIZE];
    int front;
    int rear;
}CircleQueue;



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
        printf("해당 원형 큐는 완전히 채워져 있다.\n");
        return 1;
    }
    else return 0;
}
void enQueue(CircleQueue* q, char item){
    if(isQueueFull(q)){
        return;
    }else{
    q->rear = (q->rear + 1) % Q_SIZE;
    q->queue[q->rear] = item;
    }
}
char deQueue(CircleQueue* q){
    if(isQueueEmpty(q)){
        return -1;
    }else{
        q->front = (q->front + 1)% Q_SIZE;
        return q->queue[q->front];
    }
}
char peekCQ(CircleQueue* q){
    if(isQueueEmpty(q)){
        return 0;
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

int main(void){
    CircleQueue* q =createQueue();
    char data;
    printf("원형 큐 연산 프로그램\n");
    printf("데이터 삽입\n");
    printf("\n 삽입A>>");
    enQueue(q, 'A');
    printCQ(q);
    printf("\n 삽입B>>");
    enQueue(q, 'B');
    printCQ(q);
    printf("\n 삽입C>>");
    enQueue(q, 'C');
    printCQ(q);
    printf("\n 삽입D>>");
    enQueue(q, 'D');
    printCQ(q);
    printf("\n 삽입E>>");
    enQueue(q, 'E');
    printCQ(q);
    printf("\n 삽입F>>");
    enQueue(q, 'F');
    data = peekCQ(q); printf("peek item : %c \n", data);
    printf("\n 삭제>>");
    data = deQueue(q);
    printCQ(q);
    printf("\n 삭제>>");
    data = deQueue(q);
    printCQ(q);
    printf("\n 삭제>>");
    data = deQueue(q);
    printCQ(q);
    printf("\n 삭제>>");
    data = deQueue(q);
    printCQ(q);
    printf("\n 삭제>>");
    data = deQueue(q);
    printCQ(q);
    data = deQueue(q);

    printf("\n");
    printf("\n");
    printf("\n");
    printf("\n");
    printf("\n 1819054 천시문");

    return 0;

}