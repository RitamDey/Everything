// First submission using C++ mordern features
/
int getCount(struct Node *head) {
    auto curr = head;  // Infers type as Node *
    auto leng = 0;     // Infers type as int

    while (curr) {
        leng++;
        curr = curr->next;
    }

    return leng;
}
