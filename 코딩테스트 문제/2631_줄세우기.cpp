#include<iostream>

using namespace std;

int main(){
    int N;

    cin>>N;
    int arr[201];

    for(int i = 1; i <= N; i++){
        cin>>arr[i];
    }
    int dp[201];

    int Max = 0;

    for(int i = 1; i <= N; i++){
        dp[i] = 1;
        for(int j = 1; j <= i; j++){
            if(arr[i] > arr[j] && dp[i] < dp[j] + 1){
                dp[i]++;
            }
        }

        if(Max < dp[i]){
            Max = dp[i];
        }
    }
    cout<<N-Max<<'\n';
}