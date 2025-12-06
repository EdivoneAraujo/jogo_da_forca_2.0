import random

def escolher_palavra(tema, nivel):
    arquivos = {
        "capitais": [
            "Python/arquivos/capitais1.txt",
            "Python/arquivos/capitais2.txt",
            "Python/arquivos/capitais3.txt"
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
    nome_arquivo = arquivos[tema][nivel - 1]
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        palavras = arquivo.readlines()
    palavra_sorteada = random.choice(palavras).strip().lower()
    return palavra_sorteada

def lin():
    print('__' * 10)

def continuar():
    return input('Deseja continuar? (s/n): ').lower().strip()

def jogo_da_forca():
    lin()
    print('Olá jogador!\nVamos escolher um tema?')
    print('1 - Capitais brasileiras\n2 - Animais\n3 - Frutas\n0 - Encerrar o jogo')
    temas = {1: "capitais", 2: "animais", 3: "frutas"}
    op = -1
    while op not in [0, 1, 2, 3]:
        entrada = input('Digite sua opção: ')
        if entrada in ['0', '1', '2', '3']:
            op = int(entrada)
        else:
            print("Por favor, escolha uma opção válida: 0, 1, 2 ou 3.")
    if op == 0:
        print('Jogo encerrado.')
        lin()
        return
    nivel = 0
    while nivel not in [1, 2, 3]:
        entrada_nivel = input("Escolha o nível: 1 (fácil), 2 (médio) ou 3 (difícil): ")
        if entrada_nivel in ['1', '2', '3']:
            nivel = int(entrada_nivel)
        else:
            print("Por favor, escolha apenas 1, 2 ou 3.")
    palavra_secreta = escolher_palavra(temas[op], nivel)
    letras_usuario = []
    chances = 7
    ganhou = False
    print(f'Você tem {chances} chances para descobrir a palavra.')
    while chances > 0 and not ganhou:
        print()
        for letra in palavra_secreta:
            if letra in letras_usuario:
                print(letra, end=' ')
            else:
                print('_', end=' ')
        print()
        tentativa = input('Escolha uma letra: ').lower().strip()
        if len(tentativa) != 1:
            print("Digite apenas uma letra.")
            continue
        if tentativa < 'a' or tentativa > 'z':
            print("Digite apenas letras de A a Z.")
            continue
        if tentativa in letras_usuario:
            print('Você já escolheu essa letra. Tente novamente.')
            continue
        letras_usuario.append(tentativa)
        if tentativa in palavra_secreta:
            print('✅ Letra correta!')
        else:
            chances -= 1
            print('❌ Letra incorreta! Você perdeu uma chance.')
        ganhou = True
        for letra in palavra_secreta:
            if letra not in letras_usuario:
                ganhou = False
                break
        print('Chances restantes:', chances)
    lin()
    if ganhou:
        print(f"🎉 Parabéns! Você ganhou o jogo!\nA palavra era '{palavra_secreta}'.")
    else:
        print(f"💀 Você perdeu.\nA palavra era '{palavra_secreta}'.")
    lin()

if __name__ == "__main__":
    jogo_da_forca()
