#verificar se um número é positivo,negativo ou zero

print('O algoritmo a seguir irá calcular se o número é positivo, negativo ou zero');
 
numero = float(0);
 
numero = float(input('Digite o número: '));
 
if( numero < 0 ):
    print('O número é negativo');
 
if( numero == 0):
    print('O número é zero')
 
if( numero >= 1 ):
    print('O número é positivo');
 
print('Demissão');