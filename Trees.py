class TreeNode:
    def __init__(self,data):
        self.value = data
        self.left = None
        self.right = None

    def insert(self,value):
        if value<self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = TreeNode(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = TreeNode(value)   
        return self

    def InOrder(self,func=print):
        if self.left:
            self.left.InOrder()
        func(self.value)
        if self.right:
            self.right.InOrder()

    def PostOrder(self,func=print):
        if self.left:
            self.left.PostOrder()
        if self.right:
            self.right.PostOrder()
        func(self.value)
    
    def PreOrder(self,func=print):
        func(self.value)
        if self.left:
            self.left.PreOrder()
        if self.right:
            self.right.PreOrder()

    

# class BSTNode(TreeNode):
#     def insert(self,value):
#         if value<self.value:
#             if self.left:
#                 self.left.insert(value)
#             else:
#                 self.left = TreeNode(value)
#         else:
#             if self.right:
#                 self.right.insert(value)
#             else:
#                 self.right = TreeNode(value)   
#         return self
    
def ArrayToBST(arr):
    root = TreeNode(arr[0])
    for i in arr[1::]:
        root.insert(i)
    return root

# Tree = ArrayToBST([6,2,8,3,5,4,10,1])
# Tree.InOrder()
# print("--------------------------")
# Tree.PostOrder()
# print("--------------------------")
# Tree.PreOrder()