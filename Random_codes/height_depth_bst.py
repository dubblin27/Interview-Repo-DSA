class node:
    def __init__(self,data) :
        self.right = None 
        self.left = None 
        self.data = data 
    
    def insert(self,data) :
        if self.data :
            if data < self.data :
                if self.left == None:
                    self.left = node(data)
                else :
                    self.left.insert(data)
            elif data > self.data :
                if self.right == None :
                    self.right = node(data)
                else :
                    self.right.insert(data)
        else :
            self.data = data

    def height(self,data):
        if self.data == None :
            return 0 

        leftdepth = height(self.left)
        rightdepth = height(self.right)

        if leftdepth > rightdepth :
            return leftdepth +1 
        else :
            return rightdepth +1 
             