from Student import student
from BST import BST as bst
import json

def save(student_list):
    with open("student.json","w") as f:
        json.dump([student.to_dict(s) for s in student_list],f)

def load():
    try:
        with open("student.json","r") as f:
            data=json.load(f)
            return [student.from_dict(d) for d in data]
    except FileNotFoundError:
        return []

def build(student_list):
    if not student_list:
        return None
    root=bst(student_list[0])
    for i in student_list[1:]:
        root.insert(i)
    return root

def main():

    students=load()
    root=build(students)

    while True:
        print("\n--- Student Information System ---")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Delete Student")
        print("4. Show All Students")
        print("5. Min Roll No Student")
        print("6. Max Roll No Student")
        print("7. Count Total Students")
        print("8. Save and Exit")
        print("9. Reset")
        print("0. Exit")

        choice = int(input("Enter choice: "))

        if choice==1:
            roll_no=input("enter the student roll number : ")
            if root and root.search(roll_no):
                print("student already exist ")
                continue
            name=input("enter the student name : ")
            mark=int(input("enter the mark :"))
            stu=student(roll_no,name,mark)
            if root:
                root.insert(stu)
            else:
                root=bst(stu)
            print("student is inserted successfully ")

        elif choice==2:
            roll_no=input("enter the roll number : ")
            stu= root.search(roll_no) if root else None
            if stu:
                print(f"roll_no = {stu.roll_no}, name = {stu.name}, mark = {stu.mark}")
            else:
                print("student not found")
        
        elif choice==3:
            roll_no=input("enter the roll number : ")
            if root and root.search(roll_no) :
                root=root.delete(roll_no)
                print("deleted successfully ")
            else:
                print("student not exist")
            
        elif choice==4:
            if root:
                print("--------------All Students---------------")
                list=root.inorder()
                for i in list:
                    print(f"{i.roll_no} - {i.name} - {i.mark}")
            else:
                print("No Student Record Found")
        
        elif choice==5:
            if root:
                i=root.find_min()
                print(f"Min Roll No : {i.roll_no} - {i.name} - {i.mark}")
            else:
                print("Tree is Empty")
        
        elif choice==6:
            if root:
                i=root.find_max()
                print(f"Max Roll No : {i.roll_no} - {i.name} - {i.mark}")
            else:
                print("Tree is Empty")
        
        elif choice==7:
            if root:
                print(f"Total student : {root.count()}")
            else:
                print("Tree is Empty")
        
        elif choice==8:
            all_students=root.inorder() if root else []
            save(all_students)
            print("Saved, Exiting...")
            break
        
        elif choice==9:
            conformation=input("Enter [y/n] to conform :")
            if conformation.lower()=='y':
                with open("student.json","w") as f:
                    json.dump([],f)
                root=None
                students=[]
                print("All student records cleared.")

        elif choice==0:
            print("Exit with out saving...")
            break
        
        else:
            print("Invalid Choice!")

if __name__=="__main__":
    main()
