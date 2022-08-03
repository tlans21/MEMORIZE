#include<stdio.h>
#include<stdlib.h>

typedef struct graphType{
    int n;
    int adjMatrix[30];
}graphType;

void createGraph(graphType* g);
void insertVertex(graphType* g, int v);
void insertEdge(graphType* g, int u, int v);

void createGraph(graphType* g){
    int i;
    int j;
    g->n = 0;
    for(int i = 0; i < 30; i++){
        for(int j = 0; j < 30; j++){
            g->adjMatrix[i][j] = 0;
        }
    }
}

void insertVertex(graphType* g, int v){
    if(((g->n)+1) > 30){
        return;
    }
    if(v < (g->n)){
        return;
    }
    g->n++;
}

void insertEdge(graphType* g, int u, int v){
    if(u >= g->n || v>=g->n){
        return;
    }
    g->adjMatrix[u][v] = 1;    
}

void print_adjMatrix(graphType* g){
    int i;
    int j;
    for(int i =0; i < (g->n); i++){
        for(int j = 0; j < (g->n); j++){
            printf("%2d", g->adjMatrix[i][j]);
        }
    }
}