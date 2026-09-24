def bubble_sort(bloco):                                            # função responsável por ordenar um bloco
    for i in range(len(bloco)):                                    # repete as passagens pelo bloco
        for j in range(0, len(bloco) - i - 1):                     # percorre valores que ainda precisam ser comparados
            if bloco[j] > bloco[j + 1]:                            # verifica se o valor atual é maior que o próximo
                bloco[j], bloco[j + 1] = bloco[j + 1], bloco[j]    # troca os valores de posição

    return bloco

def criar_blocos(valores, limite_memoria):                         # divide os valores em blocos respeitando o limite de memória
    blocos = []

    for i in range(0, len(valores), limite_memoria):               # percorre os valores e pula de acordo com o limite
        bloco = valores[i:i + limite_memoria]                      # seleciona a quantidade permitida
        bloco = bubble_sort(bloco)                                 # ordena usando Bubble Sort

        blocos.append(bloco)

    return blocos

def salvar_bloco(bloco, caminho_bloco):                            # salva um bloco ordenado em um arquivo
    with open(caminho_bloco, "w", encoding = "utf-8") as arquivo:  
        for numero in bloco:
            arquivo.write(f"{numero}\n")