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

  # function that will add the text into the tasks tab
  def add(self):
    #first we get the content from the text box
    content = self.text.get(1.0, END)

    #next we insert that content into the list box
    self.main_text.insert(END, content)

    #next we write the content into our data text file
    with open('data.txt', 'a') as file:
      file.write(content)
      file.seek(0)
      file.close()
    
    #then we delete the content from the text box
    self.text.delete(1.0, END)

  def delete(self):
    delete_ = self.main_text.curselection()
    look = self.main_text.get(delete_)
    
    #we will delete the content from the data text file
    with open('data.txt', 'r+') as f:
      new_f = f.readlines()
      f.seek(0)
      for line in new_f:
        item = str(look)
        if item not in line:
          f.write(line)
      f.truncate()
    
    #this deletes the content from the text box
    self.main_text.delete(delete_)

  #this reads the data from text file and adds the data into the ListBox in seperate lines
  with open('data.txt', 'r') as file:
    read = file.readlines()
    for i in read:
      ready = i.split()
      self.main_text.insert(END, ready)
    file.close()


def main():
  root = Tk()
  ui = todo(root)
  root.mainloop()

if __name__ == "__main__":
  main()