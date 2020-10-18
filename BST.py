
class BST(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return "[%s, %s, %s]" % (self.left, str(self.val), self.right)

    def isEmpty(self):
        return self.left == self.right == self.val == None

    def insertNode(self, val):
        if self.isEmpty():
            self.val = val
        elif val < self.val:
            if self.left is None:
                self.left = BST(val)
            else:
                self.left.insertNode(node, val)
        else:
            if self.right is None:
                self.right = BST(val)
            else:
                self.right.insertNode(node, val)

    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if root == None:
            return root
        else:
            if key == root.val:
                if root.left == root.right == None:
                    root = None
                    print("value deleted")
                else:
                    temp = root.right
                    root.val = temp.val
                    root.right = temp.right
                    print("No such key")

            if key > root.val:
                self. deleteNode(root.right, key)
            elif key < root.val:
                self. deleteNode(root.left, key)

            return root

a = BST(1)
a.insert(2)
a.insert(3)
a.insert(0)
print a
