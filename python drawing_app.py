import tkinter as tk
from tkinter import ttk
import random

class MiLinea:
    def _init_(self, x1=0, y1=0, x2=0, y2=0, color="black", width=1, dash=None):
        print("Se creó una línea")
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        self.__color = color
        self.__width = width
        self.__dash = dash
    
    def dibujar(self, canvas):
        print(f"Dibujando línea de ({self._x1}, {self.y1}) a ({self.x2}, {self.y2}) con color {self._color}")
        canvas.create_line(self._x1, self.y1, self.x2, self._y2,
                           fill=self._color, width=self.width, dash=self._dash)

class MiRect:
    def _init_(self, x=0, y=0, width=0, height=0, outline="black", fill=None):
        print("Se creó un rectángulo")
        self.__x = x
        self.__y = y
        self.__width = max(0, width)
        self.__height = max(0, height)
        self.__outline = outline
        self.__fill = fill
    
    def dibujar(self, canvas):
        print(f"Dibujando rectángulo en ({self._x}, {self.y}) de tamaño {self.width}x{self.height} color {self.outline} y relleno {self._fill}")
        canvas.create_rectangle(self._x, self._y,
                                self._x + self.width, self.y + self._height,
                                outline=self._outline, fill=self._fill)

class MiOvalo:
    def _init_(self, x=0, y=0, width=0, height=0, outline="black", fill=None):
        print("Se creó un óvalo")
        self.__x = x
        self.__y = y
        self.__width = max(0, width)
        self.__height = max(0, height)
        self.__outline = outline
        self.__fill = fill
    
    def dibujar(self, canvas):
        print(f"Dibujando óvalo en ({self._x}, {self.y}) de tamaño {self.width}x{self.height} color {self.outline} y relleno {self._fill}")
        canvas.create_oval(self._x, self._y,
                           self._x + self.width, self.y + self._height,
                           outline=self._outline, fill=self._fill)

class DrawingCanvas:
    def _init_(self, root):
        print("Inicializando la aplicación")
        self.root = root
        self.canvas = tk.Canvas(root, width=800, height=600, bg="white")
        self.canvas.pack(pady=10)

        self.current_tool = None
        self.start_x = None
        self.start_y = None

        self.canvas.bind("<Button-1>", self.start_drawing)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.stop_drawing)

        tool_frame = tk.Frame(root, bg="#f0f0f0")
        tool_frame.pack(pady=5)

        style = ttk.Style()
        style.configure("TButton", font=("Helvetica", 12), padding=10)

        ttk.Button(tool_frame, text="Línea", command=lambda: self.set_tool("line")).grid(row=0, column=0, padx=5)
        ttk.Button(tool_frame, text="Rectángulo", command=lambda: self.set_tool("rect")).grid(row=0, column=1, padx=5)
        ttk.Button(tool_frame, text="Óvalo", command=lambda: self.set_tool("oval")).grid(row=0, column=2, padx=5)
        ttk.Button(tool_frame, text="Recargar", command=self.reload).grid(row=0, column=3, padx=5)

    def set_tool(self, tool):
        print(f"Herramienta seleccionada: {tool}")
        self.current_tool = tool
        self.canvas.config(cursor="cross")

    def start_drawing(self, event):
        print(f"Inicio de dibujo en: ({event.x}, {event.y})")
        self.start_x = event.x
        self.start_y = event.y

    def draw(self, event):
        if not self.current_tool or self.start_x is None:
            return
        self.canvas.delete("temp")
        color = self.random_color()
        if self.current_tool == "line":
            print("Dibujando línea temporal...")
            self.canvas.create_line(self.start_x, self.start_y, event.x, event.y, fill=color, width=2, tags="temp")
        elif self.current_tool == "rect":
            print("Dibujando rectángulo temporal...")
            self.canvas.create_rectangle(self.start_x, self.start_y, event.x, event.y, outline=color, tags="temp")
        elif self.current_tool == "oval":
            print("Dibujando óvalo temporal...")
            self.canvas.create_oval(self.start_x, self.start_y, event.x, event.y, outline=color, tags="temp")

    def stop_drawing(self, event):
        print(f"Fin del dibujo en: ({event.x}, {event.y})")
        if not self.current_tool or self.start_x is None:
            return
        color = self.random_color()
        fill = self.random_color() if random.random() > 0.5 else None
        if self.current_tool == "line":
            linea = MiLinea(self.start_x, self.start_y, event.x, event.y, color, 2)
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
        print("Canvas reiniciado (todo se ha borrado)")
        self.canvas.delete("all")

    def random_color(self):
        color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        print(f"Color generado: {color}")
        return color

# Bloque principal
if __name__ == "_main_":
    print("Ejecutando aplicación de dibujo...")
    root = tk.Tk()
    root.title("Aplicación de Dibujo Interactiva")
    root.geometry("800x650")
    root.configure(bg="#f0f0f0")
    app = DrawingCanvas(root)
    root.mainloop()