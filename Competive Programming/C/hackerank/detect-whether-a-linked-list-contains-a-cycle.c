int has_cycle(SinglyLinkedListNode* head) {
    // Using the Floyd Cycle Detection Algorithm
    SinglyLinkedListNode *slow_p = head;
    SinglyLinkedListNode *fast_p = head->next;
    
    while (fast_p != NULL) {
        slow_p = slow_p->next;
        fast_p = fast_p->next;
        
        if (fast_p)
            fast_p = fast_p->next;
        
        if (slow_p == fast_p)
            return 1;
    }
    
    return 0;
}
