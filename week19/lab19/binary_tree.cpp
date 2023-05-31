#include <iostream>
#include<string>
#include "math.h"
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

void Tree::draw_tree() {
    // Uses the queue class to perform a breadth-first drawing of the tree
    // Doesn't work super well, but kind of gets the point across (when it works)
    Queue treeQ;
    Node *currNode;
    treeQ.enqueue(reinterpret_cast<long>(head));
    long currIdx = 1;
    long level = 0;
    long onLine = pow (2, level);
    while (treeQ.size > 0)
    {
        if (treeQ.peek() == -1) {
            cout << "NULL     " << flush;
            treeQ.dequeue();
        }
        else {
            currNode = reinterpret_cast<Node *>(treeQ.dequeue());
            // cout << currNode->content << " currIdx: " << currIdx << ", level: " << level << ", onLine: " << onLine << "     " << flush;
            cout << currNode -> content << "     " << flush;
            if (currIdx % 2 == 0) {
                cout << "     " << flush;
            }
            if (currNode->left != NULL) {
                treeQ.enqueue(reinterpret_cast<long>(currNode->left));
            }
            else {
                treeQ.enqueue(-1);
            }
            if (currNode->right != NULL) {
                treeQ.enqueue(reinterpret_cast<long>(currNode->right));
            }
            else {
                treeQ.enqueue(-1);
            }
        }
        currIdx++;
        // cout << currIdx << endl;
        if (currIdx > (onLine)) {
            // cout << "here" << endl;
            cout << endl;
            level++;
            onLine = pow(2, level);
            currIdx = 1;
        }
    }
    cout << endl;
}

void Tree::rotate_left(Node *rotating)
{
    // Rotates the tree to the left around a given unbalanced node
    if (rotating == head)
    {
        head = rotating->right;
        head->height = 0;
        rotating->right = head->left;
        head->left = rotating;
        if (head->left->right != NULL)
        {
            head->left->right->height = 2;
        }
        if (rotating->left != NULL)
        {
            rotating->left->update_nodes_h(1);
        }
        if (head->right != NULL)
        {
            head->right->update_nodes_h(-1);
        }
        head->height_balance = 0;
        head->left->height_balance = 0;
        head->left->parent = head;
        head->left->height = 1;
        head->parent = NULL;
    }
    else
    {
        Node *new_top = rotating->right;

        if (rotating->parent->right == rotating)
        {
            rotating->parent->right = new_top;
        }
        else
        {
            rotating->parent->left = new_top;
        }
        new_top->height--;
        rotating->right = new_top->left;
        new_top->left = rotating;
        if (new_top->left->right != NULL)
        {
            new_top->left->right->parent = new_top->left;
        }
        if (rotating->left != NULL)
        {
            rotating->left->update_nodes_h(1);
        }
        if (new_top->right != NULL)
        {
            new_top->right->update_nodes_h(-1);
        }
        new_top->height_balance = 0;
        new_top->left->height_balance = 0;
        new_top->parent = rotating->parent;
        rotating->height++;
        new_top->left->parent = new_top;
        new_top->update_nodes_b();
    }
}

void Tree::rotate_right(Node *rotating)
{
    // Rotates the tree to the right around a given unbalanced node
    if (Node::unbalanced == head)
    {
        head = Node::unbalanced->left;
        head->height = 0;
        Node::unbalanced->left = head->right;
        head->right = Node::unbalanced;
        if (head->right->left != NULL)
        {
            head->right->left->height = 2;
        }
        if (Node::unbalanced->right != NULL)
        {
            Node::unbalanced->right->update_nodes_h(1);
        }
        if (head->left != NULL)
        {
            head->left->update_nodes_h(-1);
        }
        head->height_balance = 0;
        head->right->height_balance = 0;
        head->right->parent = head;
        head->right->height = 1;
        head->parent = NULL;
    }
    else
    {

        Node *new_top = Node::unbalanced->left;
        if (Node::unbalanced->parent->right == Node::unbalanced)
        {
            Node::unbalanced->parent->right = new_top;
        }
        else
        {
            Node::unbalanced->parent->left = new_top;
        }
        new_top->height--;
        Node::unbalanced->left = new_top->right;
        new_top->right = Node::unbalanced;
        if (new_top->right->left != NULL)
        {
            new_top->right->left->parent = new_top->right;
        }
        if (Node::unbalanced->right != NULL)
        {
            Node::unbalanced->right->update_nodes_h(1);
        }
        if (new_top->left != NULL)
        {
            new_top->left->update_nodes_h(-1);
        }
        new_top->height_balance = 0;
        new_top->right->height_balance = 0;
        new_top->parent = Node::unbalanced->parent;
        Node::unbalanced->height++;
        Node::unbalanced->parent = new_top;
        new_top->update_nodes_b();
    }
}

void Tree::balance_tree() {
    // Fully balances the tree such that the height_balance for any branch is never more than 1
    if (Node::unbalanced != NULL)
    {
        if (Node::unbalanced->height_balance > 1)
        {
            if (Node::unbalanced->right->height_balance >= 0)
            {
                // Right Right unbalanced
                rotate_left(Node::unbalanced);
            }
            else if (Node::unbalanced->right->height_balance < 0)
            {
                // Right Left unbalanced
                rotate_left(Node::unbalanced->right);
                rotate_right(Node::unbalanced);
            }
        }
        else if (Node::unbalanced->height_balance < 1)
        {

            if (Node::unbalanced->left->height_balance <= 0)
            {
                // Left Left unbalanced
                rotate_right(Node::unbalanced);
            }
            else if (Node::unbalanced->right->height_balance > 0)
            {
                // Left Right unbalanced
                rotate_right(Node::unbalanced->right);
                rotate_left(Node::unbalanced);
            }
        }
        Node::unbalanced = NULL;
    }
}

Node::Node() {
    left = NULL;
    right = NULL;
    parent = NULL;
    content = 0;
    height = 0;
    height_balance = 0;
}

Node::Node(long numInput) {
    left = NULL;
    right = NULL;
    parent = NULL;
    this -> content = numInput;
    height = 0;
    height_balance = 0;
}

bool Node::adjustment = false;
Node *Node::unbalanced = NULL;

void Node::add_left(long content) {
    /*Takes a given number and adds it as the left leaf of a node if that space
    is free. If not, it finds a free space*/
    if (left == NULL) {
        Node *node_ptr = new Node(content);
        left = node_ptr;
        left->height = height + 1;
        height_balance--;
        if (right == NULL) {
            adjustment = true;
        }
        node_ptr->parent = this;
    }
    else {
        if (content < left->content)
        {
            left->add_left(content);
            if (left->height_balance < 0 && adjustment) {
                height_balance--;
            }
            else {
                adjustment = false;
            }
        }
        else if (content > left->content) {
            left->add_right(content);
            if (left->height_balance > 0 && adjustment) {
                height_balance--;
            }
            else {
                adjustment = false;
            }
        }
        else {
            adjustment = false;
        }
        if (height_balance > 1 || height_balance < -1) {
            if (unbalanced == NULL) {
                unbalanced = this;
            }
            else if (height > unbalanced->height) {
                unbalanced = this;
            }
        }
    }
}

void Node::add_right(long content) {
    /*Takes a given number and adds it as the right leaf of a node if that space
    is free. If not, it finds a free space*/
    if (right == NULL) {
        Node *node_ptr = new Node(content);
        right = node_ptr;
        right->height = height + 1;
        height_balance++;
        if (left == NULL) {
            adjustment = true;
        }
        node_ptr->parent = this;
    }
    else {
        if (content < right->content)
        {
            right->add_left(content);
            if (right->height_balance < 0 && adjustment) {
                height_balance++;
            }
            else {
                adjustment = false;
            }
        }
        else if (content > right->content) {
            right->add_right(content);
            if (right->height_balance > 0 && adjustment) {
                height_balance++;
            }
            else {
                adjustment = false;
            }
        }
        else {
            adjustment = false;
        }
        if (height_balance > 1 || height_balance < -1) {
            if (unbalanced == NULL) {
                unbalanced = this;
            }
            else if (height > unbalanced->height) {
                unbalanced = this;
            }
        }
    }
}

void Node::update_nodes_h(long change) {
    height += change;
    if (left != NULL) {
        left->update_nodes_h(change);
    }
    if (right != NULL) {
        right->update_nodes_h(change);
    }
}

void Node::update_nodes_b() {
    if (this == parent->right) {
        parent->height_balance--;
    }
    else {
        parent->height_balance++;
    }
    if (parent->parent != NULL) {
        parent->update_nodes_b();
    }
}