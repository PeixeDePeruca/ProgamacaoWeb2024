import random;
# palavras secretas (pizza , blindado , peruca , mussolini)

print('\n- BEM VINDO AO JOGO DA FORCA - \n');

secretWords = ['Pizza' , 'Blindado' , 'Peruca' , 'Mussolini', 'Hentai','Pokemon' ];
wordGenerator = str('');
TryKey = str('');

def funcao():
    contextChoice = random.randint(1 , 3);

    global secretWords
    wordChoice = str('');
    
    wordChoice = random.choice(secretWords)

    return wordChoice;


def gameplay(word:str):

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