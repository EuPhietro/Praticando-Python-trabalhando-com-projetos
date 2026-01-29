
def contar_vogais(txt:str):
    vogais = tuple("aeiouáéíóúâêîôûãẽĩõũ")
    clean_txt = txt.lower().strip().replace(" ","")
    counter = 0
    for char in clean_txt:
        if char in vogais:
            counter +=1
    
    return counter




def main():
    try:
        i_txt = input("Digite um texto para contar as vogais: ")
    except (ValueError, TypeError) as e:
        print("Entrada inválida!")
    else:
        print(contar_vogais(i_txt))



if __name__ == "__main__":
    main()




