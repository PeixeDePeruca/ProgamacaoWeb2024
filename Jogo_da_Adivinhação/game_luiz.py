#jogo de adivinhação 

import random;
import os;
import time;
SortedNumber = int(0);
dificuldade = int(0);
opçãoDoJogador = int(0);
dicas = int(0);

while (dificuldade != 1):
    print('\n O jogo consiste no jogador tentar adivinhar um número aleatório gerado pelo sistema \n O ' +
      'jogador terá 4 TENTATIVAS com um número variável de dicas para cada dificuldade. \n ')

    print('O quanto burro você é?' + '\n' + '- Muito Burro      (1 = Fácil    - 1 a 25)'
      + '\n' +'- Um Pouco Burro         (2 = Médio    - 1 a 50)' + '\n' + '- Eu sou um Gênio! (3 = Difícil  - 1 a 100)\n')
    
    dificuldade = int(input('Escolha : '));
    
    if (dificuldade > 3):
        print('\n Escolha apenas de 1 a 3');
        time.sleep(3)
        os.system("cls")
    else:
        time.sleep(3)
    
    if(dificuldade == 1):
        print('Aah, então você quer algo leve huh?');
        SortedNumber = random.randint(1 , 25);
    
    if(dificuldade == 2):
        print('Então você gosta de um desafio é?');
        SortedNumber = random.randint(1 , 50);
    
    if(dificuldade == 3):
        print('Tá se achando demais ein,vamos ver se você é tão bom assim');
        SortedNumber = random.randint(1 , 100);


count = 4;

while(count > 0):
    
    opçãoDoJogador = int(input('\n Digite um número: '));
    
    if(opçãoDoJogador == SortedNumber):
        print(f'\nÉ o que mas que p.....hmm foi apenas sorte,não signifíca nada....vamos lá jogue de novo,vamos ver se você é bom mesmo hehehe...')
        
    else:
        print(f'\n(Sárcasmo) Awn que pena,mais sorte na próxima hehehe...vamos vamos tente de novo,apenas 10 moedas,aproveite! ');
    
    count = (count - 1);
    

