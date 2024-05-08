# calcular o desconto na compra (escolher contexto), solicitar valor da compra e desconto, calcular o desconto na compra
#EXIBIR - VALOR ORGINAL - VALOR DO DESCONTO - VALOR COM DESCONTO


ValorCompra = float(0);
ValorDesconto = float(0);
ValorComDesconto = float(0);
ValorTotal = float(0);


ValorCompra = float(input('\n Digite o valor da compra: \n '));
ValorDesconto = float(input('\n Digite o valor do Desconto: \n '));

ValorComDesconto = (ValorCompra * ValorDesconto) /100;
ValorTotal = ValorCompra - ValorComDesconto;

print(f'\n O valor da compra é: {ValorTotal}\n');