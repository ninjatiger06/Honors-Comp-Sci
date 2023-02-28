#include<iostream>
#include<string>

using namespace std;

struct rpsMove {
    string playerName;
    string moveChoice;
};

enum valid_move {
    "rock",
    "paper",
    "scissors"
} rpsMoves;

rpsMove getChoice() {
    // now you can return a compound object that's *multiple* things
    
}

int main() {
    // using declared data structure
    rpsMove player;
    rpsMove computer;

    player.playerName = "Janos";
    player.moveChoice = "rock";

    computer.playerName = "ChatGPT";
    computer.moveChoice = "scissors";

}