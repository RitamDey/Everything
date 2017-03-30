#include <iostream>
#include <malloc.h>
using namespace std;

typedef struct Node {
    int data;
    struct Node *next;
}Node;


Node *insert(Node *head, int data, int position){
    if(position==0){
        Node *tmp = (Node *)malloc(sizeof(Node));
        tmp->data = data;
        tmp->next = head;
        return tmp;
    }

    Node *prev, *curr=head;
    for(int pos=1; pos<=position; ++pos){
        prev = curr;
        curr = curr->next;
    }

    prev->next = (Node *)malloc(sizeof(Node));
    prev->next->data = data;
    prev->next->next = curr;

    return head;
}



int main(){
    Node *list = NULL;
    int test;
    cin>>test;

    for(int x=1; x<=test; ++x){
        int data, pos;
        cin>>data>>pos;
        list = insert(list, data, pos);
    }

    for(Node *curr=list; curr; curr = curr->next)
        cout<<curr->data;
    cout<<endl;
    return 0;
}
