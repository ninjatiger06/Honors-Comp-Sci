#include<iostream>
#include<cmath>
#include<bitset>

using namespace std;

void integerStorage() {
    char myInt = 140;
    // type * variable means you are declaring a variable that represents a
    // pointer to an object of that data type
    char * int_ptr;
    long char_ptr;

    // & is a unary operator - it takes one argument
    int_ptr = &myInt;
    cout << int_ptr << " " << myInt << endl;
    cout << char_ptr + 1 << endl;
}

void integerArrayStorage() {
    int i;
    int myNums[10] = {};
    int * numPtr = &myNums[0];
    char * charPtr = reinterpret_cast<char*>(numPtr);

    for (i=0; i<10; i++) {
        myNums[i] = pow(2, i);
    }
    cout << endl;
    for (i=0; i<10; i++) {
        cout << numPtr + i << " ";
        cout << bitset<32>(*(numPtr + i)) << " ";
        cout << *(charPtr + i);
        cout << myNums[i] << endl;
    }
    for (i=0; i<10; i++) {
        // C++ re-casting
        cout << reinterpret_cast<long>(charPtr + i) + i << " ";
        // C re-casting
        cout << hex << (long) (charPtr + i);
        // * operator is inverse of & operator
        cout << bitset<8>(*(charPtr + i)) << " ";
        cout << *(charPtr + i);
        cout << myNums[i] << endl;
    }
}

void charArrayStorage() {
    // Hamming distance - the number of areas two strings are different (see: C and S are all the same aside from one point)

    char words[] = "HCS: Data Structures and Algorithms";
    // the sizeof() this is 4 characters because there's a null character at the end
    char * wordsPtr = & words[0];

    cout << sizeof(words) << endl;
    for (int i=0; i<sizeof(words); i++) {
        cout << hex << reinterpret_cast<long>(wordsPtr + i) << dec << " ";
        cout << bitset<8>(*(wordsPtr + i)) << " ";
        cout << *(wordsPtr + i) << endl;
        // cout << words[i] << endl;
    }
}

void stringStorage() {
    int i;
    string words = "HCS; Data Structures and Algorithms";
    string * wordsPtr = & words;
    char * charPtr;

    cout << sizeof(words) << endl;
    for (i=0; i<sizeof(words); i++) {
        charPtr = reinterpret_cast<char*>(wordsPtr);
        cout << hex << reinterpret_cast<long>(charPtr + i) << dec << " ";
        cout << bitset<8>(*(charPtr + i)) << " ";
        cout << +(*(charPtr + i)) << " ";
        cout << *(charPtr + i) << " ";
        cout << *(wordsPtr + i) << endl;
    }
}

int main() {
    // integerStorage();
    // integerArrayStorage();
    // charArrayStorage();
    stringStorage();
}