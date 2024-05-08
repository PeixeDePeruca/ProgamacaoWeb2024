Numero = float(0);
 
 
print('\nVerificar se o número é divisivel por 3 e 5\n');
 
Numero = int(input('Digite o número: '));
 
if(Numero % 3 == 0 and Numero % 5 == 0):
    print('\nO número é divisivel por 3 e 5');
else:
    print('\nO número não é divisivel por 3 e 5');
 
if(Numero % 3 == 0):
    print('\nO número é divisivel por 3');
else:
    print('\nO número não é divisivel por 3');
   
if(Numero % 5 == 0):
    print('\nO número é divisivel por 5');
 
else:
    print('\nO número não é divisivel por 5');