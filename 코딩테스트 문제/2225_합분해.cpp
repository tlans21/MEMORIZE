#include<iostream>

using namespace std;

int main(){
    int N;
    int K;

    cin>>N>>K;

    int dp[201][201] ={0};
    for(int i = 0; i <= N; i++){
        dp[1][i] = 1;
        dp[2][i] = i+1;
    }
    

    for(int i = 3; i <= K; i++){
        for(int j = 0; j <= N; j++){
            for(int k = 0; k <= j; k++){
                dp[i][j] =(dp[i][j] + dp[i-1][j-k]) %1000000000;
            }
        }
    }
    cout<<dp[K][N];
    return 0;

}