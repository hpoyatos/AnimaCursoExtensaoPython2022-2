#Pede o nome do aluno e sua nota (de 0 a 10) e, se ele tirou nota 10, mostra "{nome}, você é bichão, mesmo..."
nome = input("Informe seu nome: ")
nota = float(input("Digite sua nota: "))

if (nota == 10):
  print(f"{nome}, você é bichão, mesmo...")
elif (nota >= 6 and nota < 10):
  print(f"{nome}, bom trabalho")
else: # é sempre automaticamente o que as duas condições não tratamento
  print("Burro, não tirou dez...")


