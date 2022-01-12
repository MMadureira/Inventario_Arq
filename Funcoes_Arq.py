def chamarMenu():
    escolha = int(input("\nDigite: \n | <1> Para registrar ativo\n"
                " | <2> Para persistir em arquivo\n"
                " | <3> Para exibir ativos armazenados\n"
                " | <0> Para sair\n"
                " > "))
    return escolha

def registrar(dicionario):
    resp = "S"
    while resp == "S":
        dicionario[input("Digite o número patrimonial: ")] = [
            input("\nDigite a data da última atualização: "),
            input("Digite a descrição: "),
            input("Digite o departamento: ")]
        resp = input("\nDigite <S> para continuar ou <R> para retornar as opções. ").upper()

def persistir(dicionario):
    with open("inventario.csv", "a") as inv:
        for chave, valor in dicionario.items():
            inv.write(chave + ";" + valor[0] + ";" + valor[1] + ";" +valor[2]+" \n ")

    return "\nPersistido com sucesso"

def exibir():
    with open("inventario.csv", "r") as inv:
        linhas = inv.readlines()
    return linhas