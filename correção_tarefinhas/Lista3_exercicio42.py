PpToVote = ['Mario' , 'Luigi' , 'Daisy' , 'Toad' , 'Wario'];
count = int(0);
 
inputVote = int(0);
 
# Votos possíveis
voteOptions = [None , 0 , 0 , 0 , 0 , 0 , 0];
 
print('\nEleição para novo líder do Reino dos Cogumelo...');
 
while ( count < len(PpToVote)):
    inputVote = int(input(f'\n{PpToVote[count]}, digite seu voto: '));
   
    if ( inputVote < 1 or inputVote > 6 ):
        print('Voto inválido. Tente novamente. . .');
    else:
        voteOptions[inputVote] += 1;
       
        count = count + 1;
 
print('\nContagem de votos em andamento . . . \n');
 

 
print(f'Princesa Peach: {voteOptions[1]}');
print(f'Princesa Luna: {voteOptions[2]}');
print(f'Princesa Daisy: {voteOptions[3]}');
print(f'Bowser: {voteOptions[4]}');
print(f'Votos Nulos: {voteOptions[5]}');
print(f'Votos Brancos: {voteOptions[6]}');