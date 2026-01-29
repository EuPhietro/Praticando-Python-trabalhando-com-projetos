import string
import math

TABLE = str.maketrans("", "", string.punctuation)

def get_numbers(txt: str) -> list | None:
    try:
        clean_txt = txt.translate(TABLE).strip().split()
        return [float(n) for n in clean_txt]
    except (ValueError, TypeError):
        print("O usuário inseriu dados inválidos")
        return None

def calc(numbers: list, mode: str) -> float | None:
    """
    Executa operações matemáticas agregadas sobre uma lista de números.
    """
    if not numbers:
        return None

    # Definição das lógicas internas
    def subtrair(nums):
        res = nums[0]
        for n in nums[1:]:
            res -= n
        return res

    def multiplicar(nums):
        res = nums[0]
        for n in nums[1:]:
            res *= n
        return res

    def dividir(nums):
        # Proteção de infraestrutura: evita crash por divisão por zero
        try:
            res = nums[0]
            for n in nums[1:]:
                res /= n
            return res
        except ZeroDivisionError:
            print("Erro: Divisão por zero detectada.")
            return None

    # Mapeamento de funções (sem executá-las ainda)
    operacoes = {
        "+": lambda: sum(numbers),
        "-": lambda: subtrair(numbers),
        "*": lambda: multiplicar(numbers),
        "/": lambda: dividir(numbers)
    }

    # Executa apenas a operação solicitada
    operacao_selecionada = operacoes.get(mode)
    
    if operacao_selecionada:
        return operacao_selecionada()
    
    print(f"Modo '{mode}' não reconhecido.")
    return None

# --- Teste de Execução ---
entrada = "100, 10, 2"
nums = get_numbers(entrada)

if nums:
    print(f"Soma (+): {calc(nums, '+')}")
    print(f"Subtração (-): {calc(nums, '-')}")
    print(f"Multiplicação (*): {calc(nums, '*')}")
    print(f"Divisão (/): {calc(nums, '/')}")