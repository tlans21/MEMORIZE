#include<iostream>
#include<vector>
#include<cmath>
using namespace std;
vector<int> a;
vector<int> b[11];

int K;

void findtree(int left, int right, int depth){
    if(depth == K){
        return;
    }
    if(left == right){
        b[depth].push_back(a[left]);
        return;
    }
    int center = (left + right) / 2;
    b[depth].push_back(a[center]);
    findtree(left , center - 1, depth + 1);
    findtree(center + 1, right, depth + 1);
}

int main(){
    int num;
    cin>>K;

    int size = pow(2, K) - 1;

    for(int i = 0; i < size; i++){
        cin>>num;
        a.push_back(num); // num 배열에 저장
    }

    findtree(0, a.size(), 0);

    for(int i = 0; i < K; i++){
        for(int j = 0; j < b[i].size(); j++){
            cout<<b[i][j]<<" ";
        }
        cout<< endl;
    }
    return 0;
}