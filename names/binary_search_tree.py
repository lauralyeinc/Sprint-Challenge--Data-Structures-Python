class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None 

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else: 
                self.left.insert(value)
            
        if value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)


    def contains(self, target):
        if self.value == target:
            return True
        if target < self.value:
            if self.left is None:
                return False
            else: 
                return self.left.contains(target)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target) 

    def get_max(self):
        if self.right is None:
            return self.value
        return self.right.get_max()

    def for_each(self, fn):
        fn(self.value)

        if self.left:
            self.left.for_each(fn)
        
        if self.right:
            self.right.for_each(fn)
    