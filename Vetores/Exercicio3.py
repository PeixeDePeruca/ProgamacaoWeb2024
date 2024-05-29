
filmes_TV = [ "Corações de Ferro" , "Trêm Bala" , "Bastardos Inglórios" , "Django Livre" , "Onde os Fracos Não Têm Vez" , "Jojo Rabbit"];
pesquisa = str('');
verify = bool(False);


print(f"\nLista de filmes disponíveis na PeixeTV essa semana.");
print(f"\nDigite o nome de um filme para verificar se estará disponível.");

pesquisa = input("Pesquise o filme que deseja assistir ->") 



for i in range ( 0 , len(filmes_TV) , 1):
    if ( pesquisa == filmes_TV[i] ):
        verify = True;
        break;
    else:
        verify = False;
        
if (verify == True ):
    print("Filme Encontrado, Clique no link abaixo para assistir :D");
else:
    print("Filme NÃO Encontrado, procure por outro filme :(");