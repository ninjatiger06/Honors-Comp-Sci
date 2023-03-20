#include<iostream>
#include<string>

using namespace std;

int main() {
    int input_int;
    string input_str;

    cout << "Vhat is your name? ";
    getline(cin, input_str);
    cout << "Got " << input_str << endl;

    cout << "Vhat is your quest? ";
    getline(cin, input_str);
    cout << "Got " << input_str << endl;

    cout << "Vhat is the airspeed velocity of an unladen swallow? ";
    cin >> input_int;
    cout << "Got " << input_int << endl;
    fflush(stdin);

    cout << "What do you mean, African or European? ";
    getline(cin, input_str);
    cout << "Got " << input_str << endl;

}