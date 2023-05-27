#include <iostream>
#include<string>
#include "binary_tree.h"
#include"queue.h"

using namespace std;

Tree::Tree() {
    head = NULL;
}

void Tree::add_node(long content) {
    if (head == NULL) {
        Node * nodePtr = new Node(content);
        head = nodePtr;
    }
    else {
        if (content < head -> content) {
            head -> add_left(content);
        }
        else if ( content > head -> content) {
            head -> add_right(content);
        }
    }
}

void Tree::dump_tree() {
    Queue treeQ;
    Node* currNode;
    treeQ.enqueue(reinterpret_cast<long>(head));
    while (treeQ.size > 0) {
        currNode = reinterpret_cast<Node*>(treeQ.dequeue());
        cout << currNode -> content << ", " << flush;
        if (currNode -> left != NULL) {
            treeQ.enqueue(reinterpret_cast<long>(currNode -> left));
        }
        if (currNode -> right != NULL) {
            treeQ.enqueue(reinterpret_cast<long>(currNode -> right));
        }
    }
    cout << endl;
}

void Tree::depth_dump(Node* currNode) {
    cout << currNode -> content << endl;
    if (currNode -> left != NULL) {
        depth_dump(currNode -> left);
    }
    if (currNode -> right != NULL) {
        depth_dump(currNode -> right);
    }
}

bool Tree::search_tree(long num, Node* currNode) {
    // cout << num << ", " << currNode -> content << endl;
    // cout << (num == currNode -> content) << endl;
    if (num < currNode -> content) {
        if (currNode -> left != NULL) {
            search_tree(num, currNode -> left);
        }
        else {
            return false;
        }
    }
    if (num > currNode -> content) {
        if (currNode -> right != NULL) {
            search_tree(num, currNode->right);
        }
        else {
            return false;
        }
    }
    if (num == currNode -> content) {
        cout << true << endl;
        return true;
    }
}

Node::Node() {
    
}

Node::Node(long numInput) {
    left = NULL;
    right = NULL;
    content = numInput;
}

void Node::add_left(long content) {
    if (this -> left == NULL) {
        Node * nodePtr = new Node(content);
        this -> left = nodePtr;
    }
    else {
        if (content < left -> content) {
            left -> add_left(content);
        }
        else if (content > left -> content) {
            left -> add_right(content);
        }
    }
}

void Node::add_right(long content) {
    if (this -> right == NULL) {
            Node * nodePtr = new Node(content);
            this -> right = nodePtr;
        }
    else {
        if (content > right -> content) {
            right->add_right(content);
        }
        else if (content < right -> content) {
            right -> add_left(content);
        }
    }
}