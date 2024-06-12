numbers = [];
inputNumber = int(-1);
result = float(0);
sum = int(0);

#explicção
print("\nO algoritmo calculará a SOMA DOS VALORES PARES digitados");

print("\nDigite 0 para encerrar a conta5\nDigite números inteiros");

while (inputNumber != 0):
    
    inputNumber = int(input("\nDigite Aqui ->"));
    
    if (inputNumber == 0 ):
        break;
    else:
        numbers.append(inputNumber);
     
for i in range(0 , len(numbers) , 1 ):
    
    result = numbers[i] % 2;
    
    if (result == 0 ):
        sum = sum + numbers[i];
        
print(f"\nResultado da soma: {sum}");        
        