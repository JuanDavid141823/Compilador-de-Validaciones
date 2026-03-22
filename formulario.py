import tkinter as tk
from tkinter import ttk
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from validaciones.validaciones_regex import ValidadorRegex
from utils.mensajes import Mensajes


class GUIBase(tk.Frame):
    """Clase base para interfaces gráficas."""
    
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.configurar_ventana()
        self.crear_widgets()
    
    def configurar_ventana(self):
        """Configura la ventana principal. Se sobrescribe en subclases."""
        pass
    
    def crear_widgets(self):
        """Crea los widgets. Se sobrescribe en subclases."""
        pass


class CompiladorValidaciones(GUIBase):
    """Interfaz gráfica simple para validar expresiones."""
    
    def __init__(self, parent):
        self.validador = ValidadorRegex()
        super().__init__(parent)
    
    def configurar_ventana(self):
        """Configura la ventana principal."""
        self.parent.title("Compilador de Validaciones")
        self.parent.geometry("500x130")
        self.parent.resizable(False, False)
        self.pack(fill=tk.BOTH, expand=True)
    
    def crear_widgets(self):
        """Crea la interfaz simple."""
        frame_principal = ttk.Frame(self, padding=15)
        frame_principal.pack(fill=tk.BOTH, expand=True)
        
        lbl_entrada = ttk.Label(
            frame_principal, 
            text="Ingrese la expresión o variable a validar:", 
            font=("Arial", 10, "bold")
        )
        lbl_entrada.pack(anchor=tk.W, pady=(0, 8))
        
        self.entrada = ttk.Entry(
            frame_principal,
            font=("Courier New", 11),
            width=60
        )
        self.entrada.pack(fill=tk.X, pady=(0, 15))
        self.entrada.bind('<Return>', lambda e: self.validar())
        
        frame_botones = ttk.Frame(frame_principal)
        frame_botones.pack(anchor=tk.CENTER, pady=(0, 10))
        
        btn_validar = tk.Button(
            frame_botones,
            text="Validar",
            command=self.validar,
            font=("Arial", 11, "bold"),
            bg="#4CAF50",
            fg="white",
            padx=30,
            pady=8,
            cursor="hand2"
        )
        btn_validar.pack()
    
    def validar(self):
        """Valida la expresión y muestra el resultado a través de mensajes."""
        expresion = self.entrada.get().strip()
        
        if not expresion:
            Mensajes.mostrar_entrada_vacia()
            return
        
        clasificacion = self.validador.clasificar_linea(expresion)
        
        if "expresión válida" in clasificacion or "control de flujo" in clasificacion:
            Mensajes.mostrar_validacion_exitosa(clasificacion, expresion)
            self.entrada.delete(0, tk.END)
        else:
            Mensajes.mostrar_validacion_fallida(clasificacion, expresion)
