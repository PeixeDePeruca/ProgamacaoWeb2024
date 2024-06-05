#o algoritmo inverte o resultado dos numeros de lugar e....achoq é isso? 



num1 = int(input("\nDigite o PRIMEIRO número inteiro: "))
num2 = int(input("Digite o SEGUNDO número inteiro: "))


print(f"\nOs valores antes da inversão são: Num1 = {num1}, Num2 = {num2}")


temp = num1
num1 = num2
num2 = temp

print(f"Os valores após a inversão são: Num1 = {num1}, Num2 = {num2}")