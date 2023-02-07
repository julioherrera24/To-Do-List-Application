from tkinter import *
from tkinter import ttk

class todo:
  def __init__(self, root):
    self.root = root
    self.root.title('To-Do-List')
    #sets dimensions of the app
    self.root.geometry('650x410+300+150')

    #creates the To Do List orange label
    self.label = Label(self.root, text= 'To-Do-List App', font= 'ariel, 25 bold', width=10, bd=5, bg='orange', fg='black')
    self.label.pack(side= 'top', fill=BOTH)

    #creates the add task feature
    self.label2 = Label(self.root, text= 'Add Task', font= 'ariel, 18 bold', width=10, bd=5, bg='orange', fg='black')
    self.label2.place(x = 40, y = 54)

    #creates the Tasks feature
    self.label3 = Label(self.root, text= 'Tasks', font= 'ariel, 18 bold', width=10, bd=5, bg='orange', fg='black')
    self.label3.place(x = 320, y = 54)

    #creates a List Box where all tasks will be stored
    self.main_text = Listbox(self.root, height = 9, bd=5, width=23, font="ariel, 20 italic bold")
    self.main_text.place(x=280, y=100)

    #creates a small box where user can type tasks to enter
    self.text = Text(self.root, bd=5, height=2, width=30, font="ariel, 10 bold")
    self.text.place(x=20, y=120)

def main():
  root = Tk()
  ui = todo(root)
  root.mainloop()

if __name__ == "__main__":
  main()