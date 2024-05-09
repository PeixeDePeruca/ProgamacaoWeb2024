from temperatura import celsiusToFahrenheit;
from kmMilha import kilometerToMiles;
from metropezinho import meterToFeet;
#o algoritmo faz conversões :3

inputMenu = float(0);
number = float(0);

while(inputMenu != 1):
    inputMenu = int(input('\nEsse algoritmo faz conversões,escolha uma das opções abaixo \n \n'+'Opção 1 Converter TEMPERATURA \n'
        + 'Opção 2 Converter DISTÂNCIA\n' + 'Opção 3 Converter METROS PARA PÉS' + '\n-> :' ));

    if(inputMenu < 1 or inputMenu > 3):  
        print(f'\n Escolha apenas as alternativas disponíveis >:(\n');    
            
    if(inputMenu == 1):
        number = int(input('Quantos graus CELSIUS você deseja converter? '));
        result = celsiusToFahrenheit(number);
        print(f'O valor convertido é {result} Fahrenheit');
            
            
    if(inputMenu == 2):
        number = int(input('Quantos Quilômetros você deseja converter? '));
        result = kilometerToMiles(number); 
        print(f'O valor convertido é {int(result)} Milhas');
            
            
    if(inputMenu == 3):
        number = int(input('Quantos Metros você deseja converter? '));
        result = meterToFeet(number); 
        print(f'O valor convertido é {int(result)} Pés');