inputText = str("");
count = int(0);

print(f"\nDigite um texto. O código contará quantas vogais foram digitadas");

inputText = input("Digite:");

#processamento

print(f"\n Texto Digitado: {inputText}\n");

#for i in range(0 , len(inputText) , 1):
# print(inputText[i]);

for word in (inputText.lower()):

    if ( word == "a" or
         word == "e" or
         word == "i" or
         word == "o" or
         word == "u"):
        count = count + 1;
        
        
        
#output
print(f"Quantidade de Vogais: {count}");        