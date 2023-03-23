#include<iostream>
#include<string>

using namespace std;

class Student {
    private:
        int studentID;
    public:
        std::string firstName;
        std::string lastName;

        // default constructor; no inputs
        Student();
        // usual constructor: inputs as needed
        Student(string firstName, string lastName);
};

// To declare a method outside the class, add ClassName:: in front
Student::Student() {
    firstName = "";
    lastName = "";
}

Student::Student(string firstName, string lastName) {
    this -> firstName = firstName;
    this -> lastName = lastName;
}