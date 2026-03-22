"""Módulo de mensajes predefinidos para validación."""

from tkinter import messagebox


class Mensajes:
    """Mensajes estándar del compilador de validaciones."""
    
    # mensajes de éxito
    VALIDACION_EXITOSA = "✓ Se validó correctamente"
    MATCH_ENCONTRADO = "✓ Match encontrado"
    EXPRESION_VALIDA = "✓ Expresión válida"
    CONTROL_FLUJO_VALIDO = "✓ Control de flujo válido"
    
    # mensajes de error
    VALIDACION_FALLIDA = "✗ Validación fallida"
    MATCH_NO_ENCONTRADO = "✗ No se encontró match"
    EXPRESION_INVALIDA = "✗ Expresión inválida"
    ENTRADA_VACIA = "Por favor ingrese una expresión"
    
    @staticmethod
    def obtener_mensaje_exito(tipo: str) -> str:
        """Retorna un mensaje de éxito según el tipo."""
        if "expresión" in tipo:
            return Mensajes.EXPRESION_VALIDA
        elif "control" in tipo:
            return Mensajes.CONTROL_FLUJO_VALIDO
        return Mensajes.VALIDACION_EXITOSA
    
    @staticmethod
    def obtener_mensaje_error(tipo: str) -> str:
        """Retorna un mensaje de error según el tipo."""
        return Mensajes.VALIDACION_FALLIDA
    
    @staticmethod
    def obtener_tipo_descripcion(clasificacion: str) -> str:
        """Retorna una descripción clara del tipo de validación."""
        if "expresión válida" in clasificacion:
            return "Es una expresión válida"
        elif "control de flujo" in clasificacion:
            return f"Es un {clasificacion}"
        else:
            return f"No es válido: {clasificacion}"
    
    @staticmethod
    def mostrar_validacion_exitosa(clasificacion: str, expresion: str) -> None:
        """Muestra ventana de validación exitosa."""
        mensaje = Mensajes.obtener_mensaje_exito(clasificacion)
        tipo_descripcion = Mensajes.obtener_tipo_descripcion(clasificacion)
        messagebox.showinfo(
            "Validación Exitosa",
            f"{mensaje}\n\n{tipo_descripcion}\n\nValor ingresado: {expresion}"
        )
    
    @staticmethod
    def mostrar_validacion_fallida(clasificacion: str, expresion: str) -> None:
        """Muestra ventana de validación fallida."""
        mensaje = Mensajes.obtener_mensaje_error(clasificacion)
        tipo_descripcion = Mensajes.obtener_tipo_descripcion(clasificacion)
        messagebox.showerror(
            "Validación Fallida",
            f"{mensaje}\n\n{tipo_descripcion}\n\nValor ingresado: {expresion}"
        )
    
    @staticmethod
    def mostrar_entrada_vacia() -> None:
        """Muestra ventana de entrada vacía."""
        messagebox.showwarning("Alerta", Mensajes.ENTRADA_VACIA)


