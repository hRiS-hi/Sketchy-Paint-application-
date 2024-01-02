from tkinter import *
root = Tk()
root.title("Paint application")
root.geometry("1100x600")

frame1 = Frame(root, height=100, width=1100, bg="white", highlightthickness=0.5, highlightbackground="white")
frame1.grid(row=0,column=0)

frame2 = Frame(root, height=500, width=1100, bg="white", highlightthickness=0.5, highlightbackground="white")
frame2.grid(row=1,column=0)

canvas = Canvas(frame2,height=500,width=1100,bg="white")
canvas.grid(row=1,column=0)


root.resizable(False,False)   
root.mainloop()