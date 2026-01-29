import random
from time import sleep

# --- CONFIGURAÇÃO DE AMBIENTE (CORES LINUX) ---
CLR_CYAN    = "\033[1;36m" # Sistema / Bot
CLR_GREEN   = "\033[1;32m" # Sucesso / Acerto
CLR_RED     = "\033[1;31m" # Erros / Avisos
CLR_YELLOW  = "\033[1;33m" # Dicas (Acima/Abaixo)
CLR_MAGENTA = "\033[1;35m" # Bordas e Títulos
CLR_RESET   = "\033[0m"    # Reset

def show_header():
    """Estilização do cabeçalho do sistema."""
    print(f"{CLR_MAGENTA}{'='*45}{CLR_RESET}")
    print(f"{CLR_CYAN}SISTEMA DE PREDIÇÃO NUMÉRICA v2.0{CLR_RESET}")
    print(f"{CLR_MAGENTA}{'='*45}{CLR_RESET}\n")

def determine_winner(bot_num: int) -> None:
    """Orquestra a lógica de comparação entre User e Bot."""
    attempts = 0
    
    while True:
        try:
            user_input = input(f"{CLR_CYAN}>>> Digite sua predição (0-100): {CLR_RESET}")
            user_num = int(user_input)
            attempts += 1
            
        except KeyboardInterrupt:
            print(f"\n{CLR_RED}[SIGINT]{CLR_RESET} Operação abortada pelo arquiteto.")
            exit(0)
            
        except ValueError:
            print(f"{CLR_RED}[ERRO]{CLR_RESET} Entrada '{user_input}' é inválida. Use apenas INTEIROS.")
            continue
            
        except Exception as e:
            print(f"{CLR_RED}[CRITICAL]{CLR_RESET} Falha inesperada: {e.__class__.__name__}")
            exit(1)
            
        else:
            if user_num == bot_num:
                print(f"\n{CLR_GREEN}[ACESSO CONCEDIDO]{CLR_RESET}")
                print(f"Parabéns! Você acertou o número {bot_num} em {attempts} tentativas.")
                break
            
            elif user_num < bot_num:
                print(f"{CLR_YELLOW}[DICA]{CLR_RESET} O valor alvo é MAIOR que {user_num}.")
            
            else: # user_num > bot_num
                print(f"{CLR_YELLOW}[DICA]{CLR_RESET} O valor alvo é MENOR que {user_num}.")

def main():
    show_header()
    
    print(f"{CLR_CYAN}[PROCESS]{CLR_RESET} Gerando semente aleatória...", end="\r")
    bot_num = random.randint(0, 100)
    sleep(1) # Simulação de processamento de infra
    print(f"{CLR_CYAN}[STATUS]{CLR_RESET} Número gerado com sucesso!     ")
    
    determine_winner(bot_num=bot_num)

if __name__ == "__main__":
    main()