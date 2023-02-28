/*  
    Name: Jonas Pfefferman
    Date: 2/28/23
    Purpose: Demonstrate passing arrays to/from functions
*/

#include<iostream>
#include<cmath>
#include<bitset>

using namespace std;

int i;

void receiveArray(int * numbersPtr) {
    // We've received a pointer to a location in memory so if we
    // change the list of numbers here, yes it will change the list in main also
    for (i=0; i<10; i++){
        cout << *(numbersPtr + i) << ' ';
        cout << endl;
    }
    for (i=0; i<10; i++) *(numbersPtr + i) = i;
}

int main() {
    int numbers[10];
    int * numbersPtr = & numbers[0];

    for (i=0; i<10; i++) numbers[i] = pow(2, i);
    receiveArray(numbersPtr); // could use receiveArray(&numbers[0]) too
    for (i=0; i<10; i++) cout << numbers[i] << ' ';
    cout << endl;
}