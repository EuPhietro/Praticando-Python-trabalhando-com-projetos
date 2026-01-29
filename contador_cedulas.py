import os
from time import sleep
CEDULAS = (100,50,20,10,5,2)


def notas (valor,cedula):
    quantidade = valor // cedula
    resto = valor % cedula

    return quantidade, resto
def saque(valor_solicitado, cedulas = CEDULAS):
    valor_restante = valor_solicitado
    resultado = {"valor": valor_solicitado, "cedulas":{}}

    for cedula in cedulas:

        if valor_restante <=0:
            break

        quantidade, resto = notas(valor=valor_restante, cedula=cedula)

        if quantidade > 0:
            resultado["cedulas"][str(cedula)] = quantidade
            valor_restante = resto
        
    
    if valor_restante > 0:
        resultado["status"] = "Erro, este valor não pode ser sacado com as cédulas disponíveis"
        resultado["cedulas"] = {}
    else:
        resultado["status"] = "Sucesso"
            


    return resultado


def main():
    while True:
        try:
            user_input = input("Digite um valor (ctrl + C for exit): ")
            valor = int(user_input)
        except KeyboardInterrupt:
            print("\nO usuário decidiu não continuar, tchau tchau")
            sleep(4)
            os.system("clear")
            break
        except ValueError:
            print(f"ERRO! É esperado um  inteiro, o usuário digitou {user_input}")
        else:
            resultado = saque(valor_solicitado=valor, cedulas=CEDULAS)
            if resultado["cedulas"]:
                print("CEDULAS:")
                for c,i in resultado["cedulas"].items():
                    print(f"{'-':>2}{c} - {i:>5}")

if __name__ == "__main__":
    main()

            