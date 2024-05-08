print('O algoritmo a seguir irá calcular a sua idade de anos, irá calcular o número de dias e meses.');
 
Idade = int(0);
Meses = int(0);
Dias = int(0);
 
 
Idade = int(input('Digite sua Idade em Anos: '));
 
Dias = (Idade * 365);
Meses = (Idade * 12);
 
print (input(f'Você tem: {Dias} Dias de vida.'));
print(f'Você tem: {Meses} Meses.');
print(f'Você tem: {Idade} Anos');