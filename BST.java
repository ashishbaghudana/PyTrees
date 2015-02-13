package datastructures;

import java.util.NoSuchElementException;

/**
 * The <b>BST</b> class implements a dynamic Binary Search Tree that includes insert, delete, search and 
 * other ordered operations such as finding the floor and ceiling of a key, deleting the node with the minimum or maximum
 * key value in the tree, and also finds an in-order traversal of the elements in the tree.
 * @author Ashish
 *
 * @param <Key> the type of the keys in the BST
 * @param <Value> the type of the values in the BST
 */
public class BST<Key extends Comparable<Key>, Value>
{

	Node root; //the root of the binary search tree
	
	/**
	 * A private helper class for the Binary Search Tree
	 * @author Ashish
	 *
	 */
	private class Node
	{
		private Key key;
		private Value value;
		private Node left, right;
		private int N;
		
		/**
		 * Creates a new node with the associated key value pair and sets the size of the tree rooted at
		 * the node to a specified value
		 * @param key the key of the node
		 * @param value the value at the node
		 * @param N the size of the subtree rooted at the node
		 */
		public Node(Key key, Value value, int N)
		{
			this.key = key;
			this.value = value;
			this.N = N;
		}
	}
	
	/**
	 * Determines if the tree is empty or not
	 * @return true if the tree is empty, false otherwise
	 */
	public boolean isEmpty()
	{
		return root == null;
	}
	
	/**
	 * Returns the number of key-value pairs in the Binary Search Tree
	 * @return the size of the binary search tree
	 */
	public int size()
	{
		return size(root);
	}
	
	/**
	 * Returns the number of key-value pairs in the binary search tree rooted at a given node
	 * @param x the node acting as the root of the BST whose size is to be determined
	 * @return the size of the Binary Search Tree rooted at the given node
	 */
	private int size(Node x)
	{
		if(x==null)
			return 0;
		return x.N;
	}
	
	/**
	 * Finds and returns the value associated with a given key in the Binary Search Tree
	 * @param key The key whose associated value is to be found
	 * @return null if the BST does not contain the given key-value pair, the associated value otherwise
	 */
	public Value get(Key key)
	{
		return get(root, key);
	}
	
	/**
	 * Finds and returns the value associated with a given key in the Binary Search Tree rooted at a given node
	 * @param x the node that acts as the root of the BST
	 * @param key the key whose associated value is to be returned
	 * @return null if the key does not exist in the BST, the associated value otherwise
	 */
	private Value get(Node x, Key key)
	{
		if(x==null)
			return null;
		int compare = key.compareTo(x.key);
		if(compare==0)
			return x.value;
		else if(compare<0)
			return get(x.left, key);
		else
			return get(x.right, key);
	}
	
	/**
	 * Determines if a given key is present in the Binary Search Tree
	 * @param key the key whose existence is to be determined
	 * @return true if the key exists in the BST, false otherwise
	 */
	public boolean contains(Key key)
	{
		return get(key)!=null;
	}
	
	/**
	 * Inserts a key-value pair into the Binary Search Tree. Updates the value in the node if the key already exists.
	 * @param key The key whose value has to be updated or added
	 * @param value The value to be added to the Binary Search Tree
	 */
	public void put(Key key, Value value)
	{
		root = put(root, key, value);
	}
	
	/**
	 * A helper function that recursively adds a key value pair to the BST
	 * @param x the root of the tree to which the key value pair has to be added or updated
	 * @param key the key whose associated value has to be added or updated in the tree
	 * @param value the value to be added to the node with the associated key
	 * @return the updated node x
	 */
	private Node put(Node x, Key key, Value value)
	{
		if (x == null) 
			return new Node(key, value, 1);
        int cmp = key.compareTo(x.key);
        if      (cmp < 0) 
        	x.left  = put(x.left,  key, value);
        else if (cmp > 0) 
        	x.right = put(x.right, key, value);
        else             
        	x.value   = value;
        x.N = 1 + size(x.left) + size(x.right);
        return x;
	}
	
	/**
	 * Deletes the nose associated with the smallest key value in the Binary Search Tree
	 */
	public void deleteMin()
	{
		if(isEmpty())
			throw new NoSuchElementException();
		root = deleteMin(root);
	}
	
	/**
	 * Deletes the nose associated with the smallest key value in the Binary Search Tree rooted at x
	 * @param x the root of the tree from which the node has to be removed
	 * @return
	 */
	private Node deleteMin(Node x)
	{
		if(x.left==null)
			return x.right;
		x.left = deleteMin(x.left);
		x.N = 1 + size(x.left) + size(x.right);
		return x;
	}
	
	/**
	 * Deletes a node with the given key from the Binary Search Tree
	 * @param key the key whose associated node has to be deleted
	 */
	public void delete(Key key)
	{
		root = delete(root, key);
	}
	
	/**
	 * Deletes a node with the given key from the Binary Search Tree rooted at a given node
	 * @param x the node that acts as the root of the subtree
	 * @param key the key whose associated value is to be deleted
	 * @return the node which has been altered
	 */
	private Node delete(Node x, Key key)
	{
		if(x==null)
			return null;
		int compare = key.compareTo(x.key);
		if(compare<0)
			x = delete(x.left, key);
		else if(compare>0)
			x = delete(x.right, key);
		else
		{
			if(x.left==null)
				return x.right;
			if(x.right==null)
				return x.left;
			Node node = x;
			x = min(node.right);
			x.right = deleteMin(node.right);
			x.left = node.left;
		}
		x.N = size(x.left) + size(x.right) + 1;
		return x;
	}
	
	
	/**
	 * Returns the minimum key in the Binary Search Tree
	 * @return the smallest key in the given BST
	 */
	public Key min()
	{
		if(isEmpty())
			throw new NoSuchElementException();
		return min(root).key;
	}

	/**
	 * A helper function that returns the smallest key in the subtree rooted at a given node
	 * @param x the root node of the subtree
	 * @return the smallest key in the subtree rooted at node x
	 */
	private Node min(Node x)
	{
		if(x.left==null)
			return x;
		return min(x.left);
	}
	
	/**
	 * Returns the maximum key in the Binary Search Tree
	 * @return the largest key in the given BST
	 */
	public Key max()
	{
		if(isEmpty())
			throw new NoSuchElementException();
		return max(root).key;
	}
	
	/**
	 * A helper function that returns the largest key in the subtree rooted at a given node
	 * @param x the root node of the subtree
	 * @return the largest key in the subtree rooted at node x
	 */
	private Node max(Node x)
	{
		if(x.right==null)
			return x;
		return max(x.right);
	}
	
	/**
	 * Finds the floor of a given key in the Binary Search Tree
	 * @param k the k whose floor is to be found
	 * @return null if the floor doesn't exist in the BST, the floor of the key otherwise
	 */
	public Key floor(Key k)
	{
		Node node = floor(root, k);
		if(node==null)	
			return null;
		return node.key;
	}
	
	/**
	 * A helper function that recursively finds the floor of a given key in the Binary Search Tree
	 * @param k the k whose floor is to be found
	 * @return null if the floor doesn't exist in the BST, the node with the floor of the key otherwise
	 */
	private Node floor(Node x, Key k)
	{
		if(x==null)
			return null;
		int compare = k.compareTo(x.key);
		if(compare==0)
			return x;
		else if(compare<0)
			return floor(x.left, k);
		Node node = floor(x.right, k);
		if(node==null)
			return null;
		else
			return node;
	}
	
	/**
	 * Finds the ceiling of a given key in the Binary Search Tree
	 * @param k the k whose ceiling is to be found
	 * @return null if the ceiling doesn't exist in the BST, the ceiling of the key otherwise
	 */
	public Key ceil(Key key)
	{
		Node node = ceil(root, key);
		if(node==null)
			return null;
		else
			return node.key;
	}
	
	/**
	 * A helper function that recursively finds the ceiling of a given key in the Binary Search Tree
	 * @param k the k whose ceiling is to be found
	 * @return null if the ceiling doesn't exist in the BST, the node with the ceiling of the key otherwise
	 */
	private Node ceil(Node x, Key key)
	{
		if(x==null)
			return null;
		int compare = key.compareTo(x.key);
		if(compare==0)
			return x;
		else if(compare<0)
		{
			Node node = ceil(x.left, key);
			if(node==null)
				return null;
			else
				return x;
		}
		return ceil(x.right, key);
	}
	
	/**
	 * Computes the height of the Binary Search Tree.
	 * A one-node tree has height zero
	 * @return the height of the BST
	 */
	public int height()
	{
		return height(root);
	}
	
	/**
	 * Computes the height of the Binary Search Tree rooted at a given node
	 * @param x the node that acts as the root of the tree
	 * @return the height of the BST
	 */
	private int height(Node x)
	{
		if(x==null)
			return -1;
		return 1 + Math.max(height(x.left), height(x.right));
	}
	
	/**
	 * Returns an iterator over the keys in the Binary Search Tree in order
	 * @return an in-order iterator over the keys in the BST
	 */
	public Iterable<Key> inOrderTraversal()
	{
		QueueLinkedList<Key> keys = new QueueLinkedList<Key>();
		QueueLinkedList<Node> queue = new QueueLinkedList<Node>();
		queue.enqueue(root);
		while(!queue.isEmpty())
		{
			Node node = queue.dequeue();
			if(node==null)
				continue;
			if(node.left!=null) queue.enqueue(node.left);
			if(node.right!=null) queue.enqueue(node.right);
			keys.enqueue(node.key);
		}
		return keys;
	}
	
	/**
	 * Driver method to test the BST class
	 * @param args
	 */
	public static void main(String[] args)
	{
		// TODO Auto-generated method stub
		BST<Character, Integer> st = new BST<Character, Integer>();
        String input = "TESPME";
        for(int i=0;i<input.length();i++)
        	st.put(input.charAt(i), i);

        /*for (Character s : st.inOrderTraversal())
            System.out.println(s + " " + st.get(s));*/
        for(int i=0;i<input.length();i++)
        	System.out.println(input.charAt(i) + " " + st.get(input.charAt(i)));

        System.out.println(st.get('P'));
        System.out.println();
	}

}
