#include<string>
#include "binary_tree.h"

using namespace std;

Node::Node(){
    left = NULL;
    right = NULL;
    parent = NULL;
    content = 0;
    height = 0;
    height_balance = 0;
}

Node::Node(long content){
    left = NULL;
    right = NULL;
    parent = NULL;
    this -> content = content;
    height = 0;
    height_balance = 0;
}

bool Node::adjustment = false;
Node * Node::unbalanced = NULL;

void Node::add_left(long content){
    if (left == NULL){
        Node * node_ptr = new Node(content);
        left = node_ptr;
        left -> height = height + 1;
        height_balance --;
        if (right == NULL){
            adjustment = true;
        }
        node_ptr -> parent = this;
    }
    else{
        if (content < left -> content){
            left -> add_left(content);
            if (left -> height_balance < 0 && adjustment){
                height_balance --;
            }
            else{
                adjustment = false;
            }
        }
        else if (content > left -> content){
            left -> add_right(content);
            if (left -> height_balance > 0 && adjustment){
                height_balance --;
            }
            else{
                adjustment = false;
            }
        }
        else{
            adjustment = false;
        }
        if (height_balance > 1 || height_balance < -1){
            if (unbalanced == NULL){
                unbalanced = this;
            }
            else if (height > unbalanced -> height){
                unbalanced = this;
            }
        }
    }
}

void Node::add_right(long content){
    if (right == NULL){
        Node * node_ptr = new Node(content);
        right = node_ptr;
        right -> height = height + 1;
        height_balance ++;
        if (left == NULL){
            adjustment = true;
        }
        node_ptr -> parent = this;
    }
    else{
        if (content < right -> content){
            right -> add_left(content);
            if (right -> height_balance < 0 && adjustment){
                height_balance ++;
            }
            else{
                adjustment = false;
            }
        }
        else if (content > right -> content){
            right -> add_right(content);
            if (right -> height_balance > 0 && adjustment){
                height_balance ++;
            }
            else{
                adjustment = false;
            }
        }
        else{
            adjustment = false;
        }
        if (height_balance > 1 || height_balance < -1){
            if (unbalanced == NULL){
                unbalanced = this;
            }
            else if (height > unbalanced -> height){
                unbalanced = this;
            }
        }
    }
}

Tree::Tree() {
    head = NULL;
}

void Tree::add_node(long content) {
    Node::adjustment = false;
    if (head == NULL){
        Node * node_ptr = new Node(content);
        head = node_ptr;
        node_ptr -> parent = NULL;
    }
    else{
        if (content < head -> content){
            head -> add_left(content);
        }
        else if (content > head -> content){
            head -> add_right(content);
        }
        balance_tree();
    }

}

void Tree::dump_tree(){
    Queue queue;
    queue.enqueue(reinterpret_cast<long>(head));
    while (queue.size > 0){

        long node_ptr_long = queue.dequeue();
        Node * node_ptr = reinterpret_cast<Node*>(node_ptr_long);

        cout << "content: " << node_ptr -> content;
        cout << " height: " << node_ptr -> height;
        cout << " balance: " << node_ptr -> height_balance << endl;
    

        if(node_ptr -> left != NULL){
            queue.enqueue(reinterpret_cast<long>(node_ptr -> left));
        }
        if(node_ptr -> right != NULL){
            queue.enqueue(reinterpret_cast<long>(node_ptr -> right));
        }
    }
}

void Node::update_nodes_h(long change){
    height += change;
    if (left != NULL){
        left -> update_nodes_h(change);
    }
    if (right != NULL){
        right -> update_nodes_h(change);
    }
}

void Node::update_nodes_b(){
    if (this == parent -> right){
        parent -> height_balance --;
    }
    else{
        parent -> height_balance ++;
    }

    if (parent -> parent != NULL){
        parent -> update_nodes_b();
    }
}

void Tree::rotate_left(Node * rotating){
    if (rotating == head){
        head = rotating -> right;
        head -> height = 0;
        rotating -> right = head -> left;
        head -> left = rotating;
        if (head -> left -> right != NULL){
            head -> left -> right -> height = 2;
        }
        if (rotating -> left != NULL){
            rotating -> left -> update_nodes_h(1);

        }
        if (head -> right != NULL){
            head -> right -> update_nodes_h(-1);
        }
        head -> height_balance = 0;
        head -> left -> height_balance = 0;
        head -> left -> parent = head;
        head -> left -> height = 1;
        head -> parent = NULL;
    }
    else{
        Node * new_top = rotating -> right;
        
        if (rotating -> parent -> right == rotating){
            rotating -> parent -> right = new_top;
        }
        else{
            rotating -> parent -> left = new_top;
        }
        new_top -> height --;
        rotating -> right = new_top -> left;
        new_top -> left = rotating;
        if (new_top -> left -> right != NULL){
            new_top -> left -> right -> parent = new_top -> left;
        }
        if (rotating -> left != NULL){
            rotating -> left -> update_nodes_h(1);

        }
        if (new_top -> right != NULL){
            new_top -> right -> update_nodes_h(-1);
        }
        new_top -> height_balance = 0;
        new_top -> left -> height_balance = 0;
        new_top -> parent = rotating -> parent;
        rotating -> height ++;
        new_top -> left -> parent = new_top;
        new_top -> update_nodes_b();
    }
    
}

void Tree::rotate_right(Node * rotating){
    if (Node::unbalanced == head){
        head = Node::unbalanced -> left;
        head -> height = 0;
        Node::unbalanced -> left = head -> right;
        head -> right = Node::unbalanced;
        if (head -> right -> left != NULL){
            head -> right -> left -> height = 2;
        }
        if (Node::unbalanced -> right != NULL){
            Node::unbalanced -> right -> update_nodes_h(1);

        }
        if (head -> left != NULL){
            head -> left -> update_nodes_h(-1);
        }
        head -> height_balance = 0;
        head -> right -> height_balance = 0;
        head -> right -> parent = head;
        head -> right -> height = 1;
        head -> parent = NULL;
    }
    else{
        
        Node * new_top = Node::unbalanced -> left;
        if (Node::unbalanced -> parent -> right == Node::unbalanced){
            Node::unbalanced -> parent -> right = new_top;
        }
        else{
            Node::unbalanced -> parent -> left = new_top;
        }                
        new_top -> height --;
        Node::unbalanced -> left = new_top -> right;
        new_top -> right = Node::unbalanced;
        if (new_top -> right -> left != NULL){   
            new_top -> right -> left -> parent = new_top -> right;
        }
        if (Node::unbalanced -> right != NULL){
            Node::unbalanced -> right -> update_nodes_h(1);

        }
        if (new_top -> left != NULL){
            new_top -> left -> update_nodes_h(-1);
        }
        new_top -> height_balance = 0;
        new_top -> right -> height_balance = 0;
        new_top -> parent = Node::unbalanced -> parent;
        Node::unbalanced -> height ++;
        Node::unbalanced -> parent = new_top;
        new_top -> update_nodes_b();
    }
}

void Tree::balance_tree(){
    if (Node::unbalanced != NULL){
        if (Node::unbalanced -> height_balance > 1){
            if (Node::unbalanced -> right -> height_balance >= 0){
                // Right Right unbalanced
                rotate_left(Node::unbalanced);
            }
            else if (Node::unbalanced -> right -> height_balance < 0){
                // Right Left unbalanced
                rotate_left(Node::unbalanced -> right);
                rotate_right(Node::unbalanced);
            }
        }
        else if (Node::unbalanced -> height_balance < 1){

            if (Node::unbalanced -> left -> height_balance <= 0){                
                // Left Left unbalanced
                rotate_right(Node::unbalanced);
            }
            else if (Node::unbalanced -> right -> height_balance > 0){
                // Left Right unbalanced
                rotate_right(Node::unbalanced -> right);
                rotate_left(Node::unbalanced);
            }
        }
        Node::unbalanced = NULL;
    }
}
