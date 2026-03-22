import tkinter as tk
from gui.formulario import CompiladorValidaciones


if __name__ == "__main__":
    root = tk.Tk()
    app = CompiladorValidaciones(root)
    root.mainloop()