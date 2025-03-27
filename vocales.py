def contar_vocales(texto: str) -> int:
    vocales = "aeiouAEIOUáéíóúÁÉÍÓÚ"
    contador = sum(1 for char in texto if char in vocales)
    return contador
