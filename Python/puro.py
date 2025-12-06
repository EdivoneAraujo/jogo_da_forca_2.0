# Importa o módulo 'random', que permite gerar valores aleatórios.
# Aqui, será usado para escolher uma palavra secreta aleatória da lista.
import random

# === FUNÇÃO GENÉRICA PARA ESCOLHER PALAVRAS === #
def escolher_palavra(tema, nivel):
    # Dicionário com o nome do tema e os caminhos dos arquivos de palavras correspondentes
    arquivos = {
        "capitais": [
            "Python/arquivos/capitais1.txt",  # nível 1 - fácil
            "Python/arquivos/capitais2.txt",  # nível 2 - médio
            "Python/arquivos/capitais3.txt"   # nível 3 - difícil
        ],
        "animais": [
            "Python/arquivos/animais1.txt",
            "Python/arquivos/animais2.txt",
            "Python/arquivos/animais3.txt"
        ],
        "frutas": [
            "Python/arquivos/frutas1.txt",
            "Python/arquivos/frutas2.txt",
            "Python/arquivos/frutas3.txt"
        ]
    }

    # Escolhe o arquivo correspondente ao tema e nível informados
    nome_arquivo = arquivos[tema][nivel - 1]

    # Abre o arquivo no modo leitura ('r') com codificação UTF-8
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        # Lê todas as linhas do arquivo e armazena na lista 'palavras'
        palavras = arquivo.readlines()

    # Escolhe aleatoriamente uma palavra da lista
    # .strip() remove espaços e quebras de linha; .lower() deixa tudo minúsculo
    palavra_sorteada = random.choice(palavras).strip().lower()

    # Retorna a palavra sorteada como string simples
    return palavra_sorteada


# === FUNÇÕES AUXILIARES === #
def lin():
    # Imprime uma linha de separação para organização visual no terminal
    print('__' * 10)


def continuar():
    # Pergunta se o jogador deseja continuar após o jogo terminar
    # Retorna a resposta já convertida para minúscula e sem espaços
    return input('Deseja continuar? (s/n): ').lower().strip()


# === FUNÇÃO PRINCIPAL DO JOGO === #
def jogo_da_forca():
    lin()
    print('Olá jogador!\nVamos escolher um tema?')
    print('1 - Capitais brasileiras\n2 - Animais\n3 - Frutas\n0 - Encerrar o jogo')

    # Dicionário que mapeia as opções numéricas aos nomes dos temas
    temas = {1: "capitais", 2: "animais", 3: "frutas"}

    # --- ESCOLHA DO TEMA --- #
    op = -1  # inicializa com valor inválido
    while op not in [0, 1, 2, 3]:
        entrada = input('Digite sua opção: ')
        # Garante que a entrada seja válida (apenas 0, 1, 2 ou 3)
        if entrada in ['0', '1', '2', '3']:
            op = int(entrada)
        else:
            print("Por favor, escolha uma opção válida: 0, 1, 2 ou 3.")

    # Se o jogador quiser sair, o jogo encerra
    if op == 0:
        print('Jogo encerrado.')
        lin()
        return

    # --- ESCOLHA DO NÍVEL --- #
    nivel = 0  # também começa com valor inválido
    while nivel not in [1, 2, 3]:
        entrada_nivel = input("Escolha o nível: 1 (fácil), 2 (médio) ou 3 (difícil): ")
        # Garante que o nível seja 1, 2 ou 3
        if entrada_nivel in ['1', '2', '3']:
            nivel = int(entrada_nivel)
        else:
            print("Por favor, escolha apenas 1, 2 ou 3.")

    # Chama a função para escolher uma palavra com base no tema e nível
    palavra_secreta = escolher_palavra(temas[op], nivel)

    # --- CONFIGURAÇÕES INICIAIS DO JOGO --- #
    letras_usuario = []  # guarda as letras que o jogador já tentou
    chances = 7          # número total de tentativas
    ganhou = False        # indica se o jogador venceu

    print(f'Você tem {chances} chances para descobrir a palavra.')

    # === LOOP PRINCIPAL DO JOGO === #
    while chances > 0 and not ganhou:
        print()

        # Mostra o progresso da palavra (letras descobertas e underscores)
        for letra in palavra_secreta:
            if letra in letras_usuario:
                print(letra, end=' ')
            else:
                print('_', end=' ')
        print()

        # Pede uma nova letra ao jogador
        tentativa = input('Escolha uma letra: ').lower().strip()

        # --- VALIDAÇÃO DA LETRA --- #
        if len(tentativa) != 1:  # apenas uma letra por vez
            print("Digite apenas uma letra.")
            continue

        # Garante que o caractere digitado esteja entre 'a' e 'z' (sem usar isalpha)
        if tentativa < 'a' or tentativa > 'z':
            print("Digite apenas letras de A a Z.")
            continue

        # Se a letra já foi tentada, avisa o jogador
        if tentativa in letras_usuario:
            print('Você já escolheu essa letra. Tente novamente.')
            continue

        # Adiciona a letra à lista de tentativas do jogador
        letras_usuario.append(tentativa)

        # Verifica se a letra está na palavra secreta
        if tentativa in palavra_secreta:
            print('✅ Letra correta!')
        else:
            chances -= 1  # perde uma chance
            print('❌ Letra incorreta! Você perdeu uma chance.')

        # --- VERIFICA SE O JOGADOR JÁ DESCOBRIU TODAS AS LETRAS --- #
        ganhou = True  # assume que ganhou
        for letra in palavra_secreta:
            # Se houver alguma letra ainda não adivinhada, muda para False
            if letra not in letras_usuario:
                ganhou = False
                break

        # Mostra quantas chances ainda restam
        print('Chances restantes:', chances)

    # === RESULTADO FINAL === #
    lin()
    if ganhou:
        # Caso o jogador tenha acertado todas as letras
        print(f"🎉 Parabéns! Você ganhou o jogo!\nA palavra era '{palavra_secreta}'.")
    else:
        # Caso tenha acabado as chances
        print(f"💀 Você perdeu.\nA palavra era '{palavra_secreta}'.")
    lin()


# === EXECUÇÃO DO JOGO === #
if __name__ == "__main__":
    # Chama a função principal apenas se o arquivo for executado diretamente
    jogo_da_forca()