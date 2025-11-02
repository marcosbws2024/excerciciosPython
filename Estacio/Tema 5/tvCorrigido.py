class Televisao:
    def __init__(self, pcanal, min, max):
        # Garante que o canal inicial esteja dentro dos limites
        if min <= pcanal <= max:
            self.canal = pcanal
        else:
            # Se o canal inicial estiver fora do limite, define-o como o mínimo
            self.canal = min
            print(f"Aviso: Canal inicial {pcanal} fora do limite. Definido para {min}.")
            
        self.cmin = min
        self.cmax = max

    def muda_canal_para_baixo(self):
        # Verifica se o canal atual é maior que o mínimo
        if self.canal > self.cmin:
            self.canal -= 1
        else:
            # Se já estiver no mínimo, volta para o máximo (comportamento de 'loop')
            # Se preferir que pare no mínimo, remova a linha abaixo e deixe o 'else' vazio ou com um 'print'
            self.canal = self.cmax 


    def muda_canal_para_cima(self):
        # Verifica se o canal atual é menor que o máximo
        if self.canal < self.cmax:
            self.canal += 1
        else:
            # Se já estiver no máximo, volta para o mínimo (comportamento de 'loop')
            # Se preferir que pare no máximo, remova a linha abaixo e deixe o 'else' vazio ou com um 'print'
            self.canal = self.cmin

# --- Teste 1: Subindo o canal (deve parar/voltar em 10) ---
tv1 = Televisao(2, 2, 10)
print("\n--- Teste 1: Subindo o canal ---")
print(f"Canal Inicial: {tv1.canal} (Min: {tv1.cmin}, Max: {tv1.cmax})")

for x in range(1, 15): # 15 iterações
    tv1.muda_canal_para_cima()
    print(f"Canal Sintonizado: {tv1.canal}")

# --- Teste 2: Descendo o canal (deve parar/voltar em 2) ---
tv2 = Televisao(10, 2, 10)
print("\n--- Teste 2: Descendo o canal ---")
print(f"Canal Inicial: {tv2.canal} (Min: {tv2.cmin}, Max: {tv2.cmax})")

for x in range(1, 15): # 15 iterações
    tv2.muda_canal_para_baixo()
    print(f"Canal Sintonizado: {tv2.canal}")