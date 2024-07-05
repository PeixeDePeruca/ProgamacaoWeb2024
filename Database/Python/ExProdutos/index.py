import produto;
from os import system;
 
#variavel
inputMenu = int(0);
subInputMenu = int(0);
 
while(True):
    system('cls');
    #Opição menu
   
    print("Digite [0] para sair.");
    print("Digite [1] para CRIAR um produto.");
    print("Digite [2] para SELECIONAR um produto.");
    print("Digite [3] para LISTAR todos os produtos.");
    print("Digite [4] para deletar um produto.");
    print('Digite [5] para Atualizar.');
   
    inputMenu = int(input("Digite: "));
   
    if(inputMenu < 0 or inputMenu > 5):
        print("Digite apenas valores que estão no menu");
   
    if(inputMenu == 0):
        print("Encerrando Sistema");
        break;
   
    if(inputMenu == 1):
        print("Digite os dados solicitados para criar seu produto: ");
        try:
            name = input("Nome: ");
            price = float(input("Preço: "));
            quantity = int(input("Quantidade: "));
       
            response = produto.create(name, price, quantity)
       
            print(f'\n{response['message']}');
        except:
            print('Something went wrong');
       
    if(inputMenu == 2):
        print('\nVamos procurar um produto específico.');
        try:
            name = input('Nome: ');
       
            response = produto.findByName(name);
           
            print(f'\n{response['message']}');
           
            if ( response['status'] == 200 ):
                print(f'\nID / NOME / PREÇO / QUANTIDADE');
                print(f'{response['data'][0]} / {response['data'][1]} / {response['data'][2]} R$ / {response['data'][0]} Un');
       
        except:
            print('Something went wrong')
         
    if ( inputMenu == 3 ):
        print('\nListagem de produtos.');
   
        response = produto.select();
       
        if ( response['status'] == 200 ):
           
            print(f'\nID / NOME / PREÇO / QUANTIDADE');
            for product in response['data']:
                print(f'{product[0]} / {product[1]} / {product[2]} R$ ');
               
        else:
            print(response['data']);
           
    if ( inputMenu == 4 ):
        print('\nDeletar um produto.');
        try:
            name = input('Nome: ');
           
            response = produto.delete(name);
           
            print(f'\n{response['message']}');
 
        except:
            print('Something went wrong');
           
    if ( inputMenu == 5 ):
        print('\nMenu de atualização do produto.');
        print('Digite 1 para atualizar o nome');
        print('Digite 2 para atualizar o preço');
        print('Digite 3 para atualizar a quantidade');
 
        subInputMenu = int(input('Digite: '));
       
        try:
            name = input('Nome: ');
           
            productByName = produto.findByName(name);
           
            if ( productByName['status'] == 200 ):
                print(f'{response['data'][0]} / {response['data'][1]} / {response['data'][2]} R$ / {response['data'][0]} Un');
                   
                if ( subInputMenu == 2 ):
                    print('\nAtualizando o preço do produto.');
                    newPrice = float(input('Preço: '));
                   
                    response = produto.updatePrice(name, newPrice);
                   
                    print(f'\n{response['message']}');
            else:
                print(f'\n{productByName['message']}');        
               
        except:
            print('Something went wrong');    
   
    input('\nAperte ENTER para continuar');