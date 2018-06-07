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
      ListNode curr = this.head;
      ListNode tmp;

      while(curr.next() != null) {
        if(curr.next().data().equals(elemToRemove)) {
          tmp = curr.next().next();
          curr.setNext(tmp);
          break;
        }
        curr = curr.next();
      }
    }

    /**
    * Remove all occurrences of an element from a list.
    * @param elemToRemove The element to remove from the list
    */
    public void removeAll(Object elemToRemove) {
      ListNode curr = this.head;
      ListNode tmp;

      while(curr != null && curr.next() != null) {
        if(curr.next().data().equals(elemToRemove)) {
          tmp = curr.next().next();
          curr.setNext(tmp);
        }
        else
          curr = curr.next();
      }
    }

    /**
    * Remove the last occurrence of an element from a list.
    * @param elemToRemove The element to remove from the list
    */
    public void removeLast(Object elemToRemove) {
      ListNode toRemove = null;
      ListNode curr = this.head;

      while(curr.next() != null) {
        
        if(curr.next().data().equals(elemToRemove))
          toRemove = curr;
        
        curr = curr.next();
      }

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
          msg += ",";

        curr = curr.next();
      }

      return msg + "]";   // Just so this will compile
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
