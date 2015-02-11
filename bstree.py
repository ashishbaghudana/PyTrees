# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 14:31:00 2015

@author: Ashish
This library builds a Binary Search Tree that supports
the following functions:
a. Search
b. Insert
c. Delete
d. Get minimum value
e. Get maximum value
f. Inorder successor
g. Inorder predecessor
"""

import collections
import sys

class Node:
    """Represents a node in a Binary Search Tree"""
    
    def __init__(self, key, value):
        """
        Default Constructor for Node
        @type key: Float, Integer or Long
        @param key: Key
        @type value: Any Type
        @param value: Value
        """
        self.left = None
        self.right = None
        self.parent = None
        self.key = key
        self.value = value
    
class BSTree:
    """BSTree implements an unbalanced Binary Search Tree.
    
    A binary search tree is an ordered node based tree key structure in which 
    each node has at most two children.
    """
    
    def __init__(self, *args):
        
        self.Root = None
        
        if len(args)==1:
            if isinstance(args, collections.Iterable):
                for x in args[0]:
                    self.insert(x[0], x[1])
            else:
                raise TypeError(str(args[0]) + " is not Iterable")
    
    def get_LCA(self, node1, node2, *args):
        """
        This method gets the lowest common ancestor of
        """
        
        if not isinstance(node1, Node):
            raise TypeError(str(node1)+" is not of type Node")
        if not isinstance(node2, Node):
            raise TypeError(str(node2)+" is not of type Node")
            
        if (len(args)==0):
            root = self.Root
        else:
            root = args[0]
        
        if ((root.key <= node1.key and root.key => node2.key) 
        or (root.key => node1.key and root.key <= node2.key)):
            return root
        elif (root.key < node1.key and root.key < node2.key):
            return self.get_LCA(node1, node2, root.right)
        else: 
            return self.get_LCA(node1, node2, root.left)
            
    
    def get_node(self, key, *args):
        
        if len(args)==0:
            start = self.Root
        else:
            start = args[0]
            
        if not start:
            return None
        if key == start.key:
            return start
        elif key>start.key:
            return self.get_node(key, start.right)
        else:
            return self.get_node(key, start.left)
    
    def insert(self, key, value, *args):
        """
        Insert a value with a key into the BST
        @type key: Float, Integer or Long
        @param key: Key
        @type value: Any Type
        @param value: Value
        @type args: Node
        @param args: The root at which a particular key and value must be inserted
        """
        
        if not isinstance(key, (int, float, long)):
            """Checks if key is of the type (int, float, long). 
            If not, raises TypeError
            """
            raise TypeError(str(key) + " is not a number")
       
        else:
            if not self.Root:
                """
                If self.Root == None, create the Node with key and value.
                """
                self.Root = Node(key, value)
            elif len(args)==0:
                """
                If no arguments are specified, consider the root of the
                tree as the root to insert a Node at.
                """
                if not self.get_node(key, self.Root):
                    """
                    Ensures that a Node with the same key does not
                    already exist in the tree.
                    """
                    self.insert(key, value, self.Root)
            else:
                #Create a Node with key and value as parameters.
                child = Node(key, value)
                
                #Parent defined as the specified argument or root as default                
                parent = args[0]
                
                """
                If the child's key is lesser than the parent's key,
                insert child to the left of the parent.
                
                Else if the child's key is greater than the parent's key,
                insert child to the right of the parent.
                
                """
                if child.key<parent.key:
                    if not parent.right:
                        parent.right = child
                        child.parent = parent
                    else:
                        self.insert(key, value, parent.right)
               
                else:
                    if not parent.left:
                        parent.left = child
                        child.parent = parent
                    else:
                        self.insert(key, value, parent.left)

    def insert_from(self, seq):
        """
        T.insert_from(seq). For every key value pair in seq, 
        insert a new node into T
        """
        
        if isinstance(seq, collections.Iterable):
            for x in seq:
                self.insert(x[0], x[1])
        else:
            raise TypeError(str(iter) + " is not Iterable")
            
    def get_max(self, *args):
        if len(args)==0:
            root = self.Root
        else:
            root = args[0]
            
        if (not root.right):
            return root
        else:
            return self.get_max(root.right)
            
    def get_min(self, *args):
        if len(args)==0:
            root = self.Root
        else:
            root = args[0]
            
        if (not root.left):
            return root
        else:
            return self.get_min(root.left)
    
    def inorder(self, *args):
        if len(args)==0:
            elements = []
            root = self.Root
        else:
            if not isinstance(args[0], Node):
                raise TypeError("Arguments specified are not of the correct type")
            else:
                elements = args[1]
                root = args[0]
                
        if root.left:
            self.inorder(root.left)
            
        elements.append(root)
        
        if root.right:
            self.inorder(root.right)
            
        return elements
        
    def preorder(self, *args):
        if len(args)==0:
            elements = []
            root = self.Root
        else:
            if not isinstance(args[0], Node):
                raise TypeError("Arguments specified not of correct type")
            else:
                elements = args[1]
                root = args[0]
        
        elements.append(root)
        
        if root.left:
            self.preorder(root.left, elements)
        if root.right:
            self.preorder(root.right, elements)
            
        return elements
        
    def postorder(self, *args):
        if len(args)==0:
            elements = []
            root = self.Root
        else:
            if not isinstance(args[0], Node):
                raise TypeError("Arguments specified not of correct type")
            else:
                elements = args[1]
                root = args[0]

        if root.left:
            self.postorder(root.left, elements)
        if root.right:
            self.postorder(root.right, elements)
        
        elements.append(root)
        
    def get_successor(self, key):
        node = self.get_node(key)
        if node:
            if node.right:
                return self.get_min(node.right)
            else:
                parent = node.parent
                if parent:
                    while (node==parent.left):
                        node = parent
                        parent = node.parent
                    return parent
                else:
                    return None
    
    def get_predecessor(self, key):
        node = self.get_node(key)
        if node:
            if node.left:
                return self.get_max(node.left)
            else:
                parent = node.parent
                if parent:
                    while (node==parent.right):
                        node = parent
                        parent = node.parent
                    return parent
                else:
                    return None
    
    
    def delete(self, key):
        """
        Delete node from BST. Check if the node exists.
        If the node exists, checks if the node is a leaf node,
        node with one child or node with two children.
        """
        node = self.get_node(key, self.Root)
        
        if node:
            if not (node.left or node.right):
                self._delete_leaf(node)
            elif not (node.left and node.right):
                self._delete_leaf_parent(node)
            else:
                self._delete_node(node)

    def _delete_leaf(self, node):
        """
        Delete node from BST, treating it as a leaf node.
        """
        parent = node.parent
        if parent:
            if parent.left==node:
                parent.left = None
            if parent.right==node:
                parent.right = None
        del node
        
    def _delete_leaf_parent(self, node):
        """
        Delete node from BST, treating it as a node with just one child.
        """
        parent = node.parent
        
        if node.key == self.Root.key:
            if node.right:
                self.Root = node.right
                node.right = None
                node.right.parent = None
            else:
                self.Root = node.left
                node.left = None
                node.left.parent = None
                
        else:
            if node.left:
                if parent.left == node:
                    parent.left = node.left
                    node.left.parent = parent
                    node.left = None
                else:
                    parent.right = node.left
                    node.left.parent = parent
                    node.left = None
                    
            else:
                if parent.right == node:
                    parent.right = node.right
                    node.right.parent = parent
                    node.right = None
                else:
                    parent.left = node.right
                    node.right.parent = parent
                    node.right = None
                    
        del node
        
    def _delete_node(self, node):
        """
        Delete node as if it has two children.
        """
        switch = self.get_max(node.left)
        self._switch_nodes(node, switch)
        
        if not (switch.right or switch.left):
            to_delete = self.get_max(node.left)
            self._delete_leaf(to_delete)
        else:
            to_delete = self.get_max(node.left)
            self._delete_leaf_parent(to_delete)
    

    def is_valid(self, *args):
        if (len(args)==0):
            node = self.Root
            max_value = sys.maxint
            min_value = -sys.maxint
        else:
            node = args[0]
            min_value = args[1]
            max_value = args[2]
        
        if (node.key > min_value and
            node.key < max_value and
            self.is_valid(node.left, min_value, node.key) and
            self.is_valid(node.right, node.key, max_value)):
                return True
        else:
            return False
        
        
    def _switch_nodes(self, node1, node2):
        switch1 = node1;
        switch2 = node2;
        temp_key = switch1.key
        temp_value = switch1.value
        
        if (switch1.key == self.Root.key):
            self.Root.key = node2.key
            self.Root.value = node2.value
            switch2.key = temp_key
            switch2.value = temp_value
            
        elif (switch2.key == self.Root.key):
            switch1.key = self.Root.key
            self.Root.key = temp_key
            self.Root.value = temp_value
        
        else:
            switch1.key = node2.key
            switch1.value = node2.value
            switch2.key = temp_key
            switch2.value = temp_value
            
        
        