def encontrar_maximo(arbol):
    # Si el árbol está vacío, no hay valor máximo
    if not arbol:
        return float('-inf')  # Representa un valor muy pequeño

    # Inicializamos una pila con el nodo raíz
    pila = [arbol]
    maximo = float('-inf')  # Representa el valor máximo encontrado hasta ahora

    # Recorremos mientras haya nodos en la pila
    while pila:
        nodo_actual = pila.pop()
        
        # Procesamos el nodo actual si no está vacío
        if nodo_actual:
            valor, hijo_izquierdo, hijo_derecho = nodo_actual
            maximo = max(maximo, valor)  # Actualizamos el máximo
            
            # Agregamos los hijos a la pila para procesarlos más adelante
            if hijo_izquierdo:
                pila.append(hijo_izquierdo)
            if hijo_derecho:
                pila.append(hijo_derecho)

    return maximo


arbol_binario = [
    1,
    [7,
        [2, [], []],
        [6,
            [5, [], []],
            [11, [], []]]],
    [9,
        [],
        [9,
            [5, [], []],
            []]]]

resultado = encontrar_maximo(arbol_binario)
print("El valor máximo en el árbol binario es:", resultado)
