print('\nEsse algorito faz o calculo dos juros compostos :D \n');

initial_value = float(0);
tax = float(0);
months = int(0);
total_value = float(0);
initial_time = int(0);

initial_value = float(input('Digite o valor inicial '));
tax = float(input('Digite o valor da Taxa '));
months = int(input('Digite o número de meses com juros '));

total_value = initial_value

#conversão de taxa(o usuario digita o valor da taxa,eo algoritmo
# pega esse valor e divide por 100)
tax = (tax / 100);


while (initial_time < months):
    
    total_value = total_value * (1 + tax);
    initial_time += 1;
    
    print(f'-> no {initial_time}º mês o valor dos Juros foi: R${total_value} ')    
   
