def calcular_gorjeta(total: float, taxa: float) -> float:
    """Calcula o valor da gorjeta com base no total e porcentagem."""
    return (total / 100) * taxa

def main() -> None:
    # Definição de cores para melhor legibilidade
    COR_ERRO = "\33[3;35m"
    RESET = "\33[m"

    try:
        # Entrada de dados com sanitização básica
        entrada_total = input("Digite o valor total da conta: ").strip().replace(',', '.')
        entrada_taxa = input("Digite a porcentagem da gorjeta: ").strip().replace(',', '.')
        
        total = float(entrada_total)
        taxa = float(entrada_taxa)

    except (ValueError, TypeError):
        print(f"{COR_ERRO}Erro: Por favor, insira valores numéricos válidos.{RESET}")
    
    else:
        # Execução do cálculo e exibição formatada
        valor_final = calcular_gorjeta(total, taxa)
        print(f"O valor da gorjeta é: R$ {valor_final:.2f}")
        print(f"Total a pagar: R$ {(total + valor_final):.2f}")

if __name__ == "__main__":
    main()
    