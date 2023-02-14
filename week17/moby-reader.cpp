#include<iostream>
#include<string>
#include<fstream>

using namespace std;

int main() {
    ifstream moby("moby_dick.txt");
    string line;

    while(moby.good()) {
        getline(moby, line);
        cout << line << endl;
    }

    return 0;

    moby.close();
}
