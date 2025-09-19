num = int(input("Digite um número: "))

#resolver

if (num % 2 == 0) > 0 or num == 0: #Nessa linha de código eu quero pegar o resto da divisão por 2, e utilizei o metódo de comparação para dizer que esse resto tem que ser 0: (2 == 0), indico também para ele ser maior que 0: (0 > 0), dessa forma ele descarta resultados negativos e só pega números positivos e me devolve o resto da divisões com resultados pares.
    print ("Seu número e Par")
elif num % 2 == 1 > 1: #Nessa linha de código eu quero pegar o resto da divisão por 2, e utilizei o metódo de comparação para dizer que esse resto tem que ser 1: (2 == 1), indico também para ele ser maior que 1: (0 > 0), dessa forma ele descarta resultados negativos e só pega números positivos e me devolve o resto da divisões com resultados ímpares.
    print ("Seu número e Impar")
else: #Nessa linha se o usuário entrar com números negativos, ele já indica isso.
    print ("Seu número e negativo")



 #Resolução Rever
if num < 0:
 print ("Negativo")
elif (num % 2 == 0) > 0 or num == 0:
   print ("Par")
else:
   print ("Impar")