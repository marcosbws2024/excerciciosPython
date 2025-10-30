def maiorNumero_recursivo(lista):
    """
    Busca o maior elemento em uma lista de números inteiros de forma recursiva.
    """

    # 1. CASO BASE (PONTO DE PARADA)
    # Se a lista tiver apenas um elemento, ele é o maior por definição.
    if len(lista) == 1:
        return lista[0]

    # Trata listas vazias
    if not lista:
        return None

    # 2. PASSO RECURSIVO

    # Chama a função recursivamente com o resto da lista (todos os elementos, exceto o primeiro).
    # O resultado desta chamada é o maior elemento do 'resto' da lista.
    maior_do_resto = maiorNumero_recursivo(lista[1:])

    # 3. COMBINAÇÃO

    # Compara o primeiro elemento da lista atual (lista[0]) com o maior elemento
    # encontrado no restante da lista (maior_do_resto).
    primeiro_elemento = lista[0]

    if primeiro_elemento > maior_do_resto:
        # Se o primeiro for o maior, retorna ele.
        return primeiro_elemento
    else:
        # Senão, o maior_do_resto é o maior de todos.
        return maior_do_resto


# --- Exemplo de Uso (Testando) ---

listaNumero = [45, 456, 489, 12, 48, 34, 36]
resultado_recursivo = maiorNumero_recursivo(listaNumero)

print(f'Lista utilizada: {listaNumero}')
print(f'Maior numero encontrado (recursivo): {resultado_recursivo}')