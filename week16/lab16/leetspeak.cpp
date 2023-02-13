/*
Description: Will take a user's inputted string and convert it to Leetspeak—
             certain letters will be replaced with symbols/numbers
Author: Jonas Pfefferman '24
Date: 2/13/23
*/

#include<iostream>
#include<string>

using namespace std;

int main() {
    string userInput;

    cout << "Enter a string: ";
    getline(cin, userInput);

    for (auto character: userInput) {
        switch (character) {
            case 'e' | 'E':
                cout << '3';
                break;
            case 'l' | 'L':
                cout << '1';
                break;
            case 's' | 'S':
                cout << '5';
                break;
            default:
                cout << character;
                break;
        }
    }

    return 0;
}