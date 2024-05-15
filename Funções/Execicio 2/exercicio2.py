print('\nEsse algoritmo calcula o tempo QUASE exato que você está vivo \n');
    
    
from datetime import datetime;
 
inputYear = int(0);
inputMonth = int(0);
inputDay = int(0);
resYear = int(0);
resMonth = int(0);
resDay = int(0);
 
#Entrada de dados
inputDay = int(input('Dia: '));
inputMonth = int(input('Mês: '));
inputYear = int(input('Ano: '));
 
 
#Processamento
varr = datetime.now();
 
resDay = varr.day - inputDay;
resMonth = varr.month - inputMonth;
resYear = varr.year - inputYear;
 
if(resDay < 0):
    resDay = 30 - (resDay * -1);
    resMonth = resMonth - 1;
 
if (resMonth < 0):
    resMonth = 12 - (resMonth * -1);
    resYear = resYear - 1;
 
 
print(f'Você tem: {resYear} Anos , {resMonth} Meses e {resDay} Dias de vida');
 
