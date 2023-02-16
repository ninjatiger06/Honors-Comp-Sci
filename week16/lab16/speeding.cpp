/*
Description: Calculates whether or not someone is speeding (based on a given
             speed) and decides whether they should get a warning, a ticket or
             be let go
Author: Jonas Pfefferman '24
Date: 2/9/23
*/

#include<iostream>

using namespace std;

int main() {
    int speedLimit;
    int userSpeed;
    int difference;

    cout << "Enter speed limit: ";
    cin >> speedLimit;
    
    cout << "Enter clocked speed: ";
    cin >> userSpeed;

    difference = userSpeed - speedLimit;

    if (difference >= 1) {
        cout << "Driver is speeding! Clocked at " << difference <<
            " mph over the speed limit." << endl;
        if (difference <= 9) {
            cout << "Issue a warning." << endl;
        }
        else if (difference >= 10 && difference <= 19) {
            cout << "Issue a ticket with a $50 fine." << endl;
        }
        else if (difference >= 20 && difference <= 29) {
            cout << "Issue a ticket with a $75 fine." << endl;
        }
        else {
            cout << "Issue a ticket with a $100 fine." << endl;
        }
    }
    else {
        cout << "Driver's speed is within the legal limit." << endl;
    }
    return 0;
}