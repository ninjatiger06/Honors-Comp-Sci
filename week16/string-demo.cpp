#include<iostream>
#include<string>

using namespace std;

int main() {
    string user_input;

    cout << "Tell me your name: ";
    cin >> user_input;
    cout << endl;
    cout << "Hello, " << user_input << '!' << endl;

    return 0;
}