# 📚 Student Information System using Binary Search Tree

This is a Python-based console application for managing student records using a **Binary Search Tree (BST)**. It supports operations such as adding, searching, deleting, and displaying student records in sorted order based on their roll numbers. The data is stored in memory using a BST and persisted using a JSON file.

---

## 🔧 Features

- ✅ Add a new student (Roll No, Name, Marks)
- 🔍 Search student by roll number
- 🗑️ Delete student by roll number
- 📜 Display all students in sorted order (in-order traversal)
- 🔼 Find student with minimum roll number
- 🔽 Find student with maximum roll number
- 🔢 Count total number of students
- 💾 Automatically save and load records using `student.json`
- 🔄 Reset all student records

---

## 🧠 Concepts Used

- Object-Oriented Programming (OOP)
- Binary Search Tree (BST)
- Recursive algorithms
- File handling using JSON
- Menu-driven console interface
- Data persistence between sessions

---

## 📁 File Structure

.
├── student.py         # Student class with to_dict() and from_dict() methods
├── BST.py             # BST class with all tree operations (insert, search, delete, etc.)
├── main.py            # Main application logic with menu system
├── student.json       # Automatically generated file to persist student data
└── README.md          # Project documentation

---

## 🚀 How to Run

1. Make sure you have Python installed (3.x recommended)
2. Save all the project files in the same directory
3. Open a terminal and run:

```bash
python main.py
