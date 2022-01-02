#include<iostream>
#include<queue>
#include<cstring>

using namespace std;

int T;
char spell[4] = {'D','S','L','R'};
int N;
int M;
int visited[10001];

int dslr(int order, int n){
    if(order == 0){
        return (n * 2) % 10000;
    }
   else if(order == 1){
       if(n == 0){
           return 9999;
       }else{
           return n - 1;
       }
   }
   else if(order == 2){
       int minus = n / 1000;
       n -=minus*1000;
       n *=10;
       n +=minus;
       return n;
   }
   else if(order == 3){
       int plus = n % 10;
       n /= 10;
       n += plus *1000;
       return n;
   }
}

void bfs(){
    queue<pair<int, string>> q;
    q.push({N,""});
    visited[N] = 0;
    while(!q.empty()){
        int x = q.front().first;
        string a = q.front().second;
        q.pop();

        if(x == M){
            cout<<a<<"\n";
            return;
        }

        for(int i = 0; i < 4; i++){
            int nx = dslr(i, x);

            if(visited[nx]){
                continue;
            }
                q.push({nx,a+spell[i]});
                visited[nx] = 1;
        }
    }
}


int main(){
    cin>>T;
    while(T--){
        memset(visited, 0, sizeof(visited));
        cin >> N >> M;
        bfs();
    }
}