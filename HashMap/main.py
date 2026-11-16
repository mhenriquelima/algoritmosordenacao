from hash_table import Aluno, HashTableChaining

M = 11  # tamanho da tabela hash


# ---------------------------------------------------------------------------
# Validação de entrada
# ---------------------------------------------------------------------------

def validar_inteiro(texto, minimo=None, maximo=None):
    """Converte `texto` em inteiro. Retorna (valor, None) se válido ou
    (None, mensagem_de_erro) se inválido."""
    texto = texto.strip()
    if texto == "":
        return None, "O valor não pode ser vazio."
    # Aceita apenas dígitos (com sinal opcional) — recusa "12.5", "1e3", "abc", "12 34"
    corpo = texto[1:] if texto[0] in "+-" else texto
    if not corpo.isdigit() or not corpo.isascii():
        return None, f"'{texto}' não é um número inteiro válido."
    valor = int(texto)
    if minimo is not None and valor < minimo:
        return None, f"O valor deve ser maior ou igual a {minimo}."
    if maximo is not None and valor > maximo:
        return None, f"O valor deve ser menor ou igual a {maximo}."
    return valor, None


def ler_inteiro(mensagem, minimo=None, maximo=None):
    """Pede um inteiro ao usuário até que um valor válido seja digitado."""
    while True:
        valor, erro = validar_inteiro(input(mensagem), minimo, maximo)
        if erro is None:
            return valor
        print(f"  Entrada inválida: {erro} Tente novamente.")


def ler_matricula():
    return ler_inteiro("Matrícula: ", minimo=0)


def ler_nome():
    while True:
        nome = input("Nome: ").strip()
        if nome:
            return nome
        print("  Entrada inválida: o nome não pode ser vazio. Tente novamente.")


def ler_idade():
    return ler_inteiro("Idade: ", minimo=1, maximo=150)


def mostrar_endereco(tabela, matricula):
    endereco = tabela.hash_function(matricula)
    print(f"  h({matricula}) = {matricula} mod {tabela.tamanho} = {endereco}")
    return endereco


# ---------------------------------------------------------------------------
# Operações do menu
# ---------------------------------------------------------------------------

def opcao_inserir(tabela):
    print("\n--- Inserir novo aluno ---")
    matricula = ler_matricula()
    endereco = mostrar_endereco(tabela, matricula)
    # Verifica duplicidade antes de pedir os demais dados
    if tabela.search(matricula) is not None:
        print(f"Erro: já existe um aluno com a matrícula {matricula}. Cadastro não realizado.")
        return
    nome = ler_nome()
    idade = ler_idade()
    if tabela.insert(Aluno(nome, idade, matricula)):
        print(f"Aluno inserido com sucesso no endereço {endereco}.")
    else:
        print(f"Erro: já existe um aluno com a matrícula {matricula}. Cadastro não realizado.")


def opcao_buscar(tabela):
    print("\n--- Buscar aluno ---")
    matricula = ler_matricula()
    endereco = mostrar_endereco(tabela, matricula)
    aluno = tabela.search(matricula)
    if aluno:
        print(f"Encontrado no endereço {endereco}: {aluno}")
    else:
        print(f"Aluno com matrícula {matricula} não encontrado.")


def opcao_remover(tabela):
    print("\n--- Remover aluno ---")
    matricula = ler_matricula()
    endereco = mostrar_endereco(tabela, matricula)
    if tabela.remove(matricula):
        print(f"Aluno com matrícula {matricula} removido do endereço {endereco}.")
    else:
        print(f"Aluno com matrícula {matricula} não encontrado. Nada foi removido.")


def opcao_exibir(tabela):
    print("\n--- Tabela Hash ---")
    tabela.display()


MENU = """
========= TABELA HASH - ALUNOS =========
 1 - Inserir novo aluno
 2 - Buscar aluno
 3 - Remover aluno
 4 - Exibir tabela hash
 0 - Encerrar sistema
========================================"""

ACOES = {
    1: opcao_inserir,
    2: opcao_buscar,
    3: opcao_remover,
    4: opcao_exibir,
}


def main():
    tabela = HashTableChaining(M)
    while True:
        print(MENU)
        opcao = ler_inteiro("Escolha uma opção: ", minimo=0, maximo=4)
        if opcao == 0:
            print("Encerrando o sistema...")
            break
        ACOES[opcao](tabela)


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nEncerrando o sistema...")
