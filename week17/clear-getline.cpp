#include<iostream>
#include<string>

using namespace std;

int main() {
    int i;
    string x;

    cout << "ENter a name: ";
    getline(cin, x);
    cout << "Enter a number; ";
    cin >> i;
    while(getchar() != '\n');
    cout << "Enter one of: a, b, c: ";
    getline(cin, x);
}