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
    with open(caminho_arquivo_desordenado, "r", encoding = "utf-8") as arquivo:
        valores = arquivo.readlines()                                                           # readlines lê todas as linhas do arquivo e armazena na lista de 'valores'

    for i in range(0, len(valores), limite_memoria):                                            # O range recebe: posição inicial, quantidade total de valores e a quantidade de posisções
        bloco = valores[i:i + limite_memoria]                                                   # i indica onde o bloco começa, a soma com o limite_memoria indica onde o bloco termina
        
        bloco = [int(numero.strip()) for numero in bloco]                                       # transforma cada valor de texto em número inteiro
        bloco = ordenacao_blocos.bubble_sort(bloco)                                             # ordena o bloco usando o Bubble Sort

        os.makedirs(pasta_temporaria, exist_ok = True)                                          # cria uma pasta temporária (se ela não existir ainda)
        caminho_bloco = os.path.join(pasta_temporaria, f"bloco_{i // limite_memoria}.txt")      # cria o caminho e o nome do arquivo do bloco

        with open(caminho_bloco, "w", encoding = "utf-8") as arquivo_bloco:
            for numero in bloco:                                                                # percorre cada número dentro do bloco
                arquivo_bloco.write(f"{numero}\n")                                              # grava cada número em uma linha

if __name__ == "__main__":                                                                      # verifica se o arquivo está sendo executado
    main()                                                                                      # chamada da função 'main'100