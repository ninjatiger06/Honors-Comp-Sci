/*
Description: Takes an inputted number of games to win from the user and then
             plays rock paper scissors against the user until one party gets the
             specified number of wins.
Author: Jonas Pfefferman '24
Date; 2/13/23
*/

#include<iostream>
#include<string>

using namespace std;

string possibleMoves[3] = {"rock", "paper", "scissors"};

string getChoice() {
    /* Asks the user for their move and ensures it's valid */
    string move;

    while (true) {
        cout << "Your move (either rock, paper, or scissors): ";
        getLine(cin, move);

        if (move == possibleMoves[0] || move == possibleMoves[1] || move ==
            possibleMoves[2]) {
            return move;
        }
        else {
            cout << "Whoops! " << move << " isn't a valid choice. Try again" <<
                endl;
        }
    }
}

int main() {
    string username;
    int playTo;
    int totalGames = 0;
    int userWins = 0;
    int compWins = 0;
    string p1Choice;
    string p2Choice;
    int randIdx;

    cout << "What is your name? ";
    getLine(cin, username);
    
    cout << "How many wins shold we play until? ";
    cin >> playTo;
    cout << "Let's see who can win " << playTo << " games first. Good luck!" <<
        endl;

    while (userWins < playTo && compWins < playTo) {
        cout << "Next round:" << endl;
        p1Choice = getChoice();
    }

    return 0;
}