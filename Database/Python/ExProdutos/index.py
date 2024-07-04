import produto;
from os import system;
 
#variavel
inputMenu = int(0);
 
while(True):
    system('cls');
    #Opição menu
   
    print("Digite [0] para sair.");
    print("Digite [1] para CRIAR um produto.");
    print("Digite [2] para SELECIONAR um produto.");
    print("Digite [3] para LISTAR todos os produtos.");
    print("Digite [4] para deletar um produto.");
   
    inputMenu = int(input("Digite: "));
   
    if(inputMenu < 0 or inputMenu > 3):
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
                print(response['data']);
        
        except:
            print('Something went wrong')
          
    if ( inputMenu == 3 ):
        print('\nListagem de produtos.');
   
        response = produto.select();
        
        if ( response['status'] == 200 ):
            
            print(f'\nID / NOME / PREÇO / QUANTIDADE');
            for product in response['data']:
                print(product);
                
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
 
    input('\nAperte ENTER para continuar');