#Declaração de Variáveis

altura = float(0);
largura = float(0);
resultado = float(0);

#explicação do algoritmo
print('O algoritmo vai solicitar duas informações');
print('Respectivamente: Altura e Largura. Ao final,a área do retâgulo será calculada ');

#Entrada de Dados (input)
altura = float(input('Digite a Altura: '));
largura = float(input('Digite a Largura: '));

#Processamento (instruções)
resultado = altura * largura;

#saida de dados (output)
print(f'A área do retângulo é: {resultado}'); 