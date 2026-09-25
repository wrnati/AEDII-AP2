import os                    # trabalhar com as pastas
import time                  # medir o tempo de execução
import random                # gerar números aleatórios
import validacao             # importa funções do arquivo 'validacao.py'
import intercalacao          # importa funções do arquivo 'intercalacao.py'
import gerador_dados         # importa funções do arquivo 'gerador_dados.py'
import classificacao         # importa funções do arquivo 'classificacao.py'
import ordenacao_blocos      # importa funções do arquivo 'ordenacao_blocos.py'


def main(): # recebe as informações iniciais
    quantidade_inicial = int(input("Digite a quantidade inicial de valores: "))
    maior_valor = int(input("Digite o maior valor que poderá ser sorteado: "))
    limite_memoria = int(input("Digite o limite de memória: "))

    caminho_arquivo_desordenado = "entrada_desordenada.txt"
    pasta_categoria  = "categoria"
    pasta_temporaria = "temporarios"
    caminho_arquivo_final = "saida_ordenada.txt"

    gerar_arquivo_aleatorio(quantidade_inicial, maior_valor, caminho_arquivo_desordenado)
    classificacao.classificar_arquivo(caminho_arquivo_desordenado, pasta_categoria)
    classificar_arquivo(caminho_arquivo_desordenado, limite_memoria, pasta_temporaria, caminho_arquivo_final)


def gerar_arquivo_aleatorio(quantidade_total, maior_valor, caminho_arquivo_desordenado): # gera os números ale1atórios e grava no arquivo
    inicio = time.perf_counter()                                       # registra o tempo inicial da execução do código

    caminho_confirmado = caminho_arquivo_desordenado
    quantidade_gravada = quantidade_total

    numeros_sorteados = set()                                                          # cria um conjunto vazio para guardar os números que já foram sorteados

    if quantidade_total > maior_valor + 1:                                             # verifica se existem números suficientes para não haver repetição
        print("Erro: não é possível gerar essa quantidade de números sem repetição.")  # informa o problema
        return  # encerra a função

    with open(caminho_confirmado, "w", encoding = "utf-8") as arquivo:                 # abre o arquivo para escrita
        while len(numeros_sorteados) < quantidade_total:                               # continua até atingir a quantidade solicitada

            numero = random.randint(0, maior_valor)                                    # sorteia um número aleatório

            if numero not in numeros_sorteados:                                        # verifica se o número ainda não foi sorteado
                numeros_sorteados.add(numero)                                          # adiciona o número ao conjunto de números sorteados
                arquivo.write(f"{numero}\n")                                           # grava o número no arquivo

    tempo_geracao = time.perf_counter() - inicio                                       # calcula o tempo total da geração

    print(f"Arquivo gerado com sucesso: {caminho_confirmado}")                         # informa que o arquivo foi criado
    print(f"Quantidade de valores gravados: {quantidade_gravada}")                     # mostra a quantidade de valores
    print(f"Tempo de geração: {tempo_geracao:.2f} segundos")                           # mostra o tempo de geração


def classificar_arquivo(caminho_arquivo_desordenado, limite_memoria, pasta_temporaria, caminho_arquivo_final): # separa os valores em blocos
    os.makedirs(pasta_temporaria, exist_ok=True)                                                           # cria a pasta dos arquivos temporários caso ela não exista

    bloco = []                                                                                             # cria uma lista vazia para armazenar os números do bloco atual
    numero_bloco = 0                                                                                       # começa a numeração dos blocos

    with open(caminho_arquivo_desordenado, "r", encoding="utf-8") as arquivo:                              # abre o arquivo para leitura
        for linha in arquivo:                                                                              # lê uma linha por vez
            numero = int(linha.strip())                                                                    # remove a quebra de linha e deixa o valor inteiro
            bloco.append(numero)                                                                           # adiciona o número ao bloco atual

            if len(bloco) == limite_memoria:                                                               # verifica se o bloco atingiu o limite de memória
                bloco = ordenacao_blocos.bubble_sort(bloco)                                                # ordena os números do bloco
                caminho_bloco = os.path.join(pasta_temporaria, f"bloco_{numero_bloco}.txt")

                with open(caminho_bloco, "w", encoding="utf-8") as arquivo_bloco:
                    for numero in bloco:                                                                   # percorre os números ordenados do bloco
                        arquivo_bloco.write(f"{numero}\n")                                                 # grava cada número em uma linha

                bloco = []                                                                                 # limpa a memória do bloco para reutilizá-la no próximo bloco
                numero_bloco += 1                                                                          # passa para o número do próximo bloco

        if bloco:                                                                                          # verifica se sobraram números para formar um último bloco
            bloco = ordenacao_blocos.bubble_sort(bloco)                                                    # ordena o último bloco
            caminho_bloco = os.path.join(pasta_temporaria, f"bloco_{numero_bloco}.txt")

            with open(caminho_bloco, "w", encoding="utf-8") as arquivo_bloco:                              # cria o arquivo do último bloco
                for numero in bloco:                                                                       # percorre os números restantes
                    arquivo_bloco.write(f"{numero}\n")                                                     # grava cada número em uma linha

if __name__ == "__main__":                                                                      # verifica se o arquivo está sendo executado
    main()                                                                                      # chamada da função 'main'
