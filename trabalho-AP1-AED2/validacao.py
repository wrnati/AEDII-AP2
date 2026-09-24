def ler_numeros(caminho_arquivo):                                  # lê todos os números de um arquivo
    numeros = []

    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            numero = int(linha.strip())
            numeros.append(numero)

    return numeros

def ver_ordem_crescente(numeros):                                  # verifica se os números estão em ordem crescente
    for i in range(len(numeros) - 1):
        if numeros[i] > numeros[i + 1]:
            return False

    return True

def validar_resultado(caminho_entrada, caminho_saida):             # verifica se o resultado final está correto
    numeros_entrada = ler_numeros(caminho_entrada)
    numeros_saida = ler_numeros(caminho_saida)

    mesma_quant = len(numeros_entrada) == len(numeros_saida)
    ordem_correta = ver_ordem_crescente(numeros_saida)
    entrada_ordenada = sorted(numeros_entrada)
    numeros_guardados = entrada_ordenada == numeros_saida

    if mesma_quant and ordem_correta and numeros_guardados:
        return True

    return False