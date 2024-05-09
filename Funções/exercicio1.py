#o algoritmo faz conversões :3

print ('\nEsse algoritmo faz conversões,escolha uma das opções abaixo \n \n'+'Opção 1 Converter TEMPERATURA \n'
       + 'Opção 2 Converter DISTÂNCIA\n' + 'Opção 3 Converter METROS PARA PÉS\n');


#conversão de temperatura
def celsiusToFahrenheit(celsius:float):
    fahrenheit = float(0);
    
    fahrenheit = (celsius * 1.8) + 32;

#conversão de distância
def meterToFeet(meters:float):
    feet = float(0);
    
    feet = meters * 3.2808
    
    return feet;

#metros para pés
def kilometerToMiles(kilometers:float):
    miles = float(0);
    
    miles = kilometers * 0.62137119;
    
    return miles;

#result = float(0);

#result = celsiusToFahrenheit(27);

#print(f'27° C equivale a {result} ºF');

#result = kilometerToMiles(1.8);

#print(f'1.8 Meters = {round(result , 2)} Feet');
#testes das funções