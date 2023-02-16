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
    int numDays;
    int daysLeft;
    int pagesReadTotal;
    int pagesRead;

    cout << "Pages to read? ";
    cin >> totalPages;
    pagesLeft = totalPages;
    cout << "Days left? ";
    cin >> numDays;

    pagesReadTotal = 0;
    daysLeft = numDays;
    for (int i=0; i < numDays ; i++) {
        cout << endl << "Pages read: ";
        cin >> pagesRead;

        daysLeft -= 1;
        pagesReadTotal += pagesRead;
        pagesLeft = totalPages - pagesReadTotal;

        if (pagesLeft == 0) {
            cout << "You have read " << pagesReadTotal << " out of " <<
                totalPages << " pages. You finished early!" << endl;
            break;
        }

        cout << "You have read " << pagesReadTotal << " out of " << totalPages
            << " pages." << endl << pagesLeft << " pages left, " << daysLeft <<
            " days to go." << endl;
    }

    return 0;
}