

#Procure criar um arquivo chamado DesafioDecisao.py e elaborar o código para resolver a seguinte situação:
#o seu módulo solicitará o nível de acesso de uma pessoa que pode ser: ADM, USR ou GUEST e o gênero dessa pessoa,
#caso o nível seja ADM, ele deverá exibir “Olá administrador” para os homens ou “Olá administradora” para as mulheres.
#Se o nível for USR, deverá exibir “Olá usuário” para os homens ou “Olá usuária” para as mulheres. Se o nível for GUEST, 
#a mensagem deverá ser “Olá visitante”. E se o nível digitado for diferente de ADM, USR ou GUEST deverá exibir a mensagem
#“Olá desconhecido(a)”. Considere apenas os gêneros masculino e feminino e não olhe o código abaixo, até resolver o seu desafio.

print("Você é um 1.Usuário, 2.Visitante ou 3. Administrador? ")

lvl = input("Escolher o número da opção correspondente: ")
gender = input("Qual é o seu gênero? Feminino ou Masculino. ").upper()

if gender == "FEMININO":
    g = "a"
elif gender == "MASCULINO":
    g = "o"
else:
    print("Escolha entre os gêneros apresentados")


if lvl == "2":
    print("Olá convidado!")

elif lvl=="1":
    print("Olá Usiári"+g+"!")

elif lvl == "3":
    print("Olá administrad"+g+"r!")
else:
    print("Escolha invália.")
    print("Escolha entre as opções e digite o número correspondente")
    lvl