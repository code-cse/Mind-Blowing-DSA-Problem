#include <iostream>

using namespace std;

struct Node{
  int data;
  Node *next;
};

class linked_list{
  
  private:
    Node *head,*tail;
  
  public:
    linked_list(){
        head = NULL;
        tail = NULL;
    }

    void add_node(int new_data){
        Node *tmp = new Node;
        tmp->data = new_data;
        tmp->next = NULL;

        if(head == NULL){
            head = tmp;
            tail = tmp;
        }
        else{
            tail->next = tmp;
            tail = tail->next;
        }
    }

    void display(){
        Node *tmp;
        tmp = head;
        while (tmp != NULL){
            cout << tmp->data << endl;
            tmp = tmp->next;
        }
    }
};

int main(){
    linked_list a;
    a.add_node(1);
    a.add_node(2);
    a.display();
    return 0;
}
