unsigned long int get_len(Node *list){
    unsigned long int len = 0;
    for(; list; list = list->next)
        len += 1;
    return len;
}

int CompareLists(Node *headA, Node* headB) {
    if(headA == NULL && headB == NULL)
        return 1;
    if((headA && headB == NULL) || (headB && headA == NULL))
        return 0;
    
    if(get_len(headA) != get_len(headB))
        return 0;
    
    int is_same = 0;
    for(;headA && headB; headA = headA->next, headB = headB->next)
        if(headA->data != headB->data)
            return 0;

    return 1;
}

