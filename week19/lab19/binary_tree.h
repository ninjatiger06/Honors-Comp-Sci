#include<string>
/*
    Name: Jonas Pfefferman and Patrick Rooney
    Date: Spring 2023
    Purpose: Implement a pointer-based binary search tree whose content is
        of data type long int.  Implement height-balancing using node 
        rotations.
*/

/* @brief Class to represent one node of a binary search tree. */
class Node {
    friend class Tree;
    public:
        // Pointers to left and right child nodes.
        Node * left;
        Node * right;
        // The actual content of this node.
        long content;
        // Total height (number of levels of descendants) descendant nodes on each branch.
        long height;
        long height_balance;
        // Default constructor, assigns 0 as its content.
        Node();
        // Constructor with content.
        Node(long numInput);
    private:
        /* Methods to add a child node directly to this node.  Intended to 
            be called by Tree::add_node(). */
        void add_left(long content);
        void add_right(long content);
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
        void delete_node(long delNode, Node* currNode);
        void dump_tree();
        void depth_dump(Node* currNode);
        bool search_tree(long num, Node* currNode);
};