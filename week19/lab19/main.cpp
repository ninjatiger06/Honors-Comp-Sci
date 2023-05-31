#include<iostream>
#include "binary_tree.h"
#include <typeinfo>

/*
    Name: Jonas Pfefferman and Patrick Rooney
    Date: May 2023
    Purpose: Creates a binary tree and tests basic functionality
*/

using namespace std;

int main() {
    Tree tree;
    long contents [] = {13, 44, 58, 8, 1, 21, 60, 56, 87, 36, 6, 45, 90, 30, 61, 90, 18, 6, 60, 11};
    for (int i=0; i<20; i++) {
        cout << "Adding node with content " << contents[i] << endl;
        tree.add_node(contents[i]);
    }
    tree.dump_tree();
    tree.depth_dump(tree.head);
    bool numFound = tree.search_tree(44, tree.head);
    cout << "num: " << 44 << " numFound: " << numFound << endl;

    // prints as either a 1 or 0, but numFound is in fact a bool
    cout << typeid(numFound).name() << endl;
    
    numFound = tree.search_tree(99, tree.head);
    cout << "num: " << 99 << " numFound: " << numFound << endl;

    // tree.delete_node(21, tree.head);
    tree.dump_tree();
    tree.draw_tree();

    tree.balance_tree();
    
    tree.dump_tree();
    tree.draw_tree();
}