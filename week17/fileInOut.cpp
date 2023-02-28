#include<iostream>
#include<fstream>
#include<string>

using namespace std;

int main() {
    fstream file_in_out ("testfile.txt", ios::in | ios::out | ios::trunc);
    string line_from_file = "";
    
    getline(file_in_out, line_from_file);
    cout << line_from_file << endl;
    for (int i = 0; i<10; i++) {
        file_in_out << "Your number is " << i << endl;
    }
    getline(file_in_out, line_from_file);
    cout << line_from_file;
    file_in_out.close();
}