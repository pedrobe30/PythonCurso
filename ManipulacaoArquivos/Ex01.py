def Create():
 while True:
  fruta = input("Adicione uma fruta")
  with open("C:/Users/Aluno_Programador3/3D Objects/ArquivosCriados/frutas.txt", "a") as arquivo:
   arquivo.write(f"Frutas Adicionadas: {fruta}")
   break


def read():
 with open("C:/Users/Aluno_Programador3/3D Objects/ArquivosCriados/frutas.txt", "r") as arquivo:
  print(arquivo.read())
 


def Add():
 with open("C:/Users/Aluno_Programador3/3D Objects/ArquivosCriados/frutas.txt", "a") as arquivo:
  arquivo.write("Uva")
  arquivo.write("Abacaxi")

     