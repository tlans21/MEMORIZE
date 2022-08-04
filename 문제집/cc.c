#include<stdlib.h>
#include<stdio.h>

vector<int> arr1;
int N;
int M;
int sum;
int ans = 0;

int search(int left, int right, int ){
    sum = 0;
    ans = 0;
    int center = (left + right) / 2;
    for(int i = 0; i < N; i++){
        if(center > arr1[i]){
            sum += arr1[i];    
        }else{
            sum += center;
        }
    }

    if(ans < sum && sum < M){
        ans = sum;
    }

    search(left, center-1);
    search(center + 1, right);
}

int main(){

    scanf("%d", &N);
    int *arr1 = malloc(sizeof(int) * N);

    for(int i = 0; i < N; i++){
        int num;
        scanf("%d", &num);
        arr1[i] = num;
    }
}