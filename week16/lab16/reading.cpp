/*
Description: Helps a student reach a given reading deadline
Author: Jonas Pfefferman '24
Date: 2/14/23
*/

#include<iostream>
#include<string>

using namespace std;

int main() {
    int totalPages;
    int pagesLeft;
    int daysLeft;
    int pagesReadTotal;
    int pagesRead;

    cout << "Pages to read? ";
    cin >> totalPages;
    pagesLeft = totalPages;
    cout << "Days left? ";
    cin >> daysLeft;

    pagesReadTotal = 0;
    for (int i=0; i <= daysLeft + 1; i++) {
        cout << "Pages read: ";
        cin >> pagesRead;

        daysLeft -= 1;
        pagesReadTotal += pagesRead;
        pagesLeft = totalPages - pagesReadTotal;

        cout << "You have read " << pagesReadTotal << " out of " << totalPages << " pages." << endl;
        cout << pagesLeft << " pages left, " << daysLeft << " days to go." << endl;
    }

    return 0;
}