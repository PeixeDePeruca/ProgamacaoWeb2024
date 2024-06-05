import datetime;

anoAtual = datetime.datetime.now();

restoDaDivisão = int(0);
nascimento = int(0);
idade = int(0);

print(f"O algoritmo verificará se o usuário poderá votar na próxima eleição\n");

nascimento = int(input("Digite seu ano de nascimento ->"));

idade = anoAtual.year - nascimento;

print(f"Sua idade é: {idade} anos\n");

restoDaDivisão = anoAtual.year % 5;

if ( restoDaDivisão == 0 ):
    print(f"\nEstamos em um ano de Eleição!");
else:
    print(f"Não estamos em um ano de Eleição!");    