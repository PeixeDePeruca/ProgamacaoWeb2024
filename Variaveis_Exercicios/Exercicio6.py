# Variáveis
 
saldo = float(0);
taxa = float(0);
meses = int(0);
resultado = float(0);
saldoFinal = float(0);
 
# Explicação
 
print('O algoritmo calculará juros simples com base no saldo, taxa e período inseridos.');
 
#Entrada de dados
 
saldo = float(input('valor na conta: '));
taxa = float(input('Digite a porcentagem de rendimento (0 a 20%): '));
taxa = float(input('Vai deixar o valor rendendo por quantos meses? '));
 
# Processamento
 
rendimento = (( (taxa / 100 ) * saldo) * meses);
saldo_final = (saldo + rendimento);
 
#saída de dados
print(f"Saldo Inicial: {round(saldo , 2)} R$");
print(f"Rendimento Total: {round(rendimento , 2)} R$");
print(f"Saldo Total: {round(saldo_final , 2)} R$");