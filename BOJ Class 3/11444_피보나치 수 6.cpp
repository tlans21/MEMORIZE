#include<iostream>

using namespace std;

int fibonachi(int n){
    if(n == 0){
        return 0;
    }else if(n == 1){
        return 1;
    }else{
       return (fibonachi(n-1) % 1000000007 + fibonachi(n-2) % 1000000007) % 1000000007;
    }
}

int main(){
    int N;
    cin>>N;

    cout<<fibonachi(N)<<endl;
}