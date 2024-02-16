from tkinter import *
from tkinter import ttk, colorchooser, filedialog

import PIL

class Main:
        def __init__(self, master):
            self.master = master
            self.color_fg = 'black'
            self.color_bg = 'white'
            self.old_x = None
            self.old_y = None
            self.penwidth = 5
            self.eraser_mode = False
            self.undo_actions = []  
            self.redo_actions = []  
            self.draw_widgets()
            self.c.bind('<B1-Motion>', self.paint)
            self.c.bind('<ButtonRelease-1>', self.reset_screen)
            self.c.bind('<Enter>', self.change_cursor)
            self.c.bind('<Leave>', self.restore_cursor)
            self.master.bind('<Control-KeyPress-z>', self.undo)
            self.master.bind('<Control-KeyPress-y>', self.redo)

        def paint(self, e):
            if self.old_x and self.old_y:
                if not self.eraser_mode:
                    line = self.c.create_line(self.old_x, self.old_y, e.x, e.y, width=self.penwidth, fill=self.color_fg,
                                            capstyle="round", smooth=True)
                else:
                    line = self.c.create_line(self.old_x, self.old_y, e.x, e.y, width=self.penwidth, fill=self.color_bg,
                                            capstyle="round", smooth=True)
                self.undo_actions.append(line)
            self.old_x = e.x
            self.old_y = e.y

        def reset_screen(self, e):
            self.old_x = None
            self.old_y = None
            self.redo_actions = []  # Reset redo actions on new drawing

        def change_penwidth(self, e):
            self.penwidth = e

        def toggle_eraser(self):
            self.eraser_mode = not self.eraser_mode
            if self.eraser_mode:
                self.toggle_button.config(text='Brush Mode', bg='#3498db', fg='white')
            else:
                self.toggle_button.config(text='Eraser Mode', bg='#e74c3c', fg='white')

        def save_file(self):
            file = filedialog.asksaveasfilename(filetypes=[('Portable Network Graphics', '*.png')])
            if file:
                x = self.master.winfo_rootx() + self.c.winfo_x()
                y = self.master.winfo_rooty() + self.c.winfo_y()
                x1 = x + self.c.winfo_width()
                y1 = y + self.c.winfo_height()

                self.c.postscript(file=file + '.eps', colormode='color')
                PIL.Image.open(file + '.eps').convert("RGB").save(file + '.png', "PNG")
                self.c.delete("all")
                self.undo_actions = []  

        def clear_screen(self):
            self.c.delete(ALL)
            self.undo_actions = []  # Clear undo actions
            self.redo_actions = []  # Clear redo actions

        def undo(self, event=None):
            if self.undo_actions:
                item = self.undo_actions.pop()
                self.redo_actions.append(item)
                self.c.delete(item)

        def redo(self, event=None):
            if self.redo_actions:
                item = self.redo_actions.pop()
                self.undo_actions.append(item)
                self.c.itemconfigure(item, state='normal')

        def change_fgcolor(self):
            self.color_fg = colorchooser.askcolor(color=self.color_fg)[1]

        def change_bgcolor(self):
            self.color_bg = colorchooser.askcolor(color=self.color_bg)[1]
            self.c['bg'] = self.color_bg

        def change_cursor(self, e):
            if self.eraser_mode:
                self.c.config(cursor='circle')
            else:
                self.c.config(cursor='pencil')

        def restore_cursor(self, e):
            self.c.config(cursor='arrow')
        def create_rectangle(self, x1, y1, x2, y2, fill="white", outline="black", width_outline=1):
            self.c.create_rectangle(x1, y1, x2, y2, fill=fill, outline=outline, width=width_outline)
        def create_oval(self, x1, y1, x2, y2, fill="white", outline="black", width_outline=1):
            self.c.create_oval(x1, y1, x2, y2, fill=fill, outline=outline, width=width_outline)
        def create_polygon(self, points, fill="white", outline="black", width_outline=1):
            self.c.create_polygon(points, fill=fill, outline=outline, width=width_outline)
        def create_line(self, x1, y1, x2, y2, fill="black", width=1):
            self.c.create_line(x1, y1, x2, y2, fill=fill, width=width)
   
        

        def draw_widgets(self):
            self.controls = Frame(self.master, padx=5, pady=5, bg="#3498db")
            self.label = Label(self.controls, text='Pen Width: ', font=('Arial', 15), bg='#3498db', fg='white')
            self.label.grid(row=0, column=0)

            style = ttk.Style()
            style.configure("TScale", troughcolor="#3498db", sliderthickness=15, sliderlength=20, background="#3498db")
            self.slider = ttk.Scale(self.controls, from_=5, to=100, command=self.change_penwidth, orient=HORIZONTAL, style="TScale")
            self.slider.set(self.penwidth)
            self.slider.grid(row=0, column=1, ipadx=30)

            self.toggle_button = Button(self.controls, text='Eraser Mode', command=self.toggle_eraser, bg='#e74c3c', fg='white')
            self.toggle_button.grid(row=0, column=2, padx=10)

            self.controls.pack(fill=X)
            self.c = Canvas(self.master, width=800, height=600, bg=self.color_bg)
            self.c.pack(fill=BOTH, expand=True)

           

            menu = Menu(self.master)
            self.master.config(menu=menu)
            filemenu = Menu(menu)
            menu.add_cascade(label='File', menu=filemenu)
            filemenu.add_command(label='Save As', command=self.save_file)

            colormenu = Menu(menu)
            menu.add_cascade(label='Colors', menu=colormenu)
            colormenu.add_command(label='Brush Color', command=self.change_fgcolor)
            colormenu.add_command(label='Background Color', command=self.change_bgcolor)

            optionmenu = Menu(menu)
            menu.add_cascade(label='Options', menu=optionmenu)
            optionmenu.add_command(label='Clear Canvas', command=self.clear_screen)
            optionmenu.add_command(label='Toggle Eraser Mode', command=self.toggle_eraser)
            optionmenu.add_separator()
            optionmenu.add_command(label='Undo', command=self.undo, accelerator='Ctrl+Z')
            optionmenu.add_command(label='Redo', command=self.redo, accelerator='Ctrl+Y')
            


if __name__ == '__main__':
        root = Tk()
        root.geometry("800x700+100+100")
        root.title('PaintGui Application')
        root.configure(bg="#3498db")
        obj = Main(root)
        root.mainloop()