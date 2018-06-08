public class LinkedList {
    private ListNode head;
    private ListNode tail;

    LinkedList() {
        head = new ListNode(null);
        tail = head;
    }

    /**
    * Add an element to the end of the list
    * @param o The object to add to the end of the list
    */
    public void add(Object o) {
        tail.setNext(new ListNode(o));
        tail = tail.next();
    }

    /**
    * Remove the first occurrence of elemToRemove from the list.
    * If elemToRemove does notappear in the list, then do nothing.
    * @param elemToRemove The element to remove from the list
    */
    public void removeFirst(Object elemToRemove) {
      ListNode curr = this.head;  // Tracks current element
      boolean broke = false;  // Tracks if the node was found in the middle or not

      // Execute until the last element
      while(curr.next() != null) {
        /**
        * If the current's next element is the element to remove
        * Then set the current element's next to be next element of the node to be deleted
        * And set the flag to indicate that the element was found in the middle
        */ 
        if(curr.next().data().equals(elemToRemove)) {
          curr.setNext(curr.next().next());
          broke = true;
          break;
        }

        // Advance the node to the next node
        curr = curr.next();
      }

      /**
      * If the flag is false then the removed element was the last element in the list
      * And the current now points to the last element in the list.
      * So update the tail pointer accordingly.
      */
      if(broke == false)
        this.tail = curr;
    }

    /**
    * Remove all occurrences of an element from a list.
    * @param elemToRemove The element to remove from the list
    */
    public void removeAll(Object elemToRemove) {
      ListNode curr = this.head;  // Tracks the current node

      // Iterate until we are at the tail node
      while(curr.next() != null) {
        /**
        * If the next node's data is the same as the element we want to remove
        * then update the current node's next pointer to point to the next node's next
        * Also here we only move to next node when any removals have not been performed
        * becuase the new node placed can also be the node to be removed next
        */
        if(curr.next().data().equals(elemToRemove))
          curr.setNext(curr.next().next());
        else
          // If any removal has not been done then move to the next node.
          curr = curr.next();
      }

      /**
      * When we return here, the curr already points to the tail node
      * So update the tail pointer with the curr value
      */
      this.tail = curr;
    }

    /**
    * Remove the last occurrence of an element from a list.
    * @param elemToRemove The element to remove from the list
    */
    public void removeLast(Object elemToRemove) {
      // Used to track the node to be removed. The final value points to the last node marked for removal
      ListNode toRemove = null;
      ListNode curr = this.head;  // Tracks the current node

      // Iterate the whole list and look for matching elements and update toRemove reference
      while(curr.next() != null) {
        
        /**
        * If the current's next node's value is same as the element we wish to remove
        * Then update the toRemove with the reference
        */
        if(curr.next().data().equals(elemToRemove))
          toRemove = curr;
        
        curr = curr.next();  // Move to the next node
      }

      /**
      * When the node to be removed is the tail node itself
      * Then we first perform the removal and update the tail pointer
      * If not then we leave the tail as it is because it was not touched
      */
      if(curr == toRemove.next()) {
        toRemove.setNext(null);  // Perform the removal
        // The update the tail pointer with the same reference as the toRemove
        this.tail = toRemove;
      }
      else
        // Normal removal of node incase the node removed was not the tail pointer
        toRemove.setNext(toRemove.next().next());
    }

    /**
    * Create a string representation of the list.  The created string will begin with '[' and
    * end with ']', and contain the toString representation of all elements in the list,
    * separated by commas.  So, if the list contains the first 3 positive integers, then
    * toString would return the string "[1, 2, 3]"
    */
    public String toString() {
      String msg = "[";
      ListNode curr = this.head.next();

      while(curr != null) {
        msg += curr.data().toString();

        if(curr.next() != null)
          msg += ", ";

        curr = curr.next();
      }

      return msg + "]";
    }



    public static void main(String args[]) {

        LinkedList L  = new LinkedList();
        
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 5; j++) {
            L.add(j);
            }
        }

        System.out.println(L);
        L.removeFirst(1);
        System.out.println(L);
        L.removeFirst(0);
        System.out.println(L);
        L.removeLast(3);
        System.out.println(L);
        L.removeLast(4);
        System.out.println(L);
        L.add(5);
        System.out.println(L);
        L.removeAll(0);
        System.out.println(L);
        L.removeAll(5);
        System.out.println(L);

        L = new LinkedList();
        for (int i = 0; i < 10; i++) {
            L.add(1);
        }

        System.out.println(L);
        L.removeAll(1);
        System.out.println(L);
        L.add(2);
        System.out.println(L);
    }
}
