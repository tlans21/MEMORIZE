#include<iostream>

using namespace std;

int main(){
    int N;
    long long dp[101][21]={0,};
    int arr[101]={0,};
    cin>>N;
    
    
    for(int i = 1; i <= N; i++){
        cin>>arr[i];
    }
    int K = arr[N];

    dp[1][arr[1]] = 1;
    for(int i = 2; i <= N-1; i++){
        for(int j =0; j<=20; j++){
            if(dp[i-1][j] == 0){
                continue;
            }

            if(arr[i] + j <= 20){
                dp[i][j+arr[i]] += dp[i-1][j];
            }

            if(j - arr[i] >= 0){
                dp[i][j-arr[i]] += dp[i-1][j];
            }
        }
    }
    long long solution = dp[N-1][K];
    cout<<solution;

    return 0;
}