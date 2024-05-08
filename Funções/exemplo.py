
def parOuImpar(num:int):
    verify = int(0);
       
    verify = num % 2;
        
    if(verify == 0):
        return("o número é PAR");
    else:
        return('O número é IMPAR');
        
number = int(0);
result = str('');
    
number = int(input('\n Digite: '));
    
result = parOuImpar(number);
    
print(f'\n o resultado é: {result}');    