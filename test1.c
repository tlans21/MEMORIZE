#include<stdio.h>
#include<stdlib.h>

typedef struct node{
    int data;
    struct node* next;
}Node;

Node *front = NULL;
Node *rear = NULL;

int main(){
    Node* new = (Node*)malloc(sizeof(Node));
    int item;
    scanf("%d", &item);
    new->data = item;
    new->next = NULL;

    rear = new;
    front = new;

    printf("%d", rear->data);
    return 0;
}