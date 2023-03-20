#include<iostream>
#include<string>

using namespace std;

enum flavor {chocolate, vanilla, strawberry};

int main() {
    flavor f;
    f = chocolate;
    cout << f << endl;
    cout << "enter flavor: ";
    getline(cin, f);
    cout << f << endl;
}