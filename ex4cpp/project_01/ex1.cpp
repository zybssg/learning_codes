#include<iostream>

using namespace std;

int func1(int a){
	return a;
}

int main(){
	int (*p)(int) = &func1;
	cout << p << endl;  // 0
	// p = &func1;
	cout << p << endl;  //1
}
