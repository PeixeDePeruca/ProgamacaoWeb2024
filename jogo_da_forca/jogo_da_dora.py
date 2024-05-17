import random;

# palavras secretas (pizza , blindado , peruca , mussolini , hentai , pokemon)

print('\n- BEM VINDO AO JOGO DA FORCA - \n');

#palavras da adivinhação 
secretWords = ['Pizza' , 'Blindado' , 'Peruca' , 'Mussolini', 'Hentai','Pokemon' ];
#numero de tentativas




wordGenerator = str('');
TryKey = str('');






def funcao():
    contextChoice = random.randint(1 , 3);

    global secretWords
    wordChoice = str('');
    
    wordChoice = random.choice(secretWords)

    return wordChoice;


def gameplay(word:str):

    tries = 6
    display = ['_'] *len(word)
    letras_erradas = [];
    
    
    while (tries > 0 and '_' in display):
    
        print(f'\nQuantidade de letras na palavra escolhida: {len(word)}');

        print(f'Tente adivinhar a palavra: {'_ ' * len(word)}')

    # Repetição para exibir todas as letras da palavra. Verificar letra por letra.
    # O usuário vai digitar apenas UMA letra, devemos verificar se ela está presente na palavra.
        for i in range( 0 , len(word) ):
            print(word[i]);




secretWord = str('');
secretWord = funcao();

print(f'A palavra Secreta era: {secretWord}');

gameplay(secretWord);