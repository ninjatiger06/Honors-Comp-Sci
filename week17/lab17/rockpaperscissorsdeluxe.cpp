#include<iostream>
#include<string>
#include<ctime>
#include<fstream>

using namespace std;

string possibleMoves[3] = {"rock", "paper", "scissors"};

string getChoice() {
    /* Asks the user for their move and ensures it's valid */
    string move;

    while (true) {
        cout << "Your move (either rock, paper, or scissors): ";
        cin >> move;

        if (move == possibleMoves[0] || move == possibleMoves[1] || move ==
            possibleMoves[2]) {
            return move;
        }
        else {
            cout << "Whoops! " << move << " isn't a valid choice. Try again" <<
                endl << endl;
        }
    }
}

int calculateWinner(string choice1, string choice2) {
    /* Takes the moves of players 1 and 2 and checks to see who won */
    if (choice1 == choice2) {
        return 0;
    }
    else if (choice1 == "scissors" && choice2 == "paper") {
        return 1;
    }
    else if (choice1 == "paper" && choice2 == "rock") {
        return 1;
    }
    else if (choice1 == "rock" && choice2 == "scissors") {
        return 1;
    }
    else {
        return 2;
    }
}

int printScores(string username, int userWins, int compWins) {
    /* Prints out a scorecard of the wins after each round */
    cout << "-----------------------------------------" << endl;
    cout << username << ": " << userWins << "          " << "Computer: " <<
        compWins << endl;
    cout << "-----------------------------------------" << endl << endl;
    return 0;
}

struct round {
    string p1Name;
    string p1Move;
    int p1Wins;
    string p2Name;
    string p2Move;
    int p2Wins;
    string winner;
};

int main() {
    string username;
    int playTo;
    int totalGames = 0;
    int userWins = 0;
    int compWins = 0;
    string p1Choice;
    string p2Choice;
    int randIdx;
    int winner;
    srand(time(NULL));
    string logArray[] = {};
    int logIdx = 0;

    ofstream gameLog("gameLog.csv");

    cout << "What is your name? ";
    getline(cin, username);
    
    cout << "How many wins shold we play until? ";
    cin >> playTo;
    cout << "Let's see who can win " << playTo << " games first. Good luck!" <<
        endl;

    while (userWins < playTo && compWins < playTo) {
        cout << endl << "Next round:" << endl;
        p1Choice = getChoice();
        randIdx = rand() % 3;
        p2Choice = possibleMoves[randIdx];
        cout << username << " picks " << p1Choice << " and Computer picks " <<
            p2Choice << endl;
        winner = calculateWinner(p1Choice, p2Choice);

        if (winner == 0) {
            cout << "... A Tie." << endl;
            totalGames += 1;
        }
        else if (winner == 1) {
            cout << "... " << username << " wins!" << endl;
            totalGames += 1;
            userWins += 1;
        }
        else if (winner == 2) {
            cout << "... Computer wins!" << endl;
            totalGames += 1;
            compWins += 1;
        }

        printScores(username, userWins, compWins);
    }

    if (userWins > compWins) {
        cout << username << " beat Computer:" << endl << "... won " << userWins
        << " in " << totalGames << " rounds of rock-paper-scissors." << endl;
    }
    else {
        cout << "Computer beat " << username << ":" << endl << "... won " <<
        compWins << " in " << totalGames << " rounds of rock-paper-scissors." <<
        endl;
    }

    gameLog.close();
    return 0;
}