#criar vetor com num int e usar loop para conferir se estão
#em ordem crescente e daí print falando se esta ou n

numbers = [];
inputNumber = int(0);

while(True):

    inputNumber = int(input('Digite: '));
    
    if(inputNumber == 0):
        break;
    
    numbers.append(inputNumber);

    print("\nO algoritmo VERIFICARÁ se os números digitados no vetor estão em ORDEM CRESCENTE");

    print("\nDigite 1 para começar a verificação");

    numbers.sort();

    print(numbers);