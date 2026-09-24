import random      # medir o tempo de execução
import time        # gerar números aleatórios

def gerar_arquivo_aleatorio(quantidade_total, maior_valor, caminho_arquivo_desordenado): # gera números aleatórios e grava no arquivo
    inicio = time.perf_counter()                                                         # registra o tempo inicial da execução

    with open(caminho_arquivo_desordenado, "w", encoding = "utf-8") as arquivo:          # abre o arquivo para a escrita
        for _ in range(quantidade_total):                                                # repete o processo até atingir a quantidade necessária
            numero = random.randint(0, maior_valor)                                      # sorteia um número inteiro entre 0 e o maior número
            arquivo.write(f"{numero}\n")                                                 # grava o número no arquivo e vai pra próxima linha

    tempo_geracao = time.perf_counter() - inicio                                         # calcula o tempo de geração

    print(f"Arquivo gerado com sucesso: {caminho_arquivo_desordenado}")
    print(f"Quantidade de valores gravados: {quantidade_total}")
    print(f"Tempo de geração: {tempo_geracao: .2f} segundos")

def verificar_desordenado(caminho_arquivo_desordenado):                                  # verifica se os números estão desordenados
    with open(caminho_arquivo_desordenado, "r", encoding = "utf-8") as arquivo:          # abre o arquivo para a leitura
        valores = [int(linha.strip()) for linha in arquivo]                              # lê cada linha, remove a quebra e transforma em inteiro

    if len(valores) < 2:                                                                 # verifica se existe pelo menos dois números para comparar
        return False                                                                     

    for i in range(len(valores) - 1):                                                    # percorre os valores até o penúltimo
        if valores[i] > valores[i + 1]:                                                  # verifica se o número é maior que o próximo
            return True                                                                  

    return False
