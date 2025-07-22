import Student as student

class BST:
    def __init__(self,student):
        self.data=student
        self.left=None
        self.right=None
    
    def insert(self,student):
        if student.roll_no==self.data.roll_no:
            return
        if self.data.roll_no>student.roll_no:
            if self.left:
                self.left.insert(student)
            else:
                self.left=BST(student)
        else:
            if self.right:
                self.right.insert(student)
            else:
                self.right=BST(student)
        
    def search(self,roll_no):
        if self.data.roll_no==roll_no:
            return self.data
        
        if self.data.roll_no>roll_no and self.left:
            return self.left.search(roll_no)
        
        if self.data.roll_no<roll_no and self.right:
            return self.right.search(roll_no)
        return None
    
    def inorder(self):
        elements=[]

        if self.left:
            elements+=self.left.inorder()
        
        elements.append(self.data)

        if self.right:
            elements+=self.right.inorder()
        
        return elements
    
    def delete(self,roll_no):
        if self.data.roll_no>roll_no:
            self.left=self.left.delete(roll_no)
        elif self.data.roll_no<roll_no:
            self.right=self.right.delete(roll_no)
        else:
            if not self.left and not self.right:
                return None
            if not self.left:
                return self.right
            if not self.right:
                return self.left
            
            min_student=self.right.find_min()
            self.data=min_student
            self.right=self.right.delete(min_student.roll_no)
        return self
    
    def find_min(self):
        if self.left:
           return self.left.find_min()
        
        return self.data
        
    def find_max(self):
        if self.right:
            return self.right.find_max()
        
        return self.data
    
    def count(self):
        total=1
        if self.left:
            total+=self.left.count()
        
        if self.right:
            total+=self.right.count()
        
        return total