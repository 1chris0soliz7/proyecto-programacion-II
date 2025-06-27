import tkinter as tk
from tkinter import ttk
import random

class MiLinea:
    def __init__(self, x1=0, y1=0, x2=0, y2=0, color="black", width=1, dash=None):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        self.__color = color
        self.__width = width
        self.__dash = dash
    
    def setX1(self, x1):
        self.__x1 = x1
    
    def setY1(self, y1):
        self.__y1 = y1
    
    def setX2(self, x2):
        self.__x2 = x2
    
    def setY2(self, y2):
        self.__y2 = y2
    
    def setColor(self, color):
        self.__color = color
    
    def setWidth(self, width):
        self.__width = width
    
    def setDash(self, dash):
        self.__dash = dash
    
    def getX1(self):
        return self.__x1
    
    def getY1(self):
        return self.__y1
    
    def getX2(self):
        return self.__x2
    
    def getY2(self):
        return self.__y2
    
    def getColor(self):
        return self.__color
    
    def getWidth(self):
        return self.__width
    
    def getDash(self):
        return self.__dash
    
    def dibujar(self, canvas):
        canvas.create_line(self.__x1, self.__y1, self.__x2, self.__y2, 
                            fill=self.__color, width=self.__width, dash=self.__dash)

class MiRect:
    def __init__(self, x=0, y=0, width=0, height=0, outline="black", fill=None):
        self.__x = x
        self.__y = y
        self.__width = max(0, width)
        self.__height = max(0, height)
        self.__outline = outline
        self.__fill = fill
    
    def setX(self, x):
        self.__x = x
    
    def setY(self, y):
        self.__y = y
    
    def setWidth(self, width):
        self.__width = max(0, width)
    
    def setHeight(self, height):
        self.__height = max(0, height)
    
    def setOutline(self, outline):
        self.__outline = outline
    
    def setFill(self, fill):
        self.__fill = fill
    
    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    
    def getWidth(self):
        return self.__width
    
    def getHeight(self):
        return self.__height
    
    def getOutline(self):
        return self.__outline
    
    def getFill(self):
        return self.__fill
    
    def dibujar(self, canvas):
        if self.__fill:
            canvas.create_rectangle(self.__x, self.__y, 
                                    self.__x + self.__width, self.__y + self.__height, 
                                    outline=self.__outline, fill=self.__fill)
        else:
            canvas.create_rectangle(self.__x, self.__y, 
                                    self.__x + self.__width, self.__y + self.__height, 
                                    outline=self.__outline)

class MiOvalo:
    def __init__(self, x=0, y=0, width=0, height=0, outline="black", fill=None):
        self.__x = x
        self.__y = y
        self.__width = max(0, width)
        self.__height = max(0, height)
        self.__outline = outline
        self.__fill = fill
    
    def setX(self, x):
        self.__x = x
    
    def setY(self, y):
        self.__y = y
    
    def setWidth(self, width):
        self.__width = max(0, width)
    
    def setHeight(self, height):
        self.__height = max(0, height)
    
    def setOutline(self, outline):
        self.__outline = outline
    
    def setFill(self, fill):
        self.__fill = fill
    
    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    
    def getWidth(self):
        return self.__width
    
    def getHeight(self):
        return self.__height
    
    def getOutline(self):
        return self.__outline
    
    def getFill(self):
        return self.__fill
    
    def dibujar(self, canvas):
        if self.__fill:
            canvas.create_oval(self.__x, self.__y, 
                                self.__x + self.__width, self.__y + self.__height, 
                                outline=self.__outline, fill=self.__fill)
        else:
            canvas.create_oval(self.__x, self.__y, 
                                self.__x + self.__width, self.__y + self.__height, 
                                outline=self.__outline)

class DrawingCanvas:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=800, height=600, bg="white")
        self.canvas.pack(pady=10)
        
        # Tool selection
        self.current_tool = None
        self.start_x = None
        self.start_y = None
        self.current_shape = None
        
        # Bind mouse events
        self.canvas.bind("<Button-1>", self.start_drawing)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.stop_drawing)
        
        # Tool buttons
        tool_frame = tk.Frame(root, bg="#f0f0f0")
        tool_frame.pack(pady=5)
        
        style = ttk.Style()
        style.configure("TButton", font=("Helvetica", 12), padding=10)
        
        line_button = ttk.Button(tool_frame, text="Línea", command=lambda: self.set_tool("line"), style="TButton")
        line_button.grid(row=0, column=0, padx=5)
        
        rect_button = ttk.Button(tool_frame, text="Rectángulo", command=lambda: self.set_tool("rect"), style="TButton")
        rect_button.grid(row=0, column=1, padx=5)
        
        oval_button = ttk.Button(tool_frame, text="Óvalo", command=lambda: self.set_tool("oval"), style="TButton")
        oval_button.grid(row=0, column=2, padx=5)
        
        # Reload button
        reload_button = ttk.Button(tool_frame, text="Recargar", command=self.reload, style="TButton")
        reload_button.grid(row=0, column=3, padx=5)
    
    def set_tool(self, tool):
        self.current_tool = tool
        self.canvas.config(cursor="cross" if tool else "arrow")
    
    def start_drawing(self, event):
        if not self.current_tool:
            return
        self.start_x = event.x
        self.start_y = event.y
        self.current_shape = None
    
    def draw(self, event):
        if not self.current_tool or self.start_x is None:
            return
        self.canvas.delete("temp")
        color = self.random_color()
        if self.current_tool == "line":
            self.canvas.create_line(self.start_x, self.start_y, event.x, event.y, fill=color, width=2, tags="temp")
        elif self.current_tool == "rect":
            self.canvas.create_rectangle(self.start_x, self.start_y, event.x, event.y, outline=color, tags="temp")
        elif self.current_tool == "oval":
            self.canvas.create_oval(self.start_x, self.start_y, event.x, event.y, outline=color, tags="temp")
    
    def stop_drawing(self, event):
        if not self.current_tool or self.start_x is None:
            return
        color = self.random_color()
        fill = self.random_color() if random.random() > 0.5 else None
        if self.current_tool == "line":
            linea = MiLinea(self.start_x, self.start_y, event.x, event.y, color, width=2)
            linea.dibujar(self.canvas)
        elif self.current_tool == "rect":
            x, y = min(self.start_x, event.x), min(self.start_y, event.y)
            width = abs(event.x - self.start_x)
            height = abs(event.y - self.start_y)
            rect = MiRect(x, y, width, height, color, fill)
            rect.dibujar(self.canvas)
        elif self.current_tool == "oval":
            x, y = min(self.start_x, event.x), min(self.start_y, event.y)
            width = abs(event.x - self.start_x)
            height = abs(event.y - self.start_y)
            ovalo = MiOvalo(x, y, width, height, color, fill)
            ovalo.dibujar(self.canvas)
        self.canvas.delete("temp")
        self.start_x = None
        self.start_y = None
    
    def reload(self):
        self.canvas.delete("all")
    
    def random_color(self):
        return "#{:06x}".format(random.randint(0, 0xFFFFFF))

# Main application
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Aplicación de Dibujo Interactiva")
    root.geometry("800x650")
    root.configure(bg="#f0f0f0")
    app = DrawingCanvas(root)
    root.mainloop()
    