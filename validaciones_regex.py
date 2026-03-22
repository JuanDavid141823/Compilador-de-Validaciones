import re
from abc import ABC, abstractmethod


class ValidadorBase(ABC):
    """Clase base para todos los validadores."""
    
    def __init__(self):
        self.patrones = {}
    
    @abstractmethod
    def validar(self, linea: str) -> tuple[bool, str]:
        """Valida una línea y retorna (es_válida, tipo)."""
        pass
    
    def limpiar_linea(self, linea: str) -> str:
        """Limpia y normaliza la línea."""
        return linea.strip()


class ValidadorExpresiones(ValidadorBase):
    """Valida expresiones aritméticas, lógicas y regulares."""
    
    def __init__(self):
        super().__init__()
        self.patron_expresion = re.compile(r'^[\w\s+\-*/().\[\]{}=><\!&|^$\\]+$')
    
    def validar(self, linea: str) -> tuple[bool, str]:
        """Valida si una expresión es válida."""
        linea = self.limpiar_linea(linea).rstrip(';')
        
        if not linea:
            return False, "línea vacía"
        
        if re.match(r'^[a-zA-Z_]\w*\s*=\s*[\w\s\-+*/().\[\]{}]+$', linea):
            return False, "asignación simple (no es expresión)"
        
        if not self.patron_expresion.match(linea):
            return False, "expresión no válida"
        
        if re.search(r'(\+\+|\-\-|//|%%)', linea):
            return False, "expresión con operadores inválidos"
        
        if re.match(r'^[\+\-\*/><&!=]', linea) and not linea.startswith('^'):
            return False, "expresión comienza con operador inválido"
        
        if re.search(r'[\-/><!=&]$', linea):
            return False, "expresión termina con operador inválido"
        
        if not self._delimitadores_balanceados(linea):
            return False, "expresión con delimitadores desbalanceados"
        
        return True, "expresión válida"
    
    def _delimitadores_balanceados(self, linea: str) -> bool:
        """Verifica que paréntesis, corchetes y llaves estén balanceados."""
        pila = []
        pares = {'(': ')', '[': ']', '{': '}'}
        
        for char in linea:
            if char in pares:
                pila.append(char)
            elif char in pares.values():
                if not pila or pares[pila.pop()] != char:
                    return False
        
        return len(pila) == 0


class ValidadorControlFlujo(ValidadorBase):
    """Valida estructuras de control de flujo."""
    
    def __init__(self):
        super().__init__()
        self.patrones = {
            'if': re.compile(r'^\s*if\s*\(.+\)\s*\{?\s*$'),
            'else_if': re.compile(r'^\s*else\s+if\s*\(.+\)\s*\{?\s*$'),
            'else': re.compile(r'^\s*else\s*\{?\s*$'),
            'while': re.compile(r'^\s*while\s*\(.+\)\s*\{?\s*$'),
            'for': re.compile(r'^\s*for\s*\(.+;\s*.+;\s*.+\)\s*\{?\s*$'),
            'switch': re.compile(r'^\s*switch\s*\(.+\)\s*\{?\s*$'),
            'cierre': re.compile(r'^\s*\}\s*$')
        }
    
    def validar(self, linea: str) -> tuple[bool, str]:
        """Valida si una línea es un control de flujo válido."""
        linea = self.limpiar_linea(linea)
        
        if not linea:
            return False, "línea vacía"
        
        for tipo, patron in self.patrones.items():
            if patron.match(linea):
                nombre_tipo = tipo.replace('_', ' ').upper()
                return True, f"control de flujo ({nombre_tipo})"
        
        return False, "control de flujo no válido"

class ValidadorRegex:
    """Compilador que integra todos los validadores."""
    
    def __init__(self):
        self.validador_expresiones = ValidadorExpresiones()
        self.validador_flujo = ValidadorControlFlujo()
    
    def clasificar_linea(self, linea: str) -> str:
        """Clasifica una línea usando los validadores apropiados."""
        if not linea.strip():
            return "línea vacía"
        
        es_valido, tipo = self.validador_flujo.validar(linea)
        if es_valido:
            return tipo
        
        es_valido, tipo = self.validador_expresiones.validar(linea)
        if es_valido:
            return tipo
        
        return "expresión no válida"
    
if __name__ == "__main__":
    val = ValidadorRegex()
    
