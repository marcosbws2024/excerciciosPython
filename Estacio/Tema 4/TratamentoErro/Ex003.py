while True:
    try:
         nr = int(input("Valor: "))
         s = nr *3
         print(s)
         break

    except ValueError:
        print("valor incorreto")
    except KeyboardInterrupt:
        print("\ncliente encerrou o programa")
        break