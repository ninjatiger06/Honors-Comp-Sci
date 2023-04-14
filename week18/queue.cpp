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

class Queue {
    public:
        Queue();
        void enqueue(Entry item);
        long dequeue();
        long peek();
        void dump();
        Entry *front;
        Entry *back;
        long size;
};

Queue::Queue() {
    front = NULL;
    back = NULL;
    size = 0;
}

void Queue::enqueue(Entry item) {
    if (size == 0) {
        front = &item;
        back = &item;
    }
    else {
        back -> pointer = &item;
        back = &item;
    }
    size++;
}

long Queue::dequeue() {
    long val = front -> val;
    front = front -> pointer;
    return val;
}

long Queue::peek() {
    long val = front -> val;
    return val;
}

void Queue::dump() {
    Entry *currEntry = front;
    cout << front -> val << endl;;
    for (int i=0; i<size; i++) {
        cout << currEntry -> val << ", " << flush;
        currEntry = currEntry -> pointer;
    }
    cout << endl;
}

int main() {
    Queue myqueue;
    long userInput;
    long peekVal;

    cout << "Entry1: " << flush;
    // cin >> userInput;
    Entry entry1(1);

    cout << "Entry2: " << flush;
    // cin >> userInput;
    Entry entry2(2);

    cout << "Entry3: " << flush;
    // cin >> userInput;
    Entry entry3(3);

    cout << "Entry4: " << flush;
    // cin >> userInput;
    Entry entry4(4);
    cout << endl << endl;

    myqueue.enqueue(entry1);
    myqueue.dump();
    cout << endl;
    myqueue.enqueue(entry2);
    peekVal = myqueue.peek();
    cout << peekVal << endl;
    myqueue.dump();
    cout << endl;
    myqueue.dequeue();
    myqueue.dump();
    cout << endl;
    myqueue.enqueue(entry3);
    myqueue.enqueue(entry4);
    myqueue.dump();
    cout << endl;
    myqueue.dequeue();
    myqueue.dump();
    cout << endl;

}