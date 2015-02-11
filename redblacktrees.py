# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 14:10:50 2015

@author: Ashish
"""

from bstree import Node
from bstree import BSTree

class RedBlackNode (Node):
    def __init__(self, key, value, color):
        super.__init__(key, value)
        self.color = color

class RBTree(BSTree):
    def __init__(self, *args):
        super.__init__
        
    