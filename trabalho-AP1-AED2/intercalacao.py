import os

def intercalacao_arquivo(arquivo1, arquivo2, arquivo_saida):             # intercala dois arquivos que já estão ordenados
    with open(arquivo1, "r", encoding = "utf-8") as primeiro:            # abre o primeiro arquivo para leitura
        with open(arquivo2, "r", encoding = "utf-8") as segundo:         # abre o segundo arquivo para leitura
            with open(arquivo_saida, "w", encoding = "utf-8") as saida:  # cria o arquivo que receberá o resultado
                linha1 = primeiro.readline()
                linha2 = segundo.readline()

                while linha1 and linha2:
                    numero1 = int(linha1.srip())
                    numero2 = int(linha2.strip())

                if numero1 <= numero2:
                    saida.write(f"{numero1}\n")
                    linha1 = primeiro.readline()

                else:
                    saida.write(f"{numero2}\n")
                    linha2 = segundo.readline()

                while linha1:
                    saida.write(linha1)
                    linha1 = primeiro.readline()

                while linha2:
                    saida.write(linha2)
                    linha2 = segundo.readline()

def executar_merge_sort(pasta_temporaria, caminho_arquivo_final):        # realiza as rodadas do Merge Sort externo
    arquivos = []

    for nome in os.listdir(pasta_temporaria):                            # percorre os nomes dos arquivos existentes na pasta
        if nome.endswith(".txt"):                                        # verifica se o arquivo possui extensão .txt
            arquivos.append(os.path.join(pasta_temporaria, nome))

    arquivos.sort()
    rodada = 0

    while len(arquivos) > 1:                                             # continua enquanto existir mais de um arquivo para intercalar
        novo_arquivo = []

        for i in range(0, len(arquivos), 2):                             # percorre os arquivos de dois em dois
            arquivo1 = arquivos[i]

            if i + 1 < len(arquivos):                                    # verifica se existe um segundo arquivo para formar um par
                arquivo2 = arquivos[i + 1]
                novo_arquivo = os.path.join(pasta_temporaria, f"merge_{rodada}_{i // 2}.txt")  # cria o caminho do novo arquivo
                intercalacao_arquivo(arquivo1, arquivo2, novo_arquivo)                         # intercala os dois arquivos

                novo_arquivo.append(novo_arquivo)

            else:
                novo_arquivo.append(arquivo1)

        arquivos = novo_arquivo
        rodada += 1

    if len(arquivos) == 1:                                                # verifica se restou somente um arquivo
        os.replace(arquivos[0], caminho_arquivo_final)                    # move o único arquivo restante para o caminho final