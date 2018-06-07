public class ListNode {
    private Object data;
    private ListNode next;

    public ListNode(Object d) {
        data = d;
        next = null;
    }

    public ListNode(Object data, ListNode next) {
        this.data = data;
        this.next = next;
    }


    public Object data() {
        return data;
    }

    public ListNode next() {
        return next;
    }

    public void setNext(ListNode newNext) {
        this.next = newNext;
    }


    public void setData(Object newData) {
        this.data = newData;
    }
}
