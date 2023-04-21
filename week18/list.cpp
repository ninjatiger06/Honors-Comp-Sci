#include<iostream>
#include<string>

using namespace std;

class Entry {
    public:
        Entry();
        Entry(long valIn);
        long val;
        Entry *pointer;
};

Entry::Entry() {
    val = 0;
    pointer = NULL;
}

Entry::Entry( long valIn) {
    val = valIn;
    pointer = NULL;
}

class List {
    public:
        List();
        void insert(long item);
        long pop(long idx);
        long peek();
        void dump();
        long findAtIdx(long idx);
        Entry *front;
        Entry *back;
        long size;
};

List::List() {
    front = NULL;
    back = NULL;
    size = 0;
}

void List::insert(long item) {
    Entry * newEntry = new Entry(item);
    if (size == 0) {
        front = newEntry;
        back = newEntry;
    }
    else {
        back -> pointer = newEntry;
        back = newEntry;
    }
    size++;
}

long List::pop(long idx) {
    long val;
    Entry *currEntry = front;
    Entry *nextEntry;
    for (int i=0; i<idx-1; i++) {
        currEntry = currEntry -> pointer;
    }
    Entry *tmpPtr = currEntry;
    nextEntry = currEntry -> pointer;
    val = nextEntry -> val;
    currEntry -> pointer = nextEntry -> pointer;
    size--;
    delete tmpPtr;
    return val;
}

long List::peek() {
    long val = front -> val;
    return val;
}

void List::dump() {
    Entry *currEntry = front;
    for (int i=0; i<size; i++) {
        cout << currEntry -> val << ", " << flush;
        currEntry = currEntry -> pointer;
    }
    cout << endl;
}

long List::findAtIdx(long idx) {
    int currIdx = 0;
    Entry *currEntry = front;
    for (int i=0; i<idx; i++) {
        currEntry = currEntry -> pointer;
    }
    return currEntry -> val;
}

int main() {
    List myList;
    long userInput;
    long peekVal;
    long idxFind;

    myList.insert(1);
    myList.dump();
    cout << endl;
    myList.insert(2);
    peekVal = myList.peek();
    cout << peekVal << endl;
    myList.dump();
    cout << endl;
    myList.pop(0);
    myList.dump();
    cout << endl;
    myList.insert(3);
    myList.insert(4);
    myList.dump();
    idxFind = myList.findAtIdx(2);
    cout << idxFind << endl;
    cout << endl;
    myList.pop(0);
    myList.dump();
    cout << endl;

}