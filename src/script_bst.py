class Node:
        def __init__(self, value) -> None:
            self.value = value
            self.left = None
            self.right = None
            
class BST:
    def __init__(self) -> None:
        self.size = 0
        self.root = None
        
    def add(self, value):
        self.root = self.__add(value, self.root)
        
    def __add(self, value, root) -> Node:
        if root is None:
            self.size = self.size + 1
            return Node(value)
        if value > root.value:
            root.right = self.__add(value, root.right)
        else:
            root.left = self.__add(value, root.left)
        return root

    def preOrder(self):
        self.preOrderList = []
        self.__preOrder(self.root)
        return self.preOrderList
    
    def __preOrder(self, root):
        if root is not None:
            self.preOrderList.append(root.value)
            self.__preOrder(root.left)
            self.__preOrder(root.right)
        return

    def inOrder(self):
        self.inOrderList = []
        self.__inOrder(self.root)
        return self.inOrderList
    
    def __inOrder(self, root):
        if root is not None:
            self.__inOrder(root.left)
            self.inOrderList.append(root.value)
            self.__inOrder(root.right)
        return

    def postOrder(self):
        self.postOrderList = []
        self.__postOrder(self.root)
        return self.postOrderList

    def __postOrder(self, root):
        if root is not None:
            self.__postOrder(root.left)
            self.__postOrder(root.right)
            self.postOrderList.append(root.value)
        return
    
def main():
    values = [1, 3, 4, 6, 7, 2, 10, 5]
    bst = BST()
    for value in values:
        bst.add(value)
    print("Pre Orden", bst.preOrder())
    print("\nIn Orden", bst.inOrder())
    print("\nPost Orden", bst.postOrder())

main()
