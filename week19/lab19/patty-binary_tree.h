#include<string>
#include"queue.h"
/*
    Name:
    Date: Spring 2023
    Purpose: Implement a pointer-based binary search tree whose content is
        of data type long int.  Implement height-balancing using node 
        rotations.
*/

/* @brief Class to represent one node of a binary search tree. */

class Node {
    friend class Tree;
    public:
        // The lowest unbalanced node in the tree this node is in
        static Node * unbalanced;        
        // Previous adjustment
        static bool adjustment;
        // Pointers to left and right child nodes.
        Node * left;
        Node * right;
        // Pointer to parent node
        Node * parent;
        // The actual content of this node.
        long content;
        // Height of node and balance of height of children branches
        long height;
        long height_balance;
        // Default constructor, assigns 0 as its content.
        Node();
        // Constructor with content.
        Node(long content);
    private:
        /* Methods to add a child node directly to this node.  Intended to 
            be called by Tree::add_node(). */
        void add_left(long content);
        void add_right(long content);
        // Updates node heights for tree balancing
        void update_nodes_h(long change);
        void update_nodes_b();
};

/* @brief Class to represent a binary search tree. */
class Tree {
    friend class Node;
    public:
        // Pointer to the first node of binary search tree.
        Node * head;
        // Default constructor.  Assigns head to be a null pointer.
        Tree();
        /* Add content in the appropriate location, where every Node to its
            left has content smaller than this content, everything to the 
            right has larger content.  Silently ignore duplicated content. */
        void add_node(long content);
        void dump_tree();
        void balance_tree();
        void rotate_right(Node * rotating);
        void rotate_left(Node * rotating);
};