class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.data)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.data:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.data:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,data): 
          self.data = data  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains data as data, left , right
'''


# =============================================================================
# Using Queues
def height(root):
    que = []
    height = 0
    que.append(root)
    while (que):
        count = len(que)
        height += 1
        while (count > 0):
            tmp = que.pop(0)
            if (tmp.left is not None):
                que.append(tmp.left)
            if (tmp.right is not None):
                que.append(tmp.right)
            count -= 1
    return height - 1


# Using Queues
def heightStack2(root):
    stack = []
    height = 0
    stack.append(root)
    while (stack):
        count = len(stack)
        height += 1
        while (count > 0):
            tmp = stack.pop()
            if (tmp.right is not None):
                stack.append(tmp.right)
            if (tmp.left is not None):
                stack.append(tmp.left)
            count -= 1
    return height - 1


# Recursive function to calculate the height of a given binary tree
def height(root):
    # base case: empty tree has a height of 0
    if root is None:
        return -1

    # recur for the left and right subtree and consider maximum depth
    return 1 + max(height(root.left), height(root.right))


# Using Stacks
def heightStacks(root):
    max_lvl = 0
    curr_lvl = 0
    stack = []
    dict = {}
    stack.append(root)
    dict[root.data] = curr_lvl;
    while (stack):
        tmp_tree = stack.pop()
        if (tmp_tree.data in dict):
            curr_lvl = dict[tmp_tree.data]
        else:
            dict[tmp_tree.data] = curr_lvl
        if (tmp_tree.left or tmp_tree.right):
            curr_lvl += 1
        if (tmp_tree.right):
            stack.append(tmp_tree.right)
            if (tmp_tree.right.data in dict):
                curr_lvl = dict[tmp_tree.right.data]
            else:
                dict[tmp_tree.right.data] = curr_lvl
        if (tmp_tree.left):
            stack.append(tmp_tree.left)
            if (tmp_tree.left.data in dict):
                curr_lvl = dict[tmp_tree.left.data]
            else:
                dict[tmp_tree.left.data] = curr_lvl
        if (max_lvl < curr_lvl):
            max_lvl = curr_lvl
    return max_lvl


# =============================================================================

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])


################
def checkBST(root):
    que = []
    dict = {}
    height = 0
    que.append(root)
    while (que):
        count = len(que)
        height += 1
        while (count > 0):
            tmp = que.pop(0)
            if(tmp.data in dict):
                return "No"
            dict[tmp.data] = True
            if (tmp.left is not None):
                que.append(tmp.left)
                if(tmp.data < tmp.left.data):
                    return "No"
            if (tmp.right is not None):
                que.append(tmp.right)
                if(tmp.data > tmp.right.data):
                    return "No"
            count -= 1
        height - 1
    return "Yes"


print(checkBST(tree.root))
