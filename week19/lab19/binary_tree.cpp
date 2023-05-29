#include <iostream>
#include<string>
#include "binary_tree.h"
#include"queue.h"

/*
    Name: Jonas Pfefferman and Patrick Rooney
    Date: May 2023
    Purpose: Provides functionality of the Tree and Node classes' functions
*/

using namespace std;

Tree::Tree() {
    head = NULL;
}

void Tree::add_node(long content) {
    // Takes a given number and adds it to the correct spot on the tree
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

void Tree::delete_node(long delNode, Node* currNode) {
    /* Searches the tree for the node with the given content and starting at the
    given starting position (the head), then deletes node. If there are children,
    they get moved up */

    /* Please excuse these horrible if/else nests; it's 11:54 PM, and I saw this
    existed right before I was going to turn it in and decided I'd have a crack at it. */
    Node* nextNode;
    if (currNode -> left != NULL and delNode == currNode->left->content)
    {
        nextNode = currNode->left;
        if (nextNode->left != NULL and nextNode->right != NULL)
        {
            currNode->left = nextNode->right;
            currNode->add_left(nextNode->left->content);
            delete nextNode;
        }
        else if (nextNode->left != NULL)
        {
            currNode->left = nextNode->left;
            delete nextNode;
        }
        else if (nextNode->right != NULL)
        {
            currNode->left = nextNode->right;
            delete nextNode;
        }
        else
        {
            currNode->left = NULL;
            delete nextNode;
        }
        return;
    }
    if (currNode -> right != NULL and delNode == currNode->right->content)
    {
        nextNode = currNode->right;
        if (nextNode->left != NULL and nextNode->right != NULL)
        {
            currNode->right = nextNode->right;
            currNode->add_left(nextNode->left->content);
            delete nextNode;
        }
        else if (nextNode->left != NULL)
        {
            currNode->right = nextNode->left;
            delete nextNode;
        }
        else if (nextNode->right != NULL)
        {
            currNode->right = nextNode->right;
            delete nextNode;
        }
        else
        {
            currNode->right = NULL;
            delete nextNode;
        }
        return;
    }
    else if (delNode < currNode->content) {
        if (currNode->left != NULL)
        {
            delete_node(delNode, currNode->left);
        }
        else
        {
            cout << "Node not found" << endl;
            return;
        }
    }
    else if (delNode > currNode->content) {
        if (currNode->right != NULL)
        {
            delete_node(delNode, currNode->right);
        }
        else
        {
            cout << "Node not found" << endl;
            return;
        }
    }
}

void Tree::dump_tree() {
    // Uses the queue class to perform a breadth-first printing of the tree
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
    /* Uses recursion to perform a depth-first printing of the tree. Takes a starting
    point (the head, preferrably) */

    // Requires the head as an input for the starting place... I'm sure there's
    // a better way of doing it but didn't figure it out
    cout << currNode -> content << endl;
    if (currNode -> left != NULL) {
        depth_dump(currNode -> left);
    }
    if (currNode -> right != NULL) {
        depth_dump(currNode -> right);
    }
}

bool Tree::search_tree(long num, Node* currNode) {
    /*Uses recursion to perform a depth-frist search of the tree for a given
    number. Also requires a starting point (the head). See above function for why
    the starting place is included. */
    if (num < currNode -> content) {
        if (currNode -> left != NULL) {
            search_tree(num, currNode -> left);
        }
        else {
            // false-flag was moved here b/c function still ran through a "return false" even after I had returned true... strange
            return false;
        }
    }
    if (num > currNode -> content) {
        if (currNode -> right != NULL) {
            search_tree(num, currNode->right);
        }
        else {
            // false-flag was moved here b/c function still ran through a "return false" even after I had returned true... strange
            return false;
        }
    }
    // this became an else-if because the function had instead been returning the head's content, no matter if it was meant to return true or false
    else if (num == currNode -> content) {
        return true;
        // function just didn't stop here and continued to outside of the if statement and updated *again* to return false
    }
    // for whatever reason, the below return statement *always* runs, even after a return true above
    // return false;
}

Node::Node() {
    
}

Node::Node(long numInput) {
    left = NULL;
    right = NULL;
    content = numInput;
}

// Patrick did not manage to get the height balance change working, so it has been left out

void Node::add_left(long content) {
    /*Takes a given number and adds it as the left leaf of a node if that space
    is free. If not, it finds a free space*/
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
    /*Takes a given number and adds it as the right leaf of a node if that space
    is free. If not, it finds a free space*/
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