nota = float(0);
nota = float(input('\nDigite uma nota (0 a 10): '))
 
if ( nota >= 7 and nota < 10 ):
    print(f'\nO aluno foi APROVADO.');
 
if ( nota < 7):
    print(f'\nO aluno for REPROVADO.');
   
if( nota > 10 ):
    print(f'\n\nNota é somente de 0 a 10\n');