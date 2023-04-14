#include<iostream>
#include<string>

using namespace std;

// old school style: class student_t
class Student {
    // options are private, protected, public, and (kind of) static
    public:
        // Default constructor: No args, same name as class.
        Student();
        Student(string firstName_in, string lastName_in);
        string firstName;
        string lastName;
};

Student::Student() {
    firstName = "";
    lastName = "";
}

Student::Student(string firstName_in, string lastName_in) {
    firstName = firstName_in;
    lastName = lastName_in;
}

int main() {
    Student sophia;
    Student mia("Mia", "Gaspar");
    sophia.firstName = "Sophia";
    sophia.lastName = "Guan";
    cout << sophia.firstName << " " << sophia.lastName << endl;
    cout << mia.firstName << " " << mia.lastName << endl;
}