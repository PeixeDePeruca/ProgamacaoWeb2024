from datetime import datetime;
 
inputYear = int(0);
inputMonth = int(0);
inputDay = int(0);
resultado = [];
 
 
Day = int(input('Digite o dia que você nasceu: '));
Month = int(input('Digite o mês que você nasceu: '));
Year = int(input('Digite o Ano que você nasceu: '));
 
def conversaoIdade(Year, Month, Day):
   
    resYear = int(0);
    resMonth = int(0);
    resDay = int(0);
   
    varr = datetime.now();
   
    resDay = varr.day - Day;
    resMonth = varr.month - Month;
    resYear = varr.year - Year;
   
    if(resDay < 0):
        resDay = 30 - (resDay * -1);
        resMonth = resMonth - 1;
 
    if (resMonth < 0):  
        resMonth = 12 - (resMonth * -1);
        resYear = resYear - 1;
       
   
    return[resDay , resMonth, resYear];
 
 
resultado = conversaoIdade(Year, Month, Day);
print(resultado)