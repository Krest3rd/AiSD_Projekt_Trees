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

    def deleteAll(self):
        if self.left:
            self.left.delete()
        if self.right:
            self.right.delete()
        print(self.value, end=" ")
        self.value = None
        self.right = None
        self.left = None

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
            
            #Find succesor and
            self.value = self.right.findMin().value
            
            self.right = self.right.remove(self.value)
        return self

    def InOrder(self,func=print):
        if self.left:
            self.left.InOrder(func)
        func(self.value)
        if self.right:
            self.right.InOrder(func)

    def PostOrder(self,func=print):
        if self.left:
            self.left.PostOrder(func)
        if self.right:
            self.right.PostOrder(func)
        func(self.value)
    
    def PreOrder(self,func=print):
        func(self.value)
        if self.left:
            self.left.PreOrder(func)
        if self.right:
            self.right.PreOrder(func)

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

    def tree_to_vine(self):
        while self.left:
            self = self.rotateR()
        if self.right:
            self.right = self.right.tree_to_vine()
        return self

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


def Delete(root):
    print("Deleting: ",end="")
    root.delete()
    print("\nTree removed")


def PrintAll(root):
    print("Printing in Order")
    root.InOrder()
    print("Printing Post Order")
    root.PostOrder()
    print("Printing Pre Order")
    root.PreOrder()

# def Export(root):
#     head = "Exported tree:------------------\n\\begin{tikzpicture}[>=Stealth]\n\t\\graph[binaary tree layout]\n\t{"
#     mid = root.export()
#     end = "};\n\\end{tikzpicture}"
#     return head + mid + end


def Export(root):
    head = "Exported tree:------------------\n\\begin{tikzpicture}[\n every node/.style = {minimum width = 0em, draw, circle},\nlevel/.style = {sibling distance = 45em/(2^(#1-1))}\n]\n"
    mid = f"\\{root.export()};"
    end = "\n\\end{tikzpicture}\n--------------------------------"
    return head + mid + end


def PrintMinMax(root):
    print("Min: ",root.findMin().value)
    print("Max: ",root.findMax().value)


def DSW_balance_vine(root):
    #funkcja wykonująca rotacje
    def perform_rotations(root, count):
        if count:
            print(root.value)
            root = root.rotateL()
            root.right = perform_rotations(root.right,count-1)

        return root
    

    # count amount of nodes
    n = 1
    temp = root
    while temp.right:
        n += 1
        temp = temp.right
    #Calc number of initial ratations
    w = (n+1).bit_length()-1
    s = n+1-2**w
    root = perform_rotations(root,s)
    #Calc the number of rotations in step 2
    s = n-s
    while s>1:
        s //= 2
        root = perform_rotations(root,s)
    return root


def Balance(root):
    root = root.tree_to_vine()
    return DSW_balance_vine(root)

 
def ArrayToBST(arr):
    root = TreeNode(arr[0])
    for i in arr[1::]:
        root.insert(i)
    return root


def ArrayToAVL(arr):
    arr.sort()
    mid = len(arr)//2
    root = TreeNode(arr[mid])
    if mid != 0:
        root.left = ArrayToAVL(arr[:mid:])
    if mid != len(arr)-1:
        root.right = ArrayToAVL(arr[mid+1::]) 
    return root


Tree = ArrayToAVL([i for i in range(1,128)])
print(Export(Tree))