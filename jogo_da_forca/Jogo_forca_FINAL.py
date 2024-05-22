import random

# Palavras secretas
secretWords = ['pizza', 'blindado', 'peruca', 'mussolini', 'hentai', 'pokemon']

def choose_word():
    return random.choice(secretWords).lower()

def gameplay(word):
    word_completion = ['_'] * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6

    print(' '.join(word_completion))
    print("\n")

    while not guessed and tries > 0:
        guess = input("Digite uma letra para adivinhar a palavra secreta: ").lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("Você já tentou essa letra:", guess)
            else:
                if guess not in word:
                    print(guess, "não está na palavra.")
                    tries -= 1
                    guessed_letters.append(guess)
                else:
                    print("Bom trabalho,", guess, "está na palavra!")
                    guessed_letters.append(guess)
                    for i in range(len(word)):
                        if word[i] == guess:
                            word_completion[i] = guess
                    if '_' not in word_completion:
                        guessed = True
        else:
            if len(guess) == len(word) and guess.isalpha():
                if guess in guessed_words:
                    print("Você já tentou a palavra:", guess)
                else:
                    if guess != word:
                        print(guess, "não é a palavra.")
                        tries -= 1
                        guessed_words.append(guess)
                    else:
                        guessed = True
                        word_completion = list(word)
            else:
                print("Palpite inválido.")

        print(' '.join(word_completion))
        print("\n")

    if guessed:
        print("Parabéns, você adivinhou a palavra, VOCÊ VENCEU!")
    else:
        print("Sinto muito, você não adivinhou a palavra. A palavra era " + word + ",Hmm Talvez da próxima vez!")

def main():
    print('\n- BEM VINDO AO JOGO DA FORCA - \n')
    secret_word = choose_word()
    gameplay(secret_word)

if __name__ == "__main__":
    main()
