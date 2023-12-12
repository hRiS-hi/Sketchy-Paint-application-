import tkinter as tk
from tkinter import colorchooser

class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Paint App")

        # Set up canvas
        self.canvas = tk.Canvas(root, bg="white", width=800, height=600)
        self.canvas.pack(expand=tk.YES, fill=tk.BOTH)

        # Create buttons
        self.clear_button = tk.Button(root, text="Clear", command=self.clear_canvas)
        self.clear_button.pack(side=tk.LEFT)
                               
        self.color_button = tk.Button(root, text="Choose Color", command=self.choose_color)
        self.color_button.pack(side=tk.LEFT)

        self.pen_button = tk.Button(root, text="Pen", command=self.use_pen)
        self.pen_button.pack(side=tk.LEFT)

        self.brush_button = tk.Button(root, text="Brush", command=self.use_brush)
        self.brush_button.pack(side=tk.LEFT)

        self.eraser_button = tk.Button(root, text="Eraser", command=self.use_eraser)
        self.eraser_button.pack(side=tk.LEFT)

        # Set default tool
        self.pen = True
        self.color = "black"
        self.eraser_on = False
        self.brush_size = 2
        self.set_tool()

        # Bind mouse events
        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.reset)

    def paint(self, event):
        x1, y1 = (event.x - 1), (event.y - 1)
        x2, y2 = (event.x + 1), (event.y + 1)

        if self.eraser_on:
            self.canvas.create_oval(x1, y1, x2, y2, fill="white", width=5)
        elif self.pen:
            self.canvas.create_oval(x1, y1, x2, y2, fill=self.color, width=2)
        elif self.brush:
            self.canvas.create_oval(x1, y1, x2, y2, fill=self.color, width=self.brush_size)

    def reset(self, event):
        self.start_x, self.start_y = None, None

    def set_tool(self):
        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.reset)

    def clear_canvas(self):
        self.canvas.delete("all")

    def choose_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.color = color

    def use_pen(self):
        self.pen = True
        self.eraser_on = False
        self.brush = False
        self.set_tool()

    def use_brush(self):
        self.pen = False
        self.eraser_on = False
        self.brush = True
        self.set_tool()

    def use_eraser(self):
        self.pen = False
        self.eraser_on = True
        self.brush = False
        self.set_tool()

if __name__ == "__main__":
    root = tk.Tk()
    paint_app = PaintApp(root)
    root.mainloop()
