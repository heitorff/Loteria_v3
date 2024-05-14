import requests
import time
from collections import Counter, defaultdict
from datetime import datetime
import json
import os
from dateutil import relativedelta
from PySimpleGUI import PySimpleGUI as sg
import random
import itertools


resultados = []
url = 'https://servicebus2.caixa.gov.br/portaldeloterias/api/lotofacil/'
response = requests.get(url)
response.raise_for_status()
dados = response.json()
concurso = dados.get('numero')
x = True
i = 1

def obter_resultados_lotofacil():
    x = True
    i = 1
    resultados = {}
    
    
    while x == True:
        url = f"https://servicebus2.caixa.gov.br/portaldeloterias/api/lotofacil/{i}"
        

        try:
            #for numero in range(1,concurso):
                #anteriores = f'{numero:04}'
            response = requests.get(url)
            response.raise_for_status()
            dados = response.json()
            if 'error' in dados:
                print(f"Erro na API: {dados['error']}")
                return None
            
            
            dezena = f'dezenas{i}' 
            data =  f'data{i}'         
            resultados_parcial = {dezena: dados['listaDezenas'], data: dados['dataApuracao']}
            resultados.update(resultados_parcial)
            

            i+=1
            if i > concurso:
                    resultados_final = {'resultados': []}

                    num_pares = len([chave for chave in resultados.keys() if chave.startswith('dezena')])

                    for i in range(1, num_pares + 1):
                        chave_dezena = f'dezenas{i}'
                        chave_data = f'data{i}'

                        valor_dezena = resultados.get(chave_dezena)
                        valor_data = resultados.get(chave_data)

                        if valor_dezena is not None and valor_data is not None:
                            resultados_final['resultados'].append({'dezenas': valor_dezena, 'data': valor_data})
                   
                    window["status"].update("Atualização Encerrada!")
                    return resultados_final
                    x = False    
        except requests.exceptions.RequestException as e:
            print(f"Erro na requisição: {e}")
            time.sleep(3)
        continue

def gravar_resultados_arquivo(resultados, arquivo):
    with open(arquivo, 'w') as file:
        json.dump(resultados, file)

def ler_resultados_arquivo(arquivo):
    if os.path.exists(arquivo):
        with open(arquivo, 'r') as file:
            return json.load(file)
    else:
        return None
    

#Função para comparar dois numeros de cada linha, entre duas linhas
def contar_pares_duas_linhas(resultados, linha_1, linha_2):
    contar_pares_linhas = Counter()

    nrm_aposta = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10']


    for num1 in linha_1:
        for num2 in linha_1:
            for num3 in linha_2:
                for num4 in linha_2:
                    if num1 < num2 and num3 < num4:
                        for resultado in resultados['resultados']:
                            if num1 in resultado['dezenas'] and num2 in resultado['dezenas'] and num3 in resultado['dezenas'] and num4 in resultado['dezenas'] and all(num not in resultado['dezenas'] for num in nrm_aposta if num != num1 and num != num2 and num != num3 and num != num4):
                                #data_sorteio = datetime.strptime(resultado['data'], "%d/%m/%Y")
                                #mes_ano = f"{data_sorteio.month:02d}/{data_sorteio.year}"


                                #if mes_ano in intervalo_meses:
                                contar_pares_linhas[(num1, num2, num3, num4)] += 1

    return contar_pares_linhas


# Função para gerar 11 números adicionais diferentes dos números iniciais
def gerar_numeros_adicionais(numeros_iniciais):
    numeros_disponiveis = [str(num).zfill(2) for num in range(1, 26) if str(num).zfill(2) not in numeros_iniciais]
    numeros_adicionais = list(itertools.combinations(numeros_disponiveis, 15))
    numeros_lista = list(numeros_adicionais)
    numeros_lista.sort()

    return numeros_lista

# Função para combinar os números iniciais com os números adicionais
def combinar_numeros(numeros_iniciais, numeros_adicionais):
    numeros_completos = ()

    combinacao = list(numeros_adicionais)
    numeros_completos = numeros_iniciais.extend(combinacao)

    return numeros_completos

def contar_acertos_conjunto(resultados, numeros_aposta):
    contagem_total = Counter()

    for resultado in resultados['resultados']:
            if set(numeros_aposta) == set(resultado['dezenas']):
                contagem_total[tuple(numeros_aposta)] += 1

    return contagem_total