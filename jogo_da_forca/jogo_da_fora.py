import random;
# palavras secretas (pizza , blindado , peruca , mussolini)

print('\n- BEM VINDO A O JOGO DA FORCA - \n');

secretWords = ['pizza' , 'blindado' , 'peruca' , 'mussolini', 'hentai','pokemon' ];
wordGenerator = str('');
TryKey = str('');


def wordGenerator():
    contextChoice = random.randint(1 , 3);
    
    global secretWords;
    wordGenerator = str('');

TryKey = str(input ('Digite a LETRA desejada para adivinhar a palavra -> '));

#print('____________________')


if (secretWords != 'pizza , blindado , peruca , mussolini' ):
    print('Você ERROU a letra!\n');
else:
    print('Você ACERTOU a letra!\n');
    