while True:
    try:
         nr = int(input("numero:"))
         s= nr *3
         print(s)
         q = 12/s
         print(q)
         break
    except ValueError:
        print("numero invalido")
        break
    except KeyboardInterrupt:
        print("\ncliente encerrou o programa")
        break
    except ZeroDivisionError:
        print("numero não é divisao por zero")
        break
    else:
        print("Erro Desconhecido")
        break
    finally:
        print("Fim do programa")
