#ifndef _my_head_file_h_
#define _my_head_file_h_

#include<iostream>
#include<string>

using namespace std;

class Student{
	private:
		string name;
		int age;
		int score;
	public:
		Student(string, int, int=80);
		// Student(string, int, int);
        ~Student();
        // Student(string, int);
		void display() const;
};

#endif
