precoProduto = float(input("Digite o valor do produto: "))

print("Opcoes de Pagamento:")
print("1. A vista Dinheiro ou Cheque 10% de desconto")
print("2. A vista no Cartão 5% de desconto")
print("3. 2x no cartão mesmo preço")
print("4  3x ou mais no cartao 20% de desconto")

opcao  = int(input("opcao de pagamento: "))
if opcao == 1:
    descontodinheirocheque = (precoProduto * 10) /100
    valorPagar = precoProduto - descontodinheirocheque
elif opcao == 2:
    descontovistacartao = (precoProduto * 5) /100
    valorPagar = precoProduto - descontovistacartao
elif opcao == 3:
     valorPagar = precoProduto
elif opcao == 4:
    tresvezescartao = (precoProduto * 20) /100
    valorPagar =precoProduto + tresvezescartao

print("Valor a Pagar:{}".format(valorPagar))

