#include "headfile.h"
using namespace std;


Student::Student(string n, int a, int s){
	name = n;
	age = a;
	score = s;
}

// Student::Student(){}

Student::~Student(){
	cout << name << ", ni tai qiang le." << endl;
}

// Student::Student(string n, int a){
// 	name = n;
// 	age = a;
// 	score = 0;
// }


void Student::display() const{
	cout << this->name << " is " << (*this).age << " years old." << endl;
	cout << "the score of " << name << " is " << score << endl;
}