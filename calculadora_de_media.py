from time import sleep

def func():
    while True:
        print("="*30)
        print()
        print("         MENU PRINCIPAL          ")
        print()
        print("="*30)
        sleep(1)
        print("O QUE DESEJA FAZER?")
        print()   
        print("-"*30)
        print()   
        print("1 - CALCULAR MÉDIA")
        print("2 - SAIR")
        print()
        print("-"*30)
        resposta = int(input("DIGITE SUA OPÇÃO:\n"))
        sleep(1)
        if resposta == 1:
            print("\nOK, DIGITE AS NOTAS:")
            print()
            b1 = float(input("PRIMEIRO BIMESTRE: "))
            b2 = float(input("SEGUNDO BIMESTRE: "))
            b3 = float(input("TERCEIRO BIMESTRE: "))
            b4 = float(input("QUARTO BIMESTRE: "))
            media = ((b1 + b2 + b3 + b4) / 4)
            print()
            if media > 10.0:
                print(f"SUA NOTA NA MÉDIA FOI 10.0! VOCÊ FOI APROVADO!")
            elif media >= 5.0:
                print(f"SUA NOTA NA MÉDIA FOI {media}! VOCÊ FOI APROVADO!")
            else:
                print(f"SUA NOTA NA MÉDIA FOI {media}! VOCÊ FOI REPROVADO!")
            q = input("DESEJA FECHAR O PROGRAMA? (S/N)\n")
            print()
            if q.upper() == "S":
                print("OK, FECHANDO PROGRAMA")
                sleep(1)
                break
                exit()
            elif q.upper() == "N":
                print("VOLTANDO AO MENU PRINCIPAL")
                sleep(1)
                print()
            else:
                print("ERRO!")
                sleep(1)
                break
                exit()
        elif resposta == 2:
            print("OK, FECHANDO PROGRAMA")
            sleep(1)
            break
            exit()
func()