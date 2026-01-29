import sys
from pathlib import Path
import os

# Configurações de Infraestrutura
NOME_ARQUIVO = "tarefas.txt"
ARQUIVO_TEMP = "tarefas_temp.txt"
OPCOES_MENU = {
    "1": "Criar Tarefa",
    "2": "Listar Tarefas",
    "3": "Excluir Tarefa",
    "0": "Sair"
}

def formatar_cabecalho(titulo: str):
    largura = len(titulo) + 4
    print("\n" + "=" * largura)
    print(f"  {titulo.upper()}  ")
    print("=" * largura)



def persistir_tarefa(tarefa: dict, filename = NOME_ARQUIVO):
    """Encapsula a lógica de escrita em disco (Persistência)."""
    caminho = Path(filename)
    try:
        # Modo 'a' cria o arquivo se não existir e anexa ao final
        with open(caminho, mode="a", encoding="utf-8") as stream:
            linha = f"{tarefa['titulo']}|{tarefa['descricao']}\n"
            stream.write(linha)
    except IOError as e:
        print(f"Erro de I/O na infraestrutura: {e}")


def coletar_dados_tarefa():
    """Lógica de interface para criação de nova entidade."""
    formatar_cabecalho("Nova Tarefa")
    try:
        titulo = input("Título: ").strip()
        descricao = input("Descrição: ").strip()
        
        if titulo and descricao:
            tarefa = {"titulo": titulo, "descricao": descricao}
            persistir_tarefa(tarefa)
            print(">>> Sucesso: Tarefa registrada no sistema.")
        else:
            print(">>> Erro: Campos obrigatórios não preenchidos.")
            
    except KeyboardInterrupt:
        print("\nOperação cancelada pelo arquiteto.")


def ler_tarefas(filename = NOME_ARQUIVO) -> list | None:
    tarefas = []
    try:

        with open(file=filename,mode='+r') as stream:
            tarefas = stream.readlines()
    except IOError as e:
        print("ERRO AO LER O ARQUIVO")
        return None
    except KeyboardInterrupt as e:
        print("O usuário interrompeu a operação")
        sys.exit(0)

    else:
        lista_limpa =[]
        for  i,tarefa in enumerate(tarefas):
            tarefa_limpa= tarefa.replace("\n","").strip().split("|")
            
            lista_limpa.append({"titulo":tarefa_limpa[0], "descricao": tarefa_limpa[1]})

        # RETORNO [[title,description],[title,description]]
        return lista_limpa



def listar_tarefas():

    tarefas = ler_tarefas(NOME_ARQUIVO)

    
    print(tarefas)


def renomear(old:str, new: str , /):
    file = Path(old)
    if file.exists:
        file.rename(new)
def excluir_tarefa():
    tarefas = ler_tarefas(NOME_ARQUIVO)

    if not tarefas:
        print("\n>>> O sistema não possui tarefas para excluir.")
        return

    formatar_cabecalho("LISTANDO TAREFAS:")
    for i, tarefa in enumerate(tarefas, start=1):
        print(f"{i:>3} - {tarefa['titulo']}")
        print(f"{'':>5} - {tarefa['descricao']}")

    try:
        escolha = input("\nDigite o ID para remover (ou Enter para cancelar): ")
        if not escolha: return
        
        indice = int(escolha) - 1

        if 0 <= indice < len(tarefas):
            tarefa_removida = tarefas.pop(indice)

            # --- RECRIAÇÃO DO ESTADO NO DISCO ---
            # Abrimos o arquivo original em modo 'w' (write) 
            # Isso limpa o arquivo e escreve a lista atualizada do zero.
            with open(NOME_ARQUIVO, mode="w", encoding="utf-8") as stream:
                for t in tarefas:
                    linha = f"{t['titulo']}|{t['descricao']}\n"
                    stream.write(linha)
            
            print(f"\n>>> Sucesso: '{tarefa_removida['titulo']}' removida.")
        else:
            print("\n>>> Erro: ID fora do intervalo.")

    except ValueError:
        print("\n>>> Erro: Entrada inválida.")
               

def exibir_menu():
    formatar_cabecalho("Organizador de Tarefas")
    for chave, rotulo in OPCOES_MENU.items():
        print(f" [{chave}] - {rotulo}")
    print("-" * 25)

def loop_principal():
    while True:
        exibir_menu()
        try:
            escolha = input("Selecione a operação: ").strip()
        except KeyboardInterrupt as e:
            formatar_cabecalho("Encerrando programa")
            sys.exit(0)
        match escolha:
            case "1":
                coletar_dados_tarefa()
            case "2":
                listar_tarefas()
            case "3":
                excluir_tarefa()
                print("Encerrando sistemas... Até logo, Arquiteto.")
                sys.exit(0)
            case 4:
                print("Saindo!!!")
            case _:
                print("Erro: Opção inválida no barramento de dados.")

if __name__ == "__main__":
    loop_principal()