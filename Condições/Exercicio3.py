#solicite ao usuario que digite a nota do aluno
#use uma estrutura de decisão (if-else) para verificar se a nota é maior ou igual a 7
#imprima a mensagem indicando se o aluno foi aprovado ou não

nota = float(0);
nome = str(' ')
 
print('O algoritmo a seguir irá verificar a nota do aluno.');
 
 
nome = str(input('Digite o nome do aluno: \n'));
nota = float(input('Digite a nota do aluno: \n'));
 
 
if( nota >= 7 ):
    print('\nO aluno foi aprovado');
else:
    print('/nO aluno foi reprovado');