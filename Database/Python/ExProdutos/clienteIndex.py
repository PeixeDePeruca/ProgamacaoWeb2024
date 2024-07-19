import Clientes;
from os import system;
 
#variavel
inputMenu = int(0);
subInputMenu = int(0);
 
while(True):
    system('cls');
    #Opções do Menu
   
    print("Digite [0] para sair.");
    print("Digite [1] para CRIAR um produto.");
    print("Digite [2] para buscar pelo cpf.");
    print("Digite [3] para buscar pelo email.");
    print("Digite [4] para listar.");
    print('Digite [5] para deletar.');
    print('Digite [6] para atualizar')
   
    inputMenu = int(input("Digite: "));
   
    if(inputMenu == 0):
        print("Encerrando Sistema");
        break;
   
    if(inputMenu == 1):
        print("Digite os dados solicitados para criar seu produto: ");
        try:
            name = input("Nome: ");
            cpf = input("Preço: ");
            email = input("Preço: ");
            phone = input("Quantidade: ");
       
            response = Clientes.create(name, cpf, email, phone)
       
            print(f'\n{response['message']}');
        except:
            print('Something went wrong');
       
    if(inputMenu == 2):
        print('\nVamos procurar pelo cpf.');
        try:
            cpf = input('CPF: ');
       
            response = Clientes.findByCPF(cpf);
           
            print(f'\n{response['message']}');
           
            if ( response['status'] == 200 ):
                print(f'\nID / NOME / CPF / EMAIL / PHONE');
                print(f'{response['data'][0]} / {response['data'][1]} / {response['data'][2]}  / {response['data'][3]} / {response['data'][4]}');
       
        except:
            print('Something went wrong');
           
   
    if(inputMenu == 3):
        print('\nVamos procurar pelo email.');
        try:
            email = input('EMAIL: ');
       
            response = Clientes.findByEmail(email);
           
            print(f'\n{response['message']}');
           
            if ( response['status'] == 200 ):
                print(f'\nID / NOME / CPF / EMAIL / PHONE');
                print(f'{response['data'][0]} / {response['data'][1]} / {response['data'][2]}  / {response['data'][3]} / {response['data'][4]}');
       
        except:
            print('Something went wrong');
         
    if(inputMenu == 4):
        print('\nLista de clientes');
 
        response = Clientes.select();
 
        if (response['status'] == 200):
           
            print("|  ID  |  NOME  |  CPF  |  EMAIL  |  TELEFONE  |");
            for customer in response['data']:
               
                print(f"|  {customer[0]}  |  {customer[1]}  |  {customer[2]}  |  {customer[3]}  |  {customer[4]}");
        else:
            print(response['data']);
            print("\nAlgo deu errado");
           
           
    if ( inputMenu == 5 ):
        print('\Deletar um produto.');
        try:
            cpf = input('cpf: ');
           
            response = Clientes.delete(cpf);
           
            print(f'\n{response['message']}');
 
        except:
            print('Something went wrong');
           
    if ( inputMenu == 5 ):
        print('\nMenu de atualização do produto.');
        print('Digite 1 para atualizar o nome');
        print('Digite 2 para atualizar o cpf');
        print('Digite 3 para atualizar o email');
        print('Digite 4 para atualizar o telefone');
 
       
       
        try:
            subInputMenu = int(input('Digite: '));
           
            cpf = input('cpf: ');
           
            ClienteByCPF = Clientes.findByCPF(cpf);
           
            if ( ClienteByCPF['status'] == 200 ):
                print(f'{ClienteByCPF['data'][0]} | {ClienteByCPF['data'][1]} | {ClienteByCPF['data'][2]} R$ | {ClienteByCPF['data'][3]} / {ClienteByCPF['data'][4]}');
               
                if ( subInputMenu == 1 ):
                    print('\nAtualizando o nome do cliente.');
                    newName = input('Novo Nome: ');
                   
                    response = Clientes.update('name' , name , newName);
                   
                    print(f'\n{response['message']}');
                   
                if ( subInputMenu == 2 ):
                    print('\nAtualizando o cpf do cliente.');
                    newCPF = float(input('Preço: '));
                   
                    response = Clientes.update(cpf, newCPF);
                   
                    print(f'\n{response['message']}');
           
                if ( subInputMenu == 3 ):
                    print('\nAtualizando o email do cliente.');
                    newEmail = int(input('Email: '));
                   
                    response = Clientes.update('Email' , email , newEmail)
                   
                    print(f'\n{response['message']}');    
               
                if ( subInputMenu == 4 ):
                    print('\nAtualizando o telefone do cliente.');
                    newPhone = int(input('Phone: '));
                   
                    response = Clientes.update('Phone' , phone , newPhone);
                   
                    print(f'\n{response['message']}');  
               
        except:
            print('Something went wrong');    
   
    input('\nAperte ENTER para continuar');
   