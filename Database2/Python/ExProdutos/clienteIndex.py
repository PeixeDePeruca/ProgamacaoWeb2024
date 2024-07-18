import cliente;
from os import system;
 
#variavel
inputMenu = int(0);
 
while(True):
   
    system('cls');
   
    print(f"_____________|BANCO DE DADOS|______________");
    print("|Digite [0] para sair.                    |");
    print("|Digite [1] para ADICIONAR cliente.       |");
    print("|Digite [2] para SELECIONAR um Cliente.   |");
    print("|Digite [3] para LISTAR todos os clientes.|");
    print("|Digite [4] para DELETAR um cliente.      |");
    print("|Digite [5] para ATUALIZAR um cliente.    |");
    print(f"-------------------------------------------");
    inputMenu = int(input("Digite: "))
   
    if(inputMenu < 0 or inputMenu > 5):
        print("Digite apenas valores que estão no menu");
   
    if(inputMenu == 0):
        print("Encerrando Sistema");
        break;
   
    if(inputMenu == 1):
       
        print('\nVamos adicinar umm novo cliente.')
       
        try:
            name = input("Digete o NOME do cliente:\n")
            cpf = input("Digete o CPF do cliente:\n")
            email = input("Digete o EMAIL do cliente:\n")
            phone = input("Digete o telefone cliente:\n")
           
            response = cliente.create(name , cpf , email , phone)
           
           
            print(response['message']);
 
        except:
           
            print("\nSomenthing went wrog")
           
           
    if(inputMenu == 2):
        print("\nProcurar cliente pelo nome.")
       
        try:
            nomeCliente = input("Nome do cliente:")
           
            response = cliente.find(name);
               
            print(f'\n{response['message']}');
           
               
            if (response['status'] == 200):
                print(f"\nID | NOME | CPF | EMAIL | TELEFONE");
                print(response['data']);
        except:
          print("\nSomenthing went wrog");
       
           
    if(inputMenu == 3):
        print('\nLista de clientes')
 
        response = cliente.select()
 
        if (response['status'] == 201):
           
            print("|  ID  |  NOME  |  CPF  |  EMAIL  |  TELEFONE  |")
            for customer in response['data']:
               
                print(f"|  {customer[0]}  |  {customer[1]}  |  {customer[2]}  |  {customer[3]}  |  {customer[4]}")
        else:
            print(response['data'])
            print("\nAlgo deu errado")
 
    input("---|Digite 'ENTER' para continuar|---")
 
           
 