#include<iostream>
#include<string.h>


using namespace std;
int n;
bool visited[100][100] = {false};
char map[100][100];

int dx[4] = {0, 0, -1, 1};
int dy[4] = {-1, 1, 0, 0};

void dfs(int y, int x){

    visited[y][x] = true;

    for(int i = 0; i < 4; i++){
        int nx = x +dx[i];
        int ny = y + dy[i];
        if(nx < 0 || nx >= n || ny < 0 || ny >= n){
            continue;
        }
        if(!visited[ny][nx] && map[y][x] == map[ny][nx]){
            dfs(ny, nx);
        }
    }
}


int main(){


    int cnt;
    int cnt2;
    cnt = 0;
    cnt2 = 0;
    
    cin>>n;
    for(int i = 0; i < n; i++){
		scanf("%s", map[i]);
	}
    

    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            if(!visited[i][j]){
                dfs(i, j);
                cnt++;
                }
            }            
        }

    

    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            if(map[i][j] == 'G'){
                map[i][j] = 'R';
            }
        }
    }
     memset(visited, false, sizeof(visited));

    for(int u = 0; u < n; u++){
        for(int v = 0; v < n; v++){
            if(!visited[u][v]){
                dfs(u, v);
                cnt2++;
            }            
        }
    }
    cout<<cnt<<" "<<cnt2<<endl;

    return 0;
}


