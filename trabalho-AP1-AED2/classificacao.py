import os  # trabalha com pastas e caminhos dos arquivos

def tem_tres_digitos(numero):                               # verifica se o número possui 3 dígitos
    if numero >= 100 and numero <= 999:                        # verifica se o número está entre 100 e 999
        return True                                            # informa que o número possui 3 dígitos

    return False                                               # informa que o número não possui 3 dígitos


def tem_dois_ou_mais_zeros(numero):                            # verifica se o número possui dois ou mais zeros
    numero_texto = str(numero)                                 # transforma o número em texto
    quantidade_zeros = 0                                       # começa a contagem dos zeros
    posicao = 0                                                # começa na primeira posição do número

    while posicao < len(numero_texto):                         # percorre todos os caracteres do número
        if numero_texto[posicao] == "0":                       # verifica se o caractere atual é zero
            quantidade_zeros = quantidade_zeros + 1            # aumenta a quantidade de zeros

        posicao = posicao + 1                                  # passa para o próximo caractere

    if quantidade_zeros >= 2:                                  # verifica se existem pelo menos dois zeros
        return True                                            # informa que possui dois ou mais zeros

    return False                                               # informa que possui menos de dois zeros


def classificar_arquivo(caminho_entrada, pasta_classificados):                                 # separa os números de acordo com as regras do fluxograma
    os.makedirs(pasta_classificados, exist_ok=True)                                            # cria a pasta caso ela ainda não exista

    caminho_tres_digitos = os.path.join(pasta_classificados, "numeros_com_3_digitos.txt")      # cria o caminho do arquivo dos números de 3 dígitos
    caminho_dois_zeros = os.path.join(pasta_classificados, "numeros_com_2_ou_mais_zeros.txt")  # cria o caminho do arquivo dos números com dois ou mais zeros
    caminho_restantes = os.path.join(pasta_classificados, "numeros_restantes.txt")             # cria o caminho do arquivo dos números restantes

    arquivo_entrada = open(caminho_entrada, "r", encoding = "utf-8")                           # abre o arquivo de entrada para leitura
    arquivo_tres_digitos = open(caminho_tres_digitos, "w", encoding = "utf-8")                 # cria o arquivo dos números de 3 dígitos
    arquivo_dois_zeros = open(caminho_dois_zeros, "w", encoding = "utf-8")                     # cria o arquivo dos números com dois ou mais zeros
    arquivo_restantes = open(caminho_restantes, "w", encoding = "utf-8")                       # cria o arquivo dos números restantes

    quantidade_tres_digitos = 0                                                  # começa a contagem dos números de 3 dígitos
    quantidade_dois_zeros = 0                                                    # começa a contagem dos números com dois ou mais zeros
    quantidade_restantes = 0                                                     # começa a contagem dos números restantes

    for linha in arquivo_entrada:                                                # percorre cada linha do arquivo de entrada
        texto = linha.strip()                                                    # remove espaços e a quebra de linha

        if texto != "":                                                          # verifica se a linha possui algum valor
            numero = int(texto)                                                  # transforma o texto em número inteiro

            if tem_tres_digitos(numero):                                         # primeiro verifica se possui exatamente 3 dígitos
                arquivo_tres_digitos.write(str(numero) + "\n")                   # grava o número no arquivo de 3 dígitos
                quantidade_tres_digitos = quantidade_tres_digitos + 1            # aumenta a quantidade de 3 dígitos

            elif tem_dois_ou_mais_zeros(numero):                                 # verifica se possui dois ou mais zeros
                arquivo_dois_zeros.write(str(numero) + "\n")                     # grava o número no arquivo de dois ou mais zeros
                quantidade_dois_zeros = quantidade_dois_zeros + 1                # aumenta a quantidade de números com zeros

            else:                                                                # executa quando não pertence às duas primeiras categorias
                arquivo_restantes.write(str(numero) + "\n")                      # grava o número no arquivo dos restantes
                quantidade_restantes = quantidade_restantes + 1                  # aumenta a quantidade de números restantes

    arquivo_entrada.close()                                                      # fecha o arquivo de entrada
    arquivo_tres_digitos.close()                                                 # fecha o arquivo de 3 dígitos
    arquivo_dois_zeros.close()                                                   # fecha o arquivo de dois ou mais zeros
    arquivo_restantes.close()                                                    # fecha o arquivo dos restantes

    caminhos = [caminho_tres_digitos, caminho_dois_zeros, caminho_restantes]     # guarda os caminhos dos três arquivos criados

    quantidades = {"tres_digitos": quantidade_tres_digitos, "muitos_zeros": quantidade_dois_zeros, "restantes": quantidade_restantes}  # guarda a quantidade de números de cada categoria

    return caminhos, quantidades                                                                                                       # devolve os caminhos e as quantidades