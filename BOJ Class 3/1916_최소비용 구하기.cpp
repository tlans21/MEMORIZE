#include<iostream>
#include<queue>
#include<vector>

#define INF 100000000;

using namespace std;

int start;

vector<pair<int, int>> a[1001];
priority_queue<pair<int,int>,vector<pair<int,int> >,greater<pair<int,int>>>pq;
int d[1001];

int main(){
    int end;
    int N;
    int M;
    cin>>N>>M;
    
    for(int i = 1; i<= N; i++){
        d[i] = INF;
    }
    while(M--){
        int x, y, z;
        cin>>x>>y>>z;
        a[y].push_back(make_pair(x, z));
        a[x].push_back(make_pair(y, z)); 
    }
    cin>>start>>end;

    d[start] = 0;
    pq.push(make_pair(0, start));
    while(!pq.empty()){
        int current = pq.top().first;
        int distance = pq.top().second;
        pq.pop();
        if(d[current] < distance){
            continue;
        }
        for(int i = 0; i < a[current].size(); i++){
            int next = a[current][i].first;
            int nextDistance = distance + a[current][i].second;
            if(nextDistance < d[next]){
                d[next] = nextDistance;
                pq.push(make_pair(next, nextDistance));
            }
        }
    }
   cout<<("%d", d[end]);
}