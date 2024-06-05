A = int(0);
B = int(0);
C = int(0);
 
print(f'Os valores digitados serão exibidos em ordem decrescente\n');
 
variavel_1 = int(input('Digite: '));
variavel_2 = int(input('Digite: '));
variavel_3 = int(input('Digite: '));
 
# Processamento / Output
 
# Variavel 1 é a maior
if (A > B and A > C):
    print(f'{A}');
   
    if (B >= C):
        print(B);
        print(C);
    else:
        print(C);
        print(B);
       
 
#Variavel 2 é a maior
if(B > A and B > C):
    print(f'{B}');
   
    if(A >= C):
        print(A);
        print(B);
    else:
        print(A);
        print(B);
   
#Variavel 3 é a maior
if (C > A and C > B):
    print(f'{C}')
   
    if(A >= B):
        print(A);
        print(B);
    else:
        print(B);
        print(A);
       
if (A == B and A == C):
    print(A);
    print(B);
    print(C);