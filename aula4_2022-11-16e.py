import aula4_2022_11_16c as bd

con, cur = bd.conectar()

nome = input("Informe o nome do herói/vilão: ")
nome_civil = input("Informe o nome civil do herói/vilão (sua identidade secreta): ")
tipo_numerico = input("Tecle 1 para Herói(na) ou 2 para Vilã(o): ")

#Consulta aqui a tabela grupos e exibe na tela, pedindo para o usuário digitar o grupo_id


#Consulta para o valor máximo usado no banco
sql = "SELECT MAX(pessoa_id)+1 FROM pessoas"
cur.execute(sql)
pessoa_id = cur.fetchone()[0]

if tipo_numerico == "1":
  tipo = "Herói(na)"
else:
  tipo = "Vilã(o)"

sql = f"INSERT INTO pessoas (pessoa_id, nome, nome_civil, tipo) VALUES ({pessoa_id}, '{nome}', '{nome_civil}', '{tipo}')"

cur.execute(sql)

#Insert pessoas_grupos
#INSERT INTO pessoas_grupos (pessoa_id, grupo_id) VALUES (X, X)

con.commit()
con.close()