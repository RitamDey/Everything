import java.io.*;

class TreeOps {


    public static int MAX(int x, int y) {
      if (x > y)
        return x;
      else
        return y;
    }

    public static int MIN(int x, int y) {
      if (x < y)
        return x;
      else
        return y;
    }

    public static int height(Node tree) {
      if (tree == null)
        return 0;
      return 1 + MAX(height(tree.left()), height(tree.right()));
    }


    public static int numNodes(Node tree) {
      if (tree == null)
        return 0;
      return 1 + numNodes(tree.left()) + numNodes(tree.right());
    }

    /* Input:  A binary tree, and an element
       Output: true if the element is in the tree, false otherwise */
    public static boolean find(Node tree, Comparable elem) {
      if (tree == null)
        return false;

      if (tree.element().equals(elem))
        return true;

      return find(tree.right(), elem) || find(tree.left(), elem);
    }


    /* Input:  A binary tree  */
    /* Output: The number of leaves in the tree */
    public static int numLeaves(Node tree) {
      if (tree == null)
        return 0;

      if (tree.left() == null && tree.right() == null)
        return 1;

      return numLeaves(tree.right()) + numLeaves(tree.left());
    }

    /* Input: a Binary Tree 
       Output: The depth of the shallowest leaf in the tree,
               (or -1, if the tree is empty)

       shallowestLeaf on
             x
            / \
           x   x
          / \
         x   x

        would return 1, while shallowestLeaf on:
             x
              \
               x
              /
              x
               \
                x
        would return 3  */
    public static int shallowestLeaf(Node tree) {
      if (tree == null)
        return -1;

      if (tree.left() == null && tree.right() == null)
        return 1;

      int leftDist = shallowestLeaf(tree.left());
      int rightDist = shallowestLeaf(tree.right());

      if (leftDist == -1)
        return 1 + rightDist;
      else if (rightDist == -1)
        return 1 + leftDist;
      else
        return 1 + MIN(leftDist, rightDist);
    }


    public static void main(String args[]) throws IOException {
	Node tree1, tree2, tree3;
	BufferedReader br 
	    = new BufferedReader(new InputStreamReader(System.in),1);
	int input;

	tree1 = new Node(new Integer(1),
			 new Node(new Integer(2),
				  new Node(new Integer(3),
					   new Node(new Integer(4),
						    new Node(new Integer(5),
							     null,
							     null),
						    null),
					   null),
				  null),
			 null);
	tree2 = new Node(new Integer(1),
			 new Node(new Integer(2),
				  new Node(new Integer(3),
					   new Node(new Integer(4),
						    null,
						    null),
					   new Node(new Integer(5),
						    null,
						    null)),
				  new Node(new Integer(6),
					   new Node(new Integer(7),
						    null,
						    null),
					   new Node(new Integer(8),
						    null,
						    null))),
			 new Node(new Integer(9),
				  new Node(new Integer(10),
					   new Node(new Integer(11),
						    null,
						    null),
					   new Node(new Integer(12),
						    null,
						    null)),
				  new Node(new Integer(13),
					   new Node(new Integer(14),
						    null,
						    null),
					   new Node(new Integer(15),
						    null,
						    null))));
	tree3 = new Node(new Integer(8),
			 new Node(new Integer(3),
				  new Node(new Integer(2)),
				  new Node(new Integer(4),
					   null,
					   new Node(new Integer(5),
						    null,
						    null))),
			 null);
				 
	System.out.println("Height of tree 1 = " + height(tree1));
	System.out.println("Height of tree 2 = " + height(tree2));
	System.out.println("Height of tree 3 = " + height(tree3));
	System.out.println("numNodes of tree 1 = " + numNodes(tree1));
	System.out.println("numNodes of tree 2 = " + numNodes(tree2));
	System.out.println("numNodes of tree 3 = " + numNodes(tree3));
	System.out.println("numLeaves of tree 1 = " + numLeaves(tree1));
	System.out.println("numLeaves of tree 2 = " + numLeaves(tree2));
	System.out.println("numLeaves of tree 3 = " + numLeaves(tree3));

	System.out.println("Shallowest leaft of tree 1 = " + shallowestLeaf(tree1));
	System.out.println("Shallowest leaft of tree 2 = " + shallowestLeaf(tree2));
	System.out.println("Shallowest leaft of tree 3 = " + shallowestLeaf(tree3));

	System.out.println("Enter number to find in trees:");
	input = Integer.parseInt(br.readLine());

	System.out.println("Finding " + input + " in tree1: " + find(tree1,new Integer(input)));
	System.out.println("Finding " + input + " in tree2: " + find(tree2,new Integer(input)));
	System.out.println("Finding " + input + " in tree3: " + find(tree3,new Integer(input)));
    }

}
