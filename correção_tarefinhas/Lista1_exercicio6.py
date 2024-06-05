nota_1 = float(0);
nota_2 = float(0);
nota_3 = float(0);
resultado = float(0);

print(f"\nO algoritmo calculará a média obtida através das 3 notas (Considerando  o peso de cada nota). ");

nota_1 = float(input("Digite a 1ª Nota ->"));
nota_2 = float(input("Digite a 2ª Nota ->"));
nota_3 = float(input("Digite a 3ª Nota ->"));

#processamento
resultado = (   (nota_1 * 2) + (nota_2 * 3) + (nota_3 * 5) ) / 10;

#output
print(f"Resultado: {resultado}");             