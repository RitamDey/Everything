/**
  * Insert a Node in a doubly sorted linked list.
  * After each insertion, the list should be sorted

  * Node is defined as
  * struct Node {
  *     int data;
  *     Node *next;
  *     Node *prev;
  * }

  * This was a method only submission
**/
Node *SortedInsert(Node *head, int data) {
    Node *node = (Node *)malloc(sizeof(Node));
    node->data = data;

    if(head == NULL) {
        node->next = NULL;
        node->prev = NULL;
        return node;
    }

    if(data < head->data) {
        node->next = head;
        head->prev = node;
        return node;
    }

    Node *tmp = head;

    while(tmp->next) {
        // Increment only until we find the position to
        // insert the new node in the next position
        if(data > tmp->data && tmp->next->data > data)
            break;
        tmp = tmp->next;
    }

    node->next = tmp->next;
    node->prev = tmp;
    tmp->next = node;
    tmp->next->prev = node;

    return head;
}
