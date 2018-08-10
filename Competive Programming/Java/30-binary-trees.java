import java.util.*;
import java.io.*;


class Node {
    Node left, right;
    int data;

    Node(int data) {
        this.data = data;
        left = right = null;
    }
}


class Solution {
    static void levelOrder(Node root) {
	// Level order traversal is the BFS traversal for a binary tree.
	// Here we process each element in a level from leftmost child to the rigthmost child
        if (root != null) {
	    // Create a queue to store the children of a node in left-to-right fashion
            Queue<Node> q = new LinkedList<>();
	    q.add(root);  // Add the root as it is the level 0

	    while (!q.isEmpty()) {
		// Get the first child
	        Node elem = q.poll();

		// Process it
		System.out.print(elem.data + " ");

		// Store the children from left-to-right.
		// Using queue, the left child will get dequeued first and processed first then the right child.

		if (elem.left != null)
		    q.add(elem.left);

		if (elem.right != null)
	            q.add(elem.right);
	    }
        }

	System.out.println("");
    }

    public static Node insert (Node root, int data) {
        if (root == null) {
            return new Node(data);
        }
        else {
            Node cur;
            if(data<=root.data) {
                cur = insert(root.left,data);
                root.left = cur;
            }
            else {
                cur = insert(root.right,data);
                root.right = cur;
            }
            return root;
        }
    }

    public static void main (String args[]) {
            Scanner sc = new Scanner(System.in);
            int T = sc.nextInt();
            Node root = null;
            while(T-->0) {
                int data = sc.nextInt();
                root = insert(root,data);
            }
            levelOrder(root);
        }
}
