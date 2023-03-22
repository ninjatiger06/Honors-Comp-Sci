#include<iostream>
#include<string>
#include<ctime>
#include<fstream>
#include<stdlib.h>

using namespace std;

struct round {
    string gameTime;
    string p1Name;
    string p1Move;
    int p1Wins;
    string p2Name;
    string p2Move;
    int p2Wins;
    string winner;
};

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

void readGameLog(string filename, round *logArrayPtr, int logIdx, round *oldLogPtr) {
    ifstream readLog(filename);
    string inStr;
    string firstLine;
    int tmp;
    getline(readLog, firstLine);
    if (firstLine != "") {
        while (readLog.good()) {
            getline(readLog, inStr, ',');
            if (inStr.empty()) {
                break;
            }
            (logArrayPtr+logIdx)->gameTime = inStr;
            (oldLogPtr+logIdx)->gameTime = inStr;
            getline(readLog, inStr, ',');
            (logArrayPtr+logIdx)->p1Name = inStr;
            (oldLogPtr+logIdx)->p1Name = inStr;
            getline(readLog, inStr, ',');
            (logArrayPtr+logIdx)->p1Move = inStr;
            (oldLogPtr+logIdx)->p1Move = inStr;
            getline(readLog, inStr, ',');
            tmp = stoi(inStr);
            (logArrayPtr+logIdx)->p1Wins = tmp;
            (oldLogPtr+logIdx)->p1Wins = tmp;
            getline(readLog, inStr, ',');
            (logArrayPtr+logIdx)->p2Name = inStr;
            (oldLogPtr+logIdx)->p2Name = inStr;
            getline(readLog, inStr, ',');
            (logArrayPtr+logIdx)->p2Move = inStr;
            (oldLogPtr+logIdx)->p2Move = inStr;
            getline(readLog, inStr, ',');
            tmp = stoi(inStr);
            (logArrayPtr+logIdx)->p2Wins = tmp;
            (oldLogPtr+logIdx)->p2Wins = tmp;
            getline(readLog, inStr);
            (logArrayPtr+logIdx)->winner = inStr;
            (oldLogPtr+logIdx)->winner = inStr;
            logIdx++;
        }
    }
    else {
        ofstream gameLog(filename, ios::app);
        gameLog << "Save Time, Player1, P1 Move, P1 Wins, Player2, P2 Move, P2 Wins, Winner";
        gameLog.close();
    }
    readLog.close();
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

int printScores(string p1Name, string p2Name, int userWins, int compWins) {
    /* Prints out a scorecard of the wins after each round */
    cout << "-----------------------------------------" << endl;
    cout << p1Name << ": " << userWins << "          " << p2Name << ": " <<
        compWins << endl;
    cout << "-----------------------------------------" << endl << endl;
    return 0;
}

// int logRound(ofstream gameLog, round *currRound) {
//     gameLog << "\n";
//     gameLog << currRound->p1Name << ",";
//     gameLog << currRound->p1Move << ",";
//     gameLog << currRound->p1Wins << ",";
//     gameLog << currRound->p2Name << ",";
//     gameLog << currRound->p2Move << ",";
//     gameLog << currRound->p2Wins << ",";
//     gameLog << currRound->winner << ",";
//     return 0;
// }

void logGame(round logArray[], string filename, int logLen, string gameTime) {
    ofstream gameLog(filename, ios::app);
    for (int i=0; i<logLen; i++) {
        round lookRound;
        lookRound = logArray[i];

        if (lookRound.p1Name.empty()) {
            break;
        }
        gameLog << endl;
        gameLog << gameTime << ',';
        gameLog << lookRound.p1Name << ',';
        gameLog << lookRound.p1Move << ',';
        gameLog << lookRound.p1Wins << ',';
        gameLog << lookRound.p2Name << ',';
        gameLog << lookRound.p2Move << ',';
        gameLog << lookRound.p2Wins << ',';
        gameLog << lookRound.winner << ',';
    }
}

void reviewGames(round *logArrayptr, int logIdx) {
    string dates[logIdx] = {};
    for (int i=0; i<logIdx; i++) {
        if (!(find(dates.begin(), dates.end(), (logArrayptr+i)[0]))) {
            dates[i] = (logArrayptr+i)[0];
        }
    }
}

int main() {
    string inputStr;
    string p1Name;
    string p2Name;
    int playTo;
    int totalGames = 0;
    int userWins = 0;
    int compWins = 0;
    string p1Choice;
    string p2Choice;
    int randIdx;
    int winner;
    srand(time(NULL));
    round currRound;
    round * roundPtr = & currRound;
    string whoWon;
    string filename;
    int numPlayers;
    string printGame;
    time_t myTime = time(NULL);
    string gameTime = ctime(&myTime);
    gameTime.pop_back();
    string userInput;

    filename = "gameLog.csv";
    // ofstream gameLog(filename, ios::app);

    cout << "How many players (1 or 2): ";
    getline(cin, inputStr);
    numPlayers = stoi(inputStr);
    cout << endl;

    cout << "Player 1 name: " << flush;
    getline(cin, inputStr);
    cout << "Hi, " << inputStr << endl;
    p1Name = inputStr;

    if (numPlayers == 2) {
        cout << "Player 2 name: ";
        getline(cin, inputStr);
        cout << "Hi, " << inputStr << endl;
        p2Name = inputStr;
    }
    else {
        p2Name = "Computer";
    }
    
    cout << "How many wins shold we play until? ";
    cin >> ws;
    cin >> playTo;
    cout << "Let's see who can win " << playTo << " games first. Good luck!" <<
        endl;

    const int logLen = playTo*10;
    round logArray[logLen] = {};
    int logIdx = 0;
    round * logArrayPtr = &logArray[0];

    round oldLog[logLen] = {};
    round *oldLogPtr = &oldLog[0];

    round newLog[logLen] = {};
    int newLogIdx = 0;
    round *newLogPtr = &oldLog[0];

    // To-do: fix this
    // streampos begin;
    // gameLog.seekp(ios_base::beg);
    // begin = gameLog.tellp();
    // gameLog.seekp(ios_base::end);
    // if (gameLog.tellp() == begin) {
    //     gameLog << "Player1, P1 Move, P1 Wins, Player2, P2 Move, P2 Wins, Winner";
    // }

    // gameLog.close();

    readGameLog(filename, logArrayPtr, logIdx, oldLogPtr);

    while (true) {
        cout << "Welcome to Rock-Paper-Scissors Deluxe! Please choose one of the following options:" << endl;
        cout << "1. Play a New Game" << endl;
        cout << "2. Review Old Games" << endl;
        cout << "3. Quit" << endl;
        getline(cin, userInput);


        if (userInput == "1") {
            while (userWins < playTo && compWins < playTo) {
                cout << endl << "Next round:" << endl;
                p1Choice = getChoice();
                if (numPlayers == 1) {
                    randIdx = rand() % 3;
                    p2Choice = possibleMoves[randIdx];
                }
                else {
                    cout << flush;
                    system("clear");
                    p2Choice = getChoice();
                }
                cout << p1Name << " picks " << p1Choice << " and " << p2Name << " picks " <<
                    p2Choice << endl;
                winner = calculateWinner(p1Choice, p2Choice);

                if (winner == 0) {
                    cout << "... A Tie." << endl;
                    totalGames += 1;
                    whoWon = "Tie";
                }
                else if (winner == 1) {
                    cout << "... " << p1Name << " wins!" << endl;
                    totalGames += 1;
                    userWins += 1;
                    whoWon = p1Name;
                }
                else if (winner == 2) {
                    cout << "... " << p2Name << " wins!" << endl;
                    totalGames += 1;
                    compWins += 1;
                    whoWon = p2Name;
                }

                printScores(p1Name, p2Name, userWins, compWins);
                currRound.gameTime = gameTime;
                currRound.p1Name = p1Name;
                currRound.p1Move = p1Choice;
                currRound.p1Wins = userWins;
                currRound.p2Name = p2Name;
                currRound.p2Move = p2Choice;
                currRound.p2Wins = compWins;
                currRound.winner = whoWon;

                logArray[logIdx] = currRound;
                newLog[newLogIdx] = currRound;
                logIdx++;
                newLogIdx++;
                }

                if (userWins > compWins) {
                    cout << p1Name << " beat Computer:" << endl << "... won " << userWins
                    << " in " << totalGames << " rounds of rock-paper-scissors." << endl;
                }
                else {
                    cout << "Computer beat " << p1Name << ":" << endl << "... won " <<
                    compWins << " in " << totalGames << " rounds of rock-paper-scissors." <<
                    endl;
                }

            logGame(newLog, filename, logLen, gameTime);
        }
        else if (userInput == "2")  {
            reviewGames(logArrayPtr, logIdx);
        }
        else {
            break;
        }
    }

    return 0;
}