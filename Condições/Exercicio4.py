#ano bissexto ou não?
 
print('O algoritmo a seguir irá verificar se o ano é Bissexto');
 
Ano = int(0);
Resultado = int(0);
 
Ano = int(input('Digite qual é o ano: '));
 
Resultado = (Ano % 4 );
 
if(Ano < 0 or Ano > 2050):
    print('\nDigite somente anos validos');
    exit();
 
if (Resultado == 0):
    print(f'\nO ano {Ano} é bissexto')
else:
    print(f'\nO ano {Ano} não é bissexto');
    
