from random import randint
random_words = ['banana', 'morango', 'pessoa', 'navio','oceano', 'incostitucionalicimamente','amizade','familia','videogame','basquete','atleta']
word = random_words[randint(0,len(random_words))].upper()
word_display = ['_'] *len(word)
print('JOGO DA FORCA, VAMOS LÁ!!')
chances = 5
guesses = []

while True:
    guess = str(input("\nDigite um palpite de letra: ")) .upper() .strip()
    while guess in guesses:
        print('Essa letra já foi chutada.')
        guess = str(input("\nDigite um palpite de letra: ")).upper() .strip()

    while guess == '':
        print('Não é permitido um print vazio!')
        guess = str(input("\nDigite um palpite de letra: ")).upper() .strip()

    if guess in word:
        print('Essa letra existe')
        guesses.append(guess)
        print(f'Os seus chutes foram: {guesses}')
        for i in range(len(word)):
            if word[i] == guess:
                word_display[i] = guess
        for i in word_display:
            print(i,end='')

    else:
        print(f'Essa letra não existe. te restam {chances - 1} chances!')
        chances -= 1
        guesses.append(guess)
        print(f'Os seus chutes foram: {guesses}')
        for i in word_display:
            print(i,end='')

    if '_' not in word_display:
        print('\nParabénss, você ganhou!!!')
        print(f'\nA palavra era {word_display}')
        break

    if chances == 0:
        print('\nVoce perdeu, suas chances acabaram')
        break
    
