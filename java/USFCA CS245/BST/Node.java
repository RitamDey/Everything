class Node { 

    public Node(Comparable elem, Node lft, Node rght) {
      element = elem;
      left = lft;
      right = rght;
    }

    public Node(Comparable elem) {
      element = elem;
    }

    public Comparable element() {
      return element;
    }

    public Node left() {
      return left;
    }

    public Node right() {
      return right;
    }

    public void setLeft(Node newLeft) {
      left = newLeft;
    }

    public void setRight(Node newRight) {
      right = newRight;
    }

    public void setElement(Comparable elem) {
      element = elem;
    }

    private Comparable element;
    private Node left;
    private Node right;
}
