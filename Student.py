class student:
    def __init__(self,roll_no,name,mark):
        self.roll_no=roll_no
        self.name=name
        self.mark=mark

    def to_dict(self):
        return {
            "roll_no":self.roll_no,
            "name":self.name,
            "mark":self.mark
        }
    
    @staticmethod
    def from_dict(self):
        return student(self["roll_no"],self["name"],self["mark"])