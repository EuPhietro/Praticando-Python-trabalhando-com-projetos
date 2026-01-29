import string 

#============================================================================================
# Crie um programa que receba um texto e exiba todas as palavras que possuem mais de 10 letras. 
# Caso nenhuma palavra longa seja encontrada, o programa deve avisar o usuário.
#============================================================================================

def classificar_palavras(txt: str) -> dict:
    """
    Analisa um texto, filtra pontuações e retorna um dicionário com a 
    contagem de palavras que possuem mais de 10 caracteres.
    """
    palavras_classificadas = dict()
    
    # Tabela de tradução para remoção de pontuação
    remover_caracteres = str.maketrans("", "", string.punctuation)
    
    # Limpeza e tokenização
    texto_limpo = txt.translate(remover_caracteres).lower().split()
    palavras_unicas = set(texto_limpo)

    for word in palavras_unicas:
        if len(word) > 10:
            palavras_classificadas[word] = texto_limpo.count(word)
            
    return palavras_classificadas

def executar_teste(id_teste, texto):
    """Executa o teste e exibe o resultado conforme a regra de negócio."""
    print(f"TESTE {id_teste}:")
    print(f"Entrada: {texto}")
    
    resultado = classificar_palavras(texto)

    if resultado:
        print("PALAVRAS LONGAS ENCONTRADAS:")
        for palavra, contagem in resultado.items():
            print(f"- {palavra}: {contagem} ocorrência(s)")
    else:
        print("AVISO: Nenhuma palavra longa (mais de 10 letras) encontrada.")
    
    print("-" * 30)

def main():
    # 1. Teste com palavras longas (Cenário de sucesso)
    teste_1 = "A programação estruturada facilitou o desenvolvimento de grandes sistemas computacionais"
    
    # 2. Teste sem palavras longas (Cenário de aviso)
    teste_2 = "O Python é uma linguagem rápida."
    
    # 3. Teste com pontuação e repetição (Cenário de robustez)
    teste_3 = "Inconstitucionalissimamente! Sim, essa palavra é inconstitucionalissimamente longa."

    # Execução dos testes
    executar_teste(1, teste_1)
    executar_teste(2, teste_2)
    executar_teste(3, teste_3)

if __name__ == "__main__":
    main()