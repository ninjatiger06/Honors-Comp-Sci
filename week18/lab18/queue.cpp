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
        void enqueue(long item);
        long dequeue();
        long peek();
        void dump();
        void deleteQueue();
        Entry *front;
        Entry *back;
        long size;
};

Queue::Queue() {
    front = NULL;
    back = NULL;
    size = 0;
}

void Queue::enqueue(long item) {
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

long Queue::dequeue() {
    long val = front -> val;
    Entry *tmpPtr = this -> front;
    front = front -> pointer;
    size--;
    delete tmpPtr;
    return val;
}

long Queue::peek() {
    long val = front -> val;
    return val;
}

void Queue::dump() {
    Entry *currEntry = front;
    for (int i=0; i<size; i++) {
        cout << currEntry -> val << ", " << flush;
        currEntry = currEntry -> pointer;
    }
    cout << endl;
}

void Queue::deleteQueue() {
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
    Queue myqueue;
    long userInput;
    long peekVal;
    
    myqueue.enqueue(1);
    myqueue.dump();
    cout << endl;
    myqueue.enqueue(2);
    peekVal = myqueue.peek();
    cout << peekVal << endl;
    myqueue.dump();
    cout << endl;
    myqueue.dequeue();
    myqueue.dump();
    cout << endl;
    myqueue.enqueue(3);
    myqueue.enqueue(4);
    myqueue.dump();
    cout << endl;
    myqueue.dequeue();
    myqueue.dump();
    cout << endl;
    myqueue.deleteQueue();

    // for (long i=0; i<5000000000000000; i++) {
    //     myqueue.enqueue(1);
    //     myqueue.enqueue(2);
    //     myqueue.enqueue(3);
    //     myqueue.deleteQueue();
    // }

}