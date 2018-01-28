using System;

namespace LinkedList {
	/// <summary>
	/// A node in the LinkedList
	/// </summary>
	/// <typeparam name="T"></typeparam>
	public class LinkedListNode<T> {
		/// <summary>
		/// Constructs a new node with a specified value.
		/// </summary>
		/// <param name="value"></param>
		public LinkedListNode(T value) {
			Value = value;
		}

		/// <summary>
		/// The node value
		/// </summary>
		public T Value { get; set; }

		/// <summary>
		/// The next node in the Linked List (null if last node)
		/// </summary>
		public LinkedListNode<T> Next { get; set; }
	}
}