#Parser de series historicas da bolsa de valores brasileira

from enum import Enum
import os
import time
import multiprocessing as mp

#Variaveis contendo os indices de cada um dos campos da grande string que representa uma entrada de uma acao da bolsa
class Registros(Enum):
    tipo_registo = (0, 2)
    data_pregao = (2, 10)
    cod_BDI = (10, 11)
    cod_negociacao_papel = (12, 13)
    tipo_mercado = (24, 26)
    nome_resumido = (27, 38)
    especificacao_papel = (39, 48)
    prazo_dias = (49, 51)
    moeda_referencia = (52, 55)
    preco_abertura = (56, 68)
    preco_maximo = (69, 81)
    preco_minimo = (82, 94)
    preco_medio = (95, 107)
    preco_ultima_negociacao = (108, 120)
    preco_melhor_oferta_compra = (121, 133)
    preco_melhor_oferta_venda = (134, 146)
    numero_negociacoes_efetuadas = (147, 151)
    quantidade_titulos_negociados = (152, 169)
    volume_total_titulos_negociados = (170, 187)
    preco_mercado_opcoes_ou_termo_secundario = (188, 200)
    indicador_de_correcao = (201, 201)
    data_vencimento_mercado_opcoes = (202, 209)
    fator_cotacao_papel = (210, 216)
    preco_exercicio_pontos_opcoes_dollar = (217, 229)
    codigo_papel = (230, 241)
    numero_distribuicao = (242, 244)

#Function que parseia as linhas de um arquivo contendo dados historicos de uma acao na bolsa
def parse_stock_data(file):
    data = open(file, "r")

    path = os.path.dirname(os.path.abspath(__file__))
    out_dir_name = path + "\\dados_csv_split"
    if not os.path.isdir(path): #Cria uma pasta para os arquivos de saida        
        os.mkdir(out_dir_name)

    extension = os.path.splitext(file)[1]
    output = open(out_dir_name + "\\" + file.replace(extension, ".csv"), 'a')
    data_lines = data.readlines()[1:]
    for line in data_lines:
        index = 0
        for registro in Registros:
            output.write(line[registro.value[0]:registro.value[1]])
            output.write(",") if index != len(Registros)-1 else output.write("\n")
            index += 1

#Function que cria os headers para o arquivo csv de saida
def create_headers(output):
    output.writelines("tipo_registo,data_pregao,cod_BDI,cod_negociacao_papel,tipo_mercado,nome_resumido,especificacao_papel,prazo_dias,moeda_referencia,preco_abertura,preco_maximo,preco_minimo,preco_medio,preco_ultima_negociacao,preco_melhor_oferta_compra,preco_melhor_oferta_venda,numero_negociacoes_efetuadas,quantidade_titulos_negociados,volume_total_titulos_negociados,preco_mercado_opcoes_ou_termo_secundario,indicador_de_correcao,data_vencimento_mercado_opcoes,fator_cotacao_papel,preco_exercicio_pontos_opcoes_dollar,codigo_papel,numero_distribuicao\n")

def main():
    #Captura o nome da pasta em que o arquivo .py esta
    path = os.path.dirname(os.path.abspath(__file__))

    files = []
    #preenche o vetor "files" com o nome dos arquivos txt da pasta
    for r, d, f in os.walk(path):
        for file in f:
            extension = os.path.splitext(file)[1]
            if '.txt' in extension.lower():
                files.append(file)

    pool = mp.Pool()
    pool.map(parse_stock_data, files)

if __name__=="__main__":
    starttime = time.time()
    mp.freeze_support()
    main()
    print('That took {} seconds'.format(time.time() - starttime))