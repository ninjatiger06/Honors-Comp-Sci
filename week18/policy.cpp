#include<iostream>
#include<string>

using namespace std;

class Policy {
    public:
        Policy();
        Policy(string title_in, string time_in, string description_in);
        string title;
        string time;
        string description;
};

Policy::Policy() {
    title = "";
    time = "";
    description = "";
}

Policy::Policy(string title_in, string time_in, string description_in) {
    title = title_in;
    time = time_in;
    description = description_in;
}

int main() {
    Policy tobaccoBan;
    cout << tobaccoBan.title << " " << tobaccoBan.time << " " << tobaccoBan.description << endl;
    Policy healthcare("Jerrycare™️", "January 1, 2024", "Providing public healthcare to all");
    cout << healthcare.title << " " << healthcare.time << " " << healthcare.description << endl;
}