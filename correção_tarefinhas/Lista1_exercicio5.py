anos = int(0);
dias = int(0);
meses = float(0);
horas = int(0);

print(f"\nO algoritmo converterá a idade digitada em outras unidades. \n");

anos = int(input("Digite sua idade ->"));

#processamento

dias = anos * 365;
meses = dias / 30;
horas = dias * 24;

print(f"Resultados:\n Anos: {anos}\n Meses: {int(meses)}\n Dias: {dias}\n Horas: {horas}");