

banco1 = Banco(999, "teste")
contacliente1 = ContaCliente (1, 0.01, 0.1, 1000, 0.05)
contacomum1 = ContaComum(2, 0.01, 0.1, 2000, 0.05)
contaremunerada1 = ContaRemunerada(3, 0.01, 0.1, 2000, 0.05)

# --- 2. AGREGAÇÃO ---

# CORREÇÃO DE CASE: O método se chama adiciona_conta
banco1.adiciona_conta(contacliente1) # (4)
banco1.adiciona_conta(contacomum1)   # (5)
banco1.adiciona_conta(contaremunerada1) # (6)

# --- 3. PROCESSO E POLIMORFISMO ---

# CORREÇÃO DE CASE E SINTAXE: O método se chama calcular_rendimento_mensal() e precisa de ()
banco1.calcular_rendimento_mensal() # (7)

# CORREÇÃO DE CASE: O método se chama imprime_saldo_contas()
banco1.imprime_saldo_contas() # (8)