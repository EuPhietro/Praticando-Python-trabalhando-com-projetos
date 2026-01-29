# BIBLIOTECA PARA MANIPULAR EXPRESSÕES REGULARES    
import re

def is_cpf_valido(cpf: str) -> bool:
    """
    Valida o formato do CPF utilizando Expressões Regulares.
    Aceita formatos: 000.000.000-00 ou 00000000000.
    """
    # Definimos o padrão Regex como uma constante para performance
    PADRAO_CPF = r"^(\d{3}\.\d{3}\.\d{3}-\d{2}|\d{3}\d{3}\d{3}\d{2})$"
    
    # O fullmatch retorna um objeto Match se válido, ou None se inválido
    return bool(re.fullmatch(PADRAO_CPF, cpf.strip()))

def main() -> None:
    cpf_input = input("Digite seu CPF (com ou sem pontuação): ").strip()

    if is_cpf_valido(cpf_input):
        print(f"\033[1;32mSucesso:\033[m O CPF {cpf_input} possui um formato válido.")
    else:
        print(f"\033[1;31mErro:\033[m '{cpf_input}' não é um formato de CPF reconhecido.")

if __name__ == "__main__":
    main()