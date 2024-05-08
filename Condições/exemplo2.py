#Declaração de Variáveis
altura = float(0);
ano_nascimento = int(0);
idade = int(0);
nome = str('');
tem_cnh = bool(False);
 
#Entrada de Dados
nome = str(input('Digite o seu nome: '));
ano_nascimento = int(input('Digite seu ano de nascimento: '));
altura = float(input('Quantos Metros voçê tem de Altura: '));
tem_cnh =bool(input('Voçê tem CNH?:(Aperte ENTER se não tiver): '));
 
#Processamento
if ( ano_nascimento < 1900 or ano_nascimento > 2020 ):
    print('Digite um ano de nascimento entre 1900 e 2020');
    exit();
 
idade = (2024 - ano_nascimento);
 
#Saída de Dados
 
print(f'\nOlá, {nome}');
print(f'Você nasceu no ano {ano_nascimento}');
print(f'Você tem: {idade} anos');
print(f'Voçê tem: {altura} metros');
 
if ( tem_cnh == True ):
    print('O usuário tem CNH, portanto pode dirigir.');
else:
    print('O usuário NÃO tem CNH, voçê não pode dirigir.');