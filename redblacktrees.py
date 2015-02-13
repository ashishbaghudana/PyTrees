# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 14:10:50 2015

@author: Ashish
"""

import collections
from bstree import Node
from bstree import BSTree

class RBNode(Node):
    def __init__(self,key,value):
        Node.__init__(self,key,value)
        self.color = 'r'

class RBTree(BSTree):
    def __init__(self,*args):
		BSTree.__init__(self,*args)

    def _get_all_leaf_paths(self):
        all_leafpaths = []
        nodelist = self.preorder()
        for node in nodelist:
            all_leafpaths.append(self._get_all_leaf_paths_from(node))
        return all_leafpaths

    def _get_all_leaf_paths_from(self,node, acc=[]):
        leafpaths = []

        if not node.left and not node.right:
            leafpaths.append([node]+acc)

        if node.left:
            for leaf_path in self._get_all_leaf_paths_from(node.left, [node]+acc):
                leafpaths.append(leaf_path)
        if node.right:
            for leaf_path in self._get_all_leaf_paths_from(node.right, [node]+acc):
                leafpaths.append(leaf_path)

        return leafpaths

    def is_valid(self,*args):
        if len(args) == 0:
            node = self.Root
            all_leafpaths = self._get_all_leaf_paths()
            for leafpaths in all_leafpaths:
                black_count_list = []
                for path in leafpaths:
                    black_count = 0
                    for node in path:
                        if node.color == 'k':
                            black_count = black_count + 1
                    black_count_list.append(black_count)

                if not black_count_list[1:] == black_count_list[:-1]:
                    raise Exception("Not all simple paths in  " + str(self) + " have same amount of black nodes!")

        else:
            node = args[0]

        if not node:
            return True

        if node.left:
            if not node.left.parent == node:
                raise Exception("Left child of node " + str(node.key) + " is adopted by another node!")

        if node.right:
            if not node.right.parent == node:
                raise Exception("Right child of node " + str(node.key) + " is adopted by another node!")

        if node.parent and node.parent.left == node:
            if node.key > node.parent.key:
                raise Exception("Node " + str(node.key) + " is to the left of " + str(node.parent.key) + " but is larger")

        if node.parent and node.parent.right == node:
            if node.key < node.parent.key:
                raise Exception("Node " + str(node.key) + " is to the right of " + str(node.parent.key) + " but is smaller")

        if node.color == 'r':
            if ((node.left and node.left.color == 'r') or
                (node.right and node.right.color == 'r')):
                    raise Exception("Node " + str(node.key) + " is red and has a red child!")

        return (self.is_valid(node.left) and self.is_valid(node.right))

    def preorder(self,*args):
        return BSTree.preorder(self,*args)

    def inorder(self,*args):
        return BSTree.inorder(self,*args)

    def postorder(self,*args):
        return BSTree.postorder(self,*args)

    def levelorder(self):
        return BSTree.levelorder(self,*args)

    def get_node(self,key,*args):
        return BSTree.get_node(self,key,*args)

    def _rotate_left(self,pivot):
        old_root = pivot
        par_node = old_root.parent

        new_root = old_root.right
        temp = new_root.right
        old_root.right = new_root.left

        if (old_root.right):
            old_root.right.parent = old_root
        new_root.left = old_root
        old_root.parent = new_root

        if par_node is None:
            self.Root = new_root
            self.Root.parent = None
        else:
            if par_node.right and par_node.right.key == old_root.key:
                par_node.right = new_root
                new_root.parent = par_node
            elif par_node.left and par_node.left.key == old_root.key:
                par_node.left = new_root
                new_root.parent = par_node

    def _rotate_right(self,pivot):
        if not pivot.left:
            pass

        else:

            old_root = pivot
            par_node = old_root.parent

            new_root = old_root.left
            temp = new_root.left
            old_root.left = new_root.right

            if (old_root.left):
                old_root.left.parent = old_root

            new_root.right = old_root
            old_root.parent = new_root

            if par_node is None:
                self.Root = new_root
                self.Root.parent = None
            else:
                if par_node.right and par_node.right.key == old_root.key:
                    par_node.right = new_root
                    new_root.parent = par_node
                elif par_node.left and par_node.left.key == old_root.key:
                    par_node.left = new_root
                    new_root.parent = par_node

    def _insert_case_one(self,child):
        node = child
        par_node = node.parent

        if not par_node:
            self.Root.color = 'k'
        else:
            self._insert_case_two(node)

    def _insert_case_two(self,child):
        node = child
        par_node = node.parent

        if par_node.color == 'r':
            self._insert_case_three(node)

    def _insert_case_three(self,child):
        node = child
        par_node = node.parent
        grand_node = par_node.parent
        if grand_node.left == par_node:
            uncle = grand_node.right
        else:
            uncle = grand_node.left

        if uncle and uncle.color == 'r':
            grand_node.color = 'r'
            par_node.color = 'k'
            uncle.color = 'k'
            self._insert_case_one(grand_node)
        else:
            self._insert_case_four(node)

    def _insert_case_four(self,child):
        node = child
        par_node = node.parent
        grand_node = par_node.parent
        if grand_node.left == par_node:
            uncle = grand_node.right
        else:
            uncle = grand_node.left

        if grand_node.left == par_node and par_node.right == node:
                self._rotate_left(par_node)
                node = node.left
        elif grand_node.right == par_node and par_node.left == node:
                self._rotate_right(par_node)
                node = node.right

        self._insert_case_five(node)

    def _insert_case_five(self,child):
        node = child
        par_node = node.parent
        grand_node = par_node.parent
        if grand_node.left == par_node:
            uncle = grand_node.right
        else:
            uncle = grand_node.left

        if par_node.left == node:
                grand_node.color = 'r'
                par_node.color = 'k'
                self._rotate_right(grand_node)
        elif par_node.right == node:
                grand_node.color = 'r'
                par_node.color = 'k'
                self._rotate_left(grand_node)

    def insert(self,key,value,*args):
        if not isinstance(key,(int,long,float)):
            raise TypeError(str(key) + " is not a number")
        else:
            if not self.Root:
                self.Root = RBNode(key,value)
                self.Root.color = 'k'
            elif len(args) == 0:
                if not self.get_node(key,self.Root):
                        self.insert(key,value,self.Root)

            else:
                child = RBNode(key,value)
                parent = args[0]
                if child.key > parent.key:
                    if not parent.right:
                        parent.right = child
                        child.parent = parent
                        if parent.color == 'r':
                            self._insert_case_one(child)
                    else:
                        self.insert(key,value,parent.right)
                else:
                    if not parent.left:
                        parent.left = child
                        child.parent = parent
                        if parent.color == 'r':
                            self._insert_case_one(child)
                    else:
                        self.insert(key,value,parent.left)

    def insert_from(self,seq):
        BSTree.insert_from(self,seq)

    def get_max(self,*args):
        return BSTree.get_max(self,*args)

    def get_min(self,*args):
        return BSTree.get_min(self,*args)

    def get_element_count(self,*args):
        return BSTree.get_element_count(self,*args)

    def get_height(self,*args):
        return BSTree.get_height(self,*args)

    def _delete_case_one(self,child,parent):
        if parent:
            self._delete_case_two(child,parent)

    def _delete_case_two(self,child,parent):
        node = child
        par_node = parent

        if par_node.left == node:
            sib_node = par_node.right
        elif par_node.right == node:
            sib_node = par_node.left

        if sib_node and sib_node.color == 'r':
            sib_node.color = 'k'
            par_node.color = 'r'
            if par_node.left == node:
                self._rotate_left(par_node)
            else:
                self._rotate_right(par_node)

        self._delete_case_three(node,par_node)

    def _delete_case_three(self,child,parent):
        node = child
        par_node = parent

        if par_node.left == node:
            sib_node = par_node.right
        elif par_node.right == node:
            sib_node = par_node.left

        if ((sib_node and sib_node.color == 'k') or (not sib_node)):
            sib_color = 'k'
        else:
            sib_color = 'r'

        if ((sib_node and sib_node.left and sib_node.left.color == 'k') or (not sib_node or not sib_node.left)):
            sib_left_color = 'k'
        else:
            sib_left_color = 'r'

        if ((sib_node and sib_node.right and sib_node.right.color == 'k') or (not sib_node or not sib_node.right)):
            sib_right_color = 'k'
        else:
            sib_right_color = 'r'

        if par_node.color == 'k' and sib_color == 'k' and sib_left_color == 'k' and sib_right_color == 'k':
            sib_node.color = 'r'
            self._delete_case_one(par_node,par_node.parent if par_node.parent else None)
        else:
            self._delete_case_four(node,par_node)

    def _delete_case_four(self,child,parent):
        node = child
        par_node = parent

        if par_node.left == node:
            sib_node = par_node.right
        elif par_node.right == node:
            sib_node = par_node.left

        if ((sib_node and sib_node.color == 'k') or (not sib_node)):
            sib_color = 'k'
        else:
            sib_color = 'r'

        if ((sib_node and sib_node.left and sib_node.left.color == 'k') or (not sib_node or not sib_node.left)):
            sib_left_color = 'k'
        else:
            sib_left_color = 'r'

        if ((sib_node and sib_node.right and sib_node.right.color == 'k') or (not sib_node or not sib_node.right)):
            sib_right_color = 'k'
        else:
            sib_right_color = 'r'

        if par_node.color == 'r' and sib_color == 'k' and sib_left_color == 'k' and sib_right_color == 'k':
            sib_node.color = 'r'
            par_node.color = 'k'
        else:
            self._delete_case_five(node,par_node)

    def _delete_case_five(self,child,parent):
        node = child
        par_node = parent

        if par_node.left == node:
            sib_node = par_node.right
        elif par_node.right == node:
            sib_node = par_node.left

        if ((sib_node and sib_node.color == 'k') or (not sib_node)):
            sib_color = 'k'
        else:
            sib_color = 'r'

        if ((sib_node and sib_node.left and sib_node.left.color == 'k') or (not sib_node or not sib_node.left)):
            sib_left_color = 'k'
        else:
            sib_left_color = 'r'

        if ((sib_node and sib_node.right and sib_node.right.color == 'k') or (not sib_node or not sib_node.right)):
            sib_right_color = 'k'
        else:
            sib_right_color = 'r'

        if sib_color == 'k':

            if par_node.left == node and sib_right_color == 'k' and sib_left_color == 'r':
                sib_node.color = 'r'
                sib_node.left.color = 'k'
                self._rotate_right(sib_node)
            elif par_node.right == node and sib_left_color == 'k' and sib_right_color == 'r':
                sib_node.color = 'r'
                sib_node.right.color = 'k'
                self._rotate_left(sib_node)

        self._delete_case_six(node,par_node)

    def _delete_case_six(self,child,parent):
        node = child
        par_node = parent

        if par_node.left == node:
            sib_node = par_node.right
        elif par_node.right == node:
            sib_node = par_node.left

        if ((sib_node and sib_node.color == 'k') or (not sib_node)):
            sib_color = 'k'
        else:
            sib_color = 'r'

        if ((sib_node and sib_node.left and sib_node.left.color == 'k') or (not sib_node or not sib_node.left)):
            sib_left_color = 'k'
        else:
            sib_left_color = 'r'

        if ((sib_node and sib_node.right and sib_node.right.color == 'k') or (not sib_node or not sib_node.right)):
            sib_right_color = 'k'
        else:
            sib_right_color = 'r'

        if par_node.left == node and sib_color == 'k' and sib_right_color == 'r':
            sib_node.color = par_node.color
            par_node.color = 'k'
            sib_node.right.color = 'k'
            self._rotate_left(par_node)
        elif par_node.right == node and sib_color == 'k' and sib_left_color == 'r':
            sib_node.color = par_node.color
            par_node.color = 'k'
            sib_node.left.color = 'k'
            self._rotate_right(par_node)

    def _delete_leaf(self,node):
        par_node = node.parent
        node_color = node.color

        if par_node:
            if par_node.left == node:
                par_node.left = None
                new_node = None
            else:
                par_node.right = None
                new_node = None

            del node

        new_parent = par_node

        if node_color == 'k':
            self._delete_case_one(new_node,new_parent)

    def _delete_leaf_parent(self,node):
        par_node = node.parent
        node_color = node.color
        if node.left:
            child_color = node.left.color
        else:
            child_color = node.right.color

        if node.key == self.Root.key:
            if node.right:
                self.Root = node.right
                self.Root.color = 'k'
                node.right = None
                new_node = node.right
            else:
                self.Root = node.left
                self.Root.color = 'k'
                node.left = None
                new_node= node.left

        else:
            if par_node.right == node:
                if node.right:
                    par_node.right = node.right
                    par_node.right.parent = par_node
                    node.right = None
                    if node_color == 'k' and child_color == 'r':
                        par_node.right.color = 'k'

                else:
                    par_node.right = node.left
                    par_node.right.parent = par_node
                    node.left = None
                    if node_color == 'k' and child_color == 'r':
                        par_node.right.color = 'k'

                new_node = par_node.right

            else:

                if node.right:
                    par_node.left = node.right
                    par_node.left.parent = par_node
                    node.right = None
                    if node_color == 'k' and child_color == 'r':
                        par_node.left.color = 'k'
                else:
                    par_node.left = node.left
                    par_node.left.parent = par_node
                    node.left = None
                    if node_color == 'k' and child_color == 'r':
                        par_node.left.color = 'k'

                new_node = par_node.left

        del node

        if node_color == 'k' and child_color == 'k':

            self._delete_case_one(new_node,par_node)

    def _switch_nodes(self,node1,node2):
        BSTree._switch_nodes(self,node1,node2)

    def _delete_node(self,node):
        BSTree._delete_node(self,node)

    def delete(self,key):
        node = self.get_node(key,self.Root)

        if node:
            if not (node.left or node.right):
                if node.parent:
                    self._delete_leaf(node)

            elif not (node.left and node.right):
                self._delete_leaf_parent(node)

            else:
                self._delete_node(node)        