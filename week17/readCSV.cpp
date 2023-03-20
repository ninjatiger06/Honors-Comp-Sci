#include<iostream>
#include<fstream>

using namespace std;

// Test data structure, mixing strings and numbers
struct Test {
    string filename;
    int wins;
    string player;
};

int main() {
    // Test data to input
    ifstream fin("test.csv");
    // At this point, you'll have to just limit the total number of games?
    // There are C++ structures that would work, but we haven't covered those.
    Test test[100];
    string in_str;
    int tmp, i=0;

    // Loop over lines of file
    while (fin.good()) {
        // fields separated by commas
        getline(fin, in_str, ',');
        /* Problem is, you need quotes around the string for CSV format, but
        you don't want quotes in the stored version, so gotta snip those off */
        // Snip first character
        in_str.erase(in_str.begin());
        // Move to the end, back up one character and delete that one.
        in_str.erase(in_str.end() - 1);
        test[i].filename = in_str;
        getline(fin, in_str, ',');
        // Comes in as string, convert to integer.
        tmp = stoi(in_str);
        test[i].wins = tmp;
        getline(fin, in_str);
        // Snip quotes
        in_str.erase(in_str.begin());
        in_str.erase(in_str.end() - 1);
        test[i].player = in_str;
        // Print results to screen to make sure it worked.
        cout << i << " " << test[i].filename << " " << test[i].wins << " " << test[i].player << endl;
        i++;
    }

}