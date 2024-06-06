PpToVote = int(0);
count = int(1);
 
inputVote = int(0);
 
# Votos possíveis
candidato1 = int(0);
candidato2 = int(0);
candidato3 = int(0);
candidato4 = int(0);
vNull = int(0);
vBlank = int(0);
 
print('\nEleição em andamento....Digite quantas pessoas irão votar.');
 
PpToVote = int(input("Digite: "));
 
while ( count <= PpToVote):
    inputVote = int(input(f'Cidadão, Digite seu voto: '));
   
    if ( inputVote < 1 or inputVote > 6 ):
        print('Voto inválido. Tente novamente. . .');
    else:
        if ( inputVote == 1 ):
            candidato1 = candidato1 + 1;
        if ( inputVote == 2 ):
            candidato2 = candidato2 + 1;
        if ( inputVote == 3 ):
            candidato3 = candidato3 + 1;
        if ( inputVote == 4 ):
            candidato4 = candidato4 + 1;
        if ( inputVote == 5 ):
            vNull = vNull + 1;
        if ( inputVote == 6 ):
            vBlank = vBlank + 1;
       
        count = count + 1;
 
print('\nContagem de votos em andamento . . . \n');
 
print(f'Candidato 1: {candidato1}');
print(f'Candidato 2: {candidato2}');
print(f'Candidato 3: {candidato3}');
print(f'Candidato 4: {candidato4}');
print(f'Votos Nulos: {vNull}');
print(f'Votos Brancos: {vBlank}');