import re
import string
import secrets

# Configurações de domínio
CARACTERES = string.ascii_letters + string.punctuation + string.digits

def random_choice(choices: str) -> str:
    """Utiliza secrets para garantir aleatoriedade criptograficamente segura."""
    return secrets.choice(CARACTERES)


def generate_secure_password(tam: int = 12) -> str:
    """Gera uma senha e garante que ela seja válida antes de retornar."""
    while True:
        password = "".join(random_choice(CARACTERES) for n in range(tam))
        if is_valid_password(password):
            return password

def is_valid_password(password: str) -> bool:
    """
    Valida a política de senha:
    - ^ e $ : Garante que a string tenha EXATAMENTE o tamanho definido.
    - (?=.*[A-Z]) : Esse pattern ignora quaisquer quantidade de caracteres até encontrar um que pertence ao grupo [A-Z].
    - (?=.*[a-z]) :  Esse pattern ignora quaisquer quantidade de caracteres até encontrar um que pertence ao grupo [a-z].
    - (?=.*\\d) : Esse pattern ignora quaisquer quantidade de caracteres até encontrar um que pertence ao grupo [0-9].
    - (?=.*[...]) : Ao menos um caractere especial (colchetes escapados).
    """
    valid_pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%*(){}\[\]><!|]).{12}$"
    return bool(re.fullmatch(valid_pattern, password))

# Exemplo de execução
if __name__ == "__main__":
    nova_senha = generate_secure_password(12)
    print(f"Senha Gerada: {nova_senha}")
    print(f"É válida: {is_valid_password(nova_senha)}")