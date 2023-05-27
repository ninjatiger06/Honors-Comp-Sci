#include<string>

class Entry {
    friend class Queue;
    public:
        Entry();
        Entry(long valIn);
        long val;
        Entry *pointer;
};

class Queue {
    friend class Entry;
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