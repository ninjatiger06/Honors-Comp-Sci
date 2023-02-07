/*
Title: dashes.cpp
Date: 2/7/23
Author: Jonas Pfefferman '24
Description: Takes an input from a user and adds dashes in between
*/

#include <iostream>
#include <string>

using namespace std;

int main() {
    string userInput;
    string cin;

    cin = "Enter text: ";

   getline(cin, userInput);

    for (auto character: userInput) {
        cout << character << "-";
    }

    return 0;
}