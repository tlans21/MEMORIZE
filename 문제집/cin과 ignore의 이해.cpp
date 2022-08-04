#include <iostream>
using namespace std;
int main(void)
{
	int n;
	string s;

	cin >> n;
	cout << n << endl;
	cin.ignore();
	
	getline(cin,s);
	cout << s << endl;

	
	return 0;
}