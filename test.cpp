#include<iostream>
using namespace std;

int main(){
	int king;
	int queen;
	int look;
	int bishop;
	int knight;
	int p;

	cin>>king>>queen>>look>>bishop>>knight>>p;
	
	

	cout<<1-king<<" "<<1-queen<<" "<<2-look<<" "<<2-bishop<<" "<<2-knight<<" "<<8-p<<endl;

	return 0;
}