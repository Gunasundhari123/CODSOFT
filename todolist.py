from tkinter import *
from tkinter import ttk
class todo:
    def __init__(self,root):
        self.root=root
        self.root.title("TO_DO_LIST")
        self.root.geometry('650×410+300+150')


        self.label=Label(self.root,text='TO DO LIST APP',font='ariel,25 bold',width=10,bd=5,bg='teal',fg='white')
        self.label.pack(side='top',fill=BOTH)

                                   
def main():
    root=Tk()
    ui=todo(root) 
    root.mainloop()
if __name__ == "__main__" :
    main()         