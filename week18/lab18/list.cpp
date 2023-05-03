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
        void insertAtIdx(long item, long idx);
        long pop(long idx);
        long peek();
        void dump();
        long findAtIdx(long idx);
        void deleteList();
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

void List::insertAtIdx(long item, long idx) {
    Entry *newEntry = new Entry(item);
    Entry *currEntry = front;
    if (idx == size-1) {
        insert(item);
    }
    else if (idx > 0) {
        if (idx > size) {
            for (int i=0; i<size-1; i++) {
                currEntry = currEntry -> pointer;
            }
        }
        else {
            for (int i=0; i<idx-1; i++) {
                currEntry = currEntry -> pointer;
            }
        }
        Entry *nextEntry = currEntry -> pointer;
        currEntry -> pointer = newEntry;
        newEntry -> pointer = nextEntry;
    }
    else {
        newEntry -> pointer = currEntry;
        front = newEntry;
    }
    size++;
}

long List::pop(long idx) {
    long itemVal;
    Entry *prevEntry = front;
    Entry *currEntry;
    Entry *nextEntry;
    if (idx > 0) {
        for (int i=0; i<idx-1; i++) {
            prevEntry = prevEntry -> pointer;
        }
        currEntry = prevEntry -> pointer;
        Entry *tmpPtr = currEntry;
        nextEntry = currEntry -> pointer;
        itemVal = currEntry -> val;
        prevEntry -> pointer = nextEntry;
        delete tmpPtr;
    }
    else {
        currEntry = front;
        Entry *tmpPtr = currEntry;
        nextEntry = currEntry -> pointer;
        itemVal = currEntry -> val;
        front = nextEntry;
        delete tmpPtr;
    }
    // cout << currEntry -> val << endl;
    // Entry *tmpPtr = currEntry;
    // nextEntry = currEntry -> pointer;
    // itemVal = nextEntry -> val;
    // currEntry -> pointer = nextEntry -> pointer;
    size--;
    return itemVal;
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

void List::deleteList() {
    for (int i=0; i<size; i++) {
        long val = front -> val;
        Entry *tmpPtr = this -> front;
        front = front -> pointer;
        delete tmpPtr;
    }
    front = NULL;
    back = NULL;
    size = 0;
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
    myList.insertAtIdx(5, 0);
    myList.dump();
    idxFind = myList.findAtIdx(2);
    cout << idxFind << endl;
    cout << endl;
    myList.pop(1);
    myList.dump();
    myList.insertAtIdx(6, 12);
    myList.dump();
    myList.insertAtIdx(6, 1);
    myList.dump();
    cout << endl;

    // for (long i=0; i<5000000000000000; i++) {
    //     myList.insert(1);
    //     myList.insert(2);
    //     myList.insert(3);
    //     myList.deleteList();
    // }

}