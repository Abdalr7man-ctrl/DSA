
# python Doesn't have Avl Tree in internall Lib (pip install avltree) 
import avltree 
print(dir(avltree.AvlTree))


class Avl :
    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None 
        self.height = 1

