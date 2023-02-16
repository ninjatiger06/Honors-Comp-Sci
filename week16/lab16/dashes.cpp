/*
Description: Takes an input from a user and adds dashes in between
Author: Jonas Pfefferman '24
Date: 2/7/23
*/

#include <iostream>
#include <string>

using namespace std;

int main() {
    string userInput;

    cout << "Enter text: ";
    getline(cin, userInput);

    cout << '-';
    for (auto character: userInput) {
        cout << character << '-';
    }

    return 0;
}