#include<stdio.h>
#include<stdlib.h>

typedef struct{
    int heap_size;
    int heap[100];
}heapType;

heapType* create;

void insertHeap(heapType* h, int item){
    int i;
    h->heap_size = h->heap_size + 1;
    i = h->heap_size;

    while(i != 1 && item > h->heap[i/2]){
        h->heap[i] = h->heap[i/2]; // 자식노드의 값을 부모 노드의 값으로 변환
        i = i / 2; // 자식노드의 인덱스를 부모 노드 인덱스로 변환
    }
    h->heap[i] = item;
}

int deleteHeap(heapType *h){
    int item;
    int temp;
    int parent;
    int child;

    item = h->heap[1];
    temp = h->heap[h->heap_size];
    h->heap_size = h->heap_size - 1;
    parent = 1;
    child = 2;

    while(child <= h->heap_size){
        if((child < h->heap_size)&& (h->heap[child]) < h->heap[child + 1]){
            //부모 노드의 오른쪽, 왼쪽 자식노드의 크기를 비교합니다. 그 중에서 큰 자식 노드를 고릅니다.
            //나중에 temp에 저장된 키와 비교할 때 큰 키 노드를 고르면, 큰 노드와 작은 노드와 비교하는 일 두 번해야 할 일을 한 번으로 덜어주기 때문입니다.
            child++;
        }
        if(temp>= h->heap[child]){
            break;
        }else{
            h->heap[parent] = h->heap[child];
            parent = child;
            child = child * 2;
        }
    }
    h->heap[parent] = temp;
    return item;
}

