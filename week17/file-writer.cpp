#include<iostream>
#include<string>
#include<fstream>

using namespace std;

int main() {
    ofstream fout("testfile.txt");
    // Equivalent: fstream fout("testfile.txt", ios::out)
        // :: is to select function out of subclass
    // fout is just a variable name, not a keyword -> could be anything

    for (int i = 0; i<10; i++) {
        fout << "My number is " << i << endl;
        // because file output instead of console output
    }

    fout.close();

    return 0;
}
