
#PART 1
class Node:

    def __init__(self, data=None, right = None, left = None):
        self.left = left
        self.right= right
        self.data = data
            
def insert(tree, value):
    if tree == None:
        tree = value;
    elif tree.data >= value.data:
        tree.left = insert(tree.left, value)
    else:
        tree.right = insert(tree.right, value)
    return tree

def printTree(tree):
    if tree == None:
        return
    else:
        if tree.left != None:
            print printTree(tree.left)
        print tree.data
        if tree.right != None:
            print printTree(tree.right)

def search(tree, value):
    if tree == None:
        return
    if tree.data == value:
        print tree.data
    elif tree.data >= value:
        print tree.data
        search(tree.left, value)
    else:
        print tree.data
        search(tree.right, value)

def Total_Depth(tree, current = 1):
    if tree == None:
        return 0
    else:
        return current + Total_Depth(tree.left, current+1) + Total_Depth(tree.right, current+1)


#PART 2
class RBNode:
    
    def __init__(self, data = None, colour = True, right = None, left = None):
        if data != None:
            self.data = data
            self.colour = colour # black == false, red == true
            self.right = leafNode()
            self.left = leafNode()
        else:
            self = leafNode()

class leafNode:

    def __init__(self):
        self.data = None
        self.colour = False
        
def searchRB(tree, value):
    if tree == None:
        return
    elif tree.data == value:
        print tree.data," (",
        if tree.colour == True:
            print "R )"
        else:
            print "B )"
    elif tree.data >= value:
        print tree.data," (",
        if tree.colour == True:
            print "R )"
        else:
            print "B )"
        searchRB(tree.left, value)
    else:
        print tree.data," (",
        if tree.colour == True:
            print "R )"
        else:
            print "B )"
        searchRB(tree.right, value)

def Total_DepthRB(tree, current = 1):
    if tree == None:
        return 0
    elif tree.data == None:
        return 0
    else:
        return current + Total_DepthRB(tree.left, current+1) + Total_DepthRB(tree.right, current+1)


def insertRB(tree, value):
    tree = rec_insertRB(tree, value)
    tree.colour = False
    return tree

def rec_insertRB(current, value):
    if current == None or current.data == None:
        return RBNode(value)
    elif current.left == None and current.right == None: #if its a leaf
        if current.data >= value:
            current.left = RBNode(value)
            return current
        else:
            current.right = RBNode(value)
            return current
    elif current.data < value:
        current.right = rec_insertRB(current.right, value)
        if current.colour == True:
            return current
        elif current.right.colour == True: #if current's right child is red, check grandchildren
            if current.right.right.colour == True or current.right.left.colour == True: #if there is a red grandchild
                return fix_right(current, value)
            else: #balanced
                return current
        else: #black right child, no rebalance
            return current
    else: #current.data > value
        current.left = rec_insertRB(current.left, value)
        if current.colour == True:
            return current
        elif current.left.colour == True:
            if current.left.left.colour == True or current.left.right.colour == True:
                return fix_left(current, value)
            else:
                return current
        else:
            return current


def fix_left(current, value):
    l_child = current.left
    r_child = current.right
    if r_child.colour == True: #simple case, recolouring
        l_child.colour = False
        r_child.colour = False
        current.colour = True
        return current
    else: #right childs colour is black, left is red
        if value < l_child.data: #left-left case, single rotation
            grandchild = l_child.left
            current.left = l_child.right 
            l_child.right = current
            l_child.colour = False
            current.colour = True
            return l_child
        else: #left-right case, double rotation
            grandchild = l_child.right
            l_child.right = grandchild.left
            current.left = grandchild.right
            grandchild.left = l_child
            grandchild.right = current
            grandchild.colour = False
            current.colour = True
            return grandchild

def fix_right(current, value):
    l_child = current.left
    r_child = current.right
    if l_child.colour == True: #simple case, recolouring
        r_child.colour = False
        l_child.colour = False
        current.colour = True
        return current
    else: #left childs colour is black, right child is red
        if value > r_child.data: #right-right case, single rotation
            grandchild = r_child.right
            current.right = r_child.left 
            r_child.left = current
            r_child.colour = False
            current.colour = True
            return r_child
        else: #right-left case, double rotation
            grandchild = r_child.left
            r_child.left = grandchild.right
            current.right = grandchild.left
            grandchild.right = r_child
            grandchild.left = current
            grandchild.colour = False
            current.colour = True
            return grandchild


#PART 3 - Testing

import random

def test():
    lengths = [20, 100, 500, 2500]
    k = 500
    print " n | r < 0.5 | 0.5 <= r < 0.75 | 0.75 <= r < 1.25 | 1.25 <= r < 1.5 | r > 1.5 |"
    print "    |            |                        |                          |                         |            |"
    for n in lengths:
        r1 = 0
        r2 = 0
        r3 = 0
        r4 = 0
        r5 = 0
        for q in range(0, k):
            lis = random.sample(xrange(1, n+1), n)
            bst = Node(lis[0])
            rb = RBNode(lis[0])
            for j in range(1, n): #adds nodes to trees
                bst = insert(bst, Node(lis[j]))
                rb = insertRB(rb, lis[j])
            bstDepth = Total_Depth(bst)
            rbDepth = Total_DepthRB(rb)
            calc = float(bstDepth)/float(rbDepth) #calculates r
            if calc < 0.5:
                r1 += 1
            elif calc < 0.75:
                r2 += 1
            elif calc < 1.25:
                r3 += 1
            elif calc < 1.5:
                r4 += 1
            else:
                r5 += 1
        print n,"| ",r1/5.0,"% |     ",r2/5.0,"%         |       ",r3/5.0,"%        |       ",r4/5.0,"%      | ",r5/5.0,"% |"

