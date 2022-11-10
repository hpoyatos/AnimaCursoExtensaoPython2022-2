#criação de funções

preco = 1999.90

#Calcular apenas 5% de imposto, guardar na variavel imposto e exibir na tela
imposto = preco * 0.05
print(imposto)

preco2 = 100
imposto2 = preco2 * 0.05
print(imposto2)

#Criar uma função calcular_imposto() que calcular um imposto de 5% e retorna a quem pediu...
#Isso é a declaração da função (Como ela funciona)
def calcular_imposto(preco_produto):
  imposto = preco_produto * 0.07
  return imposto

#Aqui é o uso... aqui é imposto a calcular.. e exibir na tela
preco = 299
imposto = calcular_imposto(preco)
print(f"Esse aqui é com a função (7%): {imposto}")

#Explicação de variável local x global
print(preco) #????
preco_produto = 100
print(preco_produto) #????


#agora calcular imposto a alíquota agora é 7%

valores = [1.99, 24.50, 78.27, 1515.5]
# se eu quiser calcular o imposto destes quatro valores... e exibir na tela assim: "O imposto de .... é ...." (1o. preço, 2o. imposto)
for valor in valores:
  print(f"O imposto de {valor} é {calcular_imposto(valor)}")
