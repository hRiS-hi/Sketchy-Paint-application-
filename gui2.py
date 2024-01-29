import tkinter as tk

class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sketchy")

        self.canvas = tk.Canvas(root, width=700, height=600, bg="white")
        self.canvas.pack()

        self.setup_drawing_tool()

    def setup_drawing_tool(self):
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.reset)
        self.old_x = None
        self.old_y = None

    def draw(self, event):
        x, y = event.x, event.y
        if self.old_x and self.old_y:
            self.canvas.create_line(self.old_x, self.old_y, x, y, width=2, fill="black", capstyle=tk.ROUND, smooth=tk.TRUE)
        self.old_x = x
        self.old_y = y
   
    def reset(self, event):
        self.old_x = None
        self.old_y = None
    
def main():
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()

def main():
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

