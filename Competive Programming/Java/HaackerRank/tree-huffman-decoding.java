/**
  * Method only submission.
  * The required functionality to implement was Huffman Tree decoder
  * Only the decode function was needed to be implemented

  * class Node
  *		public int frequnecy;
  *		public char data;
  *		public Node left, right;
**/


void decode(String s, Node root) {
	int S_length = S.length();
	int index = 0;
	String result = "";
	char curr;
	Node curr_node = root;

	while(index < S_length) {
		curr = S.charAt(index);
		// System.out.println(curr);
		// System.out.println("Index " + index);

		if(curr == '1')
			curr_node = curr_node.right;
		else
			curr_node = curr_node.left;

		if(curr_node.left == null && curr_node.right == null) {
			result += curr_node.data;
			// System.out.println(curr_node.data);
			curr_node = root;
		}

		index++;
	}

	System.out.println(result);
}
	}
}
