inputMenu = int(-1);
nota = int(0);
 
while ( inputMenu != 0 ):
    print(f'\n------------------------------------------');
    print('Digite 1 para acessar o algoritmo de  xxxxx.');
    print('Digite 0 para encerrar a aplicação.');
   
    inputMenu = int(input('Digite: '));
   
    if( inputMenu < 0 or inputMenu > 1 ):
        print('\nDigite apenas números presentes no menu.\n')
   
    if ( inputMenu == 1 ):
        #Algoritmo de aprovação
       
        nota = float(input('Digite uma nota (0 a 10): '));
       
        if (nota >= 7):
            print(f'O aluno foi APROVADO.');
        else:
            print(f'O aluno foi REPROVADO.');