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

    def delete(self):
        if self.left:
            self.left.delete()
        if self.right:
            self.right.delete()
        print(self.value, end=" ")
        del self

    def remove(self,val):
        if self is None:
            return None

        #Search for node
        if self.value > val:
            self.left = self.left.remove(val)
        elif self.value < val:
            self.right = self.right.remove(val)
        else:
            # One child
            if self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            
            self.value = self.right.findMin().value

            self.right = self.right.remove(self.value)
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
    
    def export(self):
        if not self.left and not self.right:
            return f"node {{{self.value}}}"
        l_str = f"child {{{self.left.export()}}}" if self.left else "child[missing]"
        r_str = f"child {{{self.right.export()}}}" if self.right else "child[missing]"
        return f"node {{{self.value}}} \n{l_str} \n{r_str}"
    
    def findMin(self):
        root = self
        while root.left:
            root = root.left
        return root
    
    def findMax(self):
        root = self
        while root.right:
            root = root.right
        return root

    def rotateR(self):
        temp = self.left.right
        self.left.right = self
        self = self.left
        self.right.left = temp
        return self

    def rotateL(self):
        temp = self.right.left
        self.right.left = self
        self = self.right
        self.left.right = temp
        return self


class RootNode(TreeNode):
    def Delete(self):
        print("Deleting: ",end="")
        self.delete()
        print("\nTree removed")

    def PrintAll(self):
        print("Printing in Order")
        self.InOrder()
        print("Printing Post Order")
        self.PostOrder()
        print("Printing Pre Order")
        self.PreOrder()

    def Export(self):
        head = "Exported tree:------------------\n\\begin{tikzpicture}[\n every node/.style = {minimum width = 2em, draw, circle},\nlevel/.style = {sibling distance = 30mm/#1}\n]\n"
        mid = f"\\{self.export()}"
        end = "\n\\end{tikzpicture}\n--------------------------------"
        return head + mid + end
    
    def PrintMinMax(self):
        print("Min: ",self.findMin().value)
        print("Max: ",self.findMax().value)

 


    
def ArrayToBST(arr):
    root = RootNode(arr[0])
    for i in arr[1::]:
        root.insert(i)
    return root


def ArrayToAVL(arr):
    arr.sort()
    mid = len(arr)//2
    root = RootNode(arr[mid])
    if mid != 0:
        root.left = ArrayToAVL(arr[:mid:])
    if mid != len(arr)-1:
        root.right = ArrayToAVL(arr[mid+1::]) 
    return root


Tree = ArrayToAVL([1, 2, 3, 6, 5, 4, 7])
print(Tree.Export())
Tree = Tree.rotateL()
# Tree.PrintAll()
# print(x==Tree)
print(Tree.Export())

