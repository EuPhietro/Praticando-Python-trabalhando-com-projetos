import secrets
from time import sleep

# --- OPÇÕES (GAME RULES) ---
GAME_RULES = {
    "pedra": {"ganha_de": "tesoura", "perde_para": "papel"},
    "papel": {"ganha_de": "pedra", "perde_para": "tesoura"},
    "tesoura": {"ganha_de": "papel", "perde_para": "pedra"}
}

# --- PALETA DE CORES LINUX TERMINAL ---
CLR_CYAN    = "\033[1;36m" # Info / Bot
CLR_GREEN   = "\033[1;32m" # Sucesso / Vitória
CLR_RED     = "\033[1;31m" # Erro / Derrota
CLR_YELLOW  = "\033[1;33m" # Alerta / Empate / Opções
CLR_MAGENTA = "\033[1;35m" # Destaque Sistema
CLR_RESET   = "\033[0m"    # Reset

def show_line(tam=40):
    print(f"{CLR_MAGENTA}{'-' * tam}{CLR_RESET}")

def show_options(choices: dict):
    """Exibe as opções formatadas para o terminal Linux."""
    print(f"{CLR_YELLOW}>>> Selecione sua jogada:{CLR_RESET}")
    show_line(25)
    for i, option in enumerate(choices.keys()):
        print(f" {CLR_CYAN}{i + 1}{CLR_RESET} - {option.capitalize()}")
    show_line(25)

def get_choice(choices: dict, auto_choice=False):
    """Captura a escolha via input ou gera via secrets (Bot)."""
    if auto_choice:
        print(f"{CLR_CYAN}[SYSTEM]{CLR_RESET} O bot está calculando uma jogada...")
        sleep(1.2)
        bot_move = secrets.choice(list(choices.keys()))
        return {bot_move: choices[bot_move]}

    show_options(choices=choices)
    
    while True:
        try:
            player_choice = input(f"{CLR_YELLOW}Opção (ou 'q' para sair): {CLR_RESET}").lower().strip()
        except KeyboardInterrupt:
            print(f"\n{CLR_RED}[SIGINT]{CLR_RESET} Processo interrompido pelo usuário.")
            exit(0)
        else:
            if player_choice in choices.keys():
                return {player_choice: choices[player_choice]}
            elif player_choice == 'q':
                print(f"{CLR_RED}[EXIT]{CLR_RESET} Encerrando instância do jogo.")
                exit(0)
            else:
                print(f"{CLR_RED}ERRO: '{player_choice}' não é um parâmetro válido.{CLR_RESET}")
                continue

def determine_winner(player: dict, bot: dict):
    """Executa a lógica de precedência."""
    p_move = list(player.keys())[0]
    b_move = list(bot.keys())[0]

    print(f"\n{CLR_MAGENTA}LOG DE COMBATE:{CLR_RESET}")
    show_line()
    print(f" JOGADOR: {CLR_GREEN}{p_move.upper()}{CLR_RESET}")
    print(f" BOT:     {CLR_RED}{b_move.upper()}{CLR_RESET}")
    show_line()

    if p_move == b_move:
        print(f"{CLR_YELLOW}RESULTADO: EMPATE TÉCNICO!{CLR_RESET}")
    
    # Lógica de precedência baseada no seu mapa GAME_RULES
    elif p_move in bot[b_move]["ganha_de"]:
        print(f"{CLR_RED}RESULTADO: DERROTA! {b_move.capitalize()} anula {p_move}.{CLR_RESET}")
    
    else:
        print(f"{CLR_GREEN}RESULTADO: VITÓRIA! {p_move.capitalize()} supera {b_move}.{CLR_RESET}")

def main():
    """Handler principal da aplicação."""
    print(f"{CLR_MAGENTA}--- ROCK-PAPER-SCISSORS CLI v1.0 ---{CLR_RESET}")
    
    # Orquestração de turnos
    first_player = secrets.choice([1, 2])

    if first_player == 1:
        print(f"{CLR_GREEN}[STATUS]{CLR_RESET} Jogador tem a prioridade.")
        player = get_choice(GAME_RULES)
        bot = get_choice(GAME_RULES, auto_choice=True)
    else:
        print(f"{CLR_CYAN}[STATUS]{CLR_RESET} Bot tem a prioridade.")
        bot = get_choice(GAME_RULES, auto_choice=True)
        player = get_choice(GAME_RULES)

    determine_winner(player=player, bot=bot)

if __name__ == "__main__":
    main()