#include "my_head_file.h"

int main(){
	string n1 = "zyb", n2="sx";
	Student *p_s1 = new Student(n1, 20, 90);
	Student s2(n2, 19);
	void (Student::*p_fun)();
	p_fun = &Student::display;
	// p_s1->get_score(95);
	// Student s2(n2, 19);
	// s2.get_score(90);

	p_s1->display();
	(s2.*p_fun)();
	// p_s2->display();
	delete p_s1;
	// s2.display();
	// delete p_s2;
	cout << p_s1 << endl;
	cout << p_fun << endl;
	return 0;
}
