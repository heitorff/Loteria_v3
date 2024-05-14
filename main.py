from collections import Counter, defaultdict 
from datetime import datetime
from PySimpleGUI import PySimpleGUI as sg
import functions as functions
import re

if __name__ == '__main__':

    sg.theme('Reddit')

    numeros_par = ['11', '12', '13', '14', '15']

    arquivo_resultados = 'resultados_lotofacil.json'

    resultados_lotofacil = functions.ler_resultados_arquivo(arquivo_resultados)

    if not resultados_lotofacil:
        resultados_lotofacil = functions.obter_resultados_lotofacil()
        functions.gravar_resultados_arquivo(resultados_lotofacil, arquivo_resultados)

    #resultados_lotofacil = obter_resultados_lotofacil()

    if resultados_lotofacil:

        numero_qtd = []
        semestre = []
        par  = []


        layout = [
            [sg.Button('Sair'), sg.Button('Atualizar'), sg.Button('Selecionados'), sg.Text('Status Atualização!', key='status')],
            [sg.Checkbox("'01', '02', '03', '04', '05'", "linha_1", key='linha_1')],
            [sg.Checkbox("'06', '07', '08', '09', '10'", "linha_2", key='linha_2')],
            [sg.Checkbox("'11', '12', '13', '14', '16'", "linha_3", key='linha_3')],
            [sg.Checkbox("'16', '17', '18', '19', '20'", "linha_4", key='linha_4')],
            [sg.Checkbox("'21', '22', '22', '24', '25'", "linha_5", key='linha_5')],
            [sg.Listbox(key='pares_linhas', values = par, s=(60, 5), select_mode=sg.LISTBOX_SELECT_MODE_SINGLE), sg.Listbox(key='conjunto_total', values = par, s=(60, 5))],
            [sg.Button('Resultados')]
        ]

        window = sg.Window('Lotofácil Analyzer', layout, resizable=True)    

        while True:
            event, values = window.read()

            if event == sg.WINDOW_CLOSED or event == 'Sair':
                break
            elif event == 'Resultados':

                pares_linhas = []
                conjunto_total = []

                if values['linha_1'] == True and values['linha_2'] == True:

                    linha_1 = ['01', '02', '03', '04', '05']
                    linha_2 = ['06', '07', '08', '09', '10']

                    contagem_pares_linhas = functions.contar_pares_duas_linhas(resultados_lotofacil, linha_1, linha_2)

                    for par, total in contagem_pares_linhas.items():
                        pares_linhas.append(f"Par {par[0]}-{par[1]}-{par[2]}-{par[3]}: {total} vezes")
                window['pares_linhas'].update(values=pares_linhas)


                if values['linha_1'] == True and values['linha_3'] == True:
                    
                    linha_1 = ['01', '02', '03', '04', '05']
                    linha_2 = ['11', '12', '13', '14', '15']

                    contagem_pares_linhas = functions.contar_pares_duas_linhas(resultados_lotofacil, linha_1, linha_2, intervalo_meses)

                    for par, total in contagem_pares_linhas.items():
                        pares_linhas.append(f"Par {par[0]}-{par[1]}-{par[2]}-{par[3]}: {total} vezes (Semestre/Ano: {par[4]})")
                window['pares_linhas'].update(values=pares_linhas)


                if values['linha_1'] == True and values['linha_4'] == True:
                    
                    linha_1 = ['01', '02', '03', '04', '05']
                    linha_2 = ['16', '17', '18', '19', '20']

                    contagem_pares_linhas = functions.contar_pares_duas_linhas(resultados_lotofacil, linha_1, linha_2, intervalo_meses)

                    for par, total in contagem_pares_linhas.items():
                        pares_linhas.append(f"Par {par[0]}-{par[1]}-{par[2]}-{par[3]}: {total} vezes (Semestre/Ano: {par[4]})")
                window['pares_linhas'].update(values=pares_linhas)


                if values['linha_1'] == True and values['linha_5'] == True:
                    
                    linha_1 = ['01', '02', '03', '04', '05']
                    linha_2 = ['21', '22', '23', '24', '25']

                    contagem_pares_linhas = functions.contar_pares_duas_linhas(resultados_lotofacil, linha_1, linha_2, intervalo_meses)

                    for par, total in contagem_pares_linhas.items():
                        pares_linhas.append(f"Par {par[0]}-{par[1]}-{par[2]}-{par[3]}: {total} vezes (Semestre/Ano: {par[4]})")
                    window['pares_linhas'].update(values=pares_linhas)

                if values['linha_2'] == True and values['linha_3'] == True:
                    
                    linha_1 = ['06', '07', '08', '09', '10']
                    linha_2 = ['11', '12', '13', '14', '15']

                    contagem_pares_linhas = functions.contar_pares_duas_linhas(resultados_lotofacil, linha_1, linha_2, intervalo_meses)

                    for par, total in contagem_pares_linhas.items():
                        pares_linhas.append(f"Par {par[0]}-{par[1]}-{par[2]}-{par[3]}: {total} vezes (Semestre/Ano: {par[4]})")
                window['pares_linhas'].update(values=pares_linhas)


                if values['linha_2'] == True and values['linha_4'] == True:
                    
                    linha_1 = ['06', '07', '08', '09', '10']
                    linha_2 = ['16', '17', '18', '19', '20']

                    contagem_pares_linhas = functions.contar_pares_duas_linhas(resultados_lotofacil, linha_1, linha_2, intervalo_meses)

                    for par, total in contagem_pares_linhas.items():
                        pares_linhas.append(f"Par {par[0]}-{par[1]}-{par[2]}-{par[3]}: {total} vezes (Semestre/Ano: {par[4]})")
                window['pares_linhas'].update(values=pares_linhas)


                if values['linha_2'] == True and values['linha_5'] == True:
                    
                    linha_1 = ['06', '07', '08', '09', '10']
                    linha_2 = ['21', '22', '23', '24', '24']

                    contagem_pares_linhas = functions.contar_pares_duas_linhas(resultados_lotofacil, linha_1, linha_2, intervalo_meses)

                    for par, total in contagem_pares_linhas.items():
                        pares_linhas.append(f"Par {par[0]}-{par[1]}-{par[2]}-{par[3]}: {total} vezes (Semestre/Ano: {par[4]})")
                window['pares_linhas'].update(values=pares_linhas)


                if values['linha_3'] == True and values['linha_4'] == True:
                    
                    linha_1 = ['11', '12', '13', '14', '15']
                    linha_2 = ['16', '17', '18', '19', '20']

                    contagem_pares_linhas = functions.contar_pares_duas_linhas(resultados_lotofacil, linha_1, linha_2, intervalo_meses)

                    for par, total in contagem_pares_linhas.items():
                        pares_linhas.append(f"Par {par[0]}-{par[1]}-{par[2]}-{par[3]}: {total} vezes (Semestre/Ano: {par[4]})")
                window['pares_linhas'].update(values=pares_linhas)


                if values['linha_3'] == True and values['linha_5'] == True:
                    
                    linha_1 = ['11', '12', '13', '14', '15']
                    linha_2 = ['21', '22', '23', '24', '25']

                    contagem_pares_linhas = functions.contar_pares_duas_linhas(resultados_lotofacil, linha_1, linha_2, intervalo_meses)

                    for par, total in contagem_pares_linhas.items():
                        pares_linhas.append(f"Par {par[0]}-{par[1]}-{par[2]}-{par[3]}: {total} vezes (Semestre/Ano: {par[4]})")
                window['pares_linhas'].update(values=pares_linhas)


                if values['linha_4'] == True and values['linha_5'] == True:
                    
                    linha_1 = ['16', '17', '18', '19', '20']
                    linha_2 = ['21', '22', '23', '24', '25']

                    contagem_pares_linhas = functions.contar_pares_duas_linhas(resultados_lotofacil, linha_1, linha_2, intervalo_meses)

                    for par, total in contagem_pares_linhas.items():
                        pares_linhas.append(f"Par {par[0]}-{par[1]}-{par[2]}-{par[3]}: {total} vezes (Semestre/Ano: {par[4]})")
                window['pares_linhas'].update(values=pares_linhas)


            elif event == 'Selecionados':
                selected_indexes = window['pares_linhas'].get_indexes()
                all_items = window['pares_linhas'].get_list_values()
                selected_items = [all_items[index] for index in selected_indexes]

                padrao_numeros = re.compile(r'(\d{2})-(\d{2})-(\d{2})-(\d{2})')

                numeros_lista = []

                for dado in selected_items:
                    match = padrao_numeros.search(dado)
                    if match:
                        numeros = [match.group(i) for i in range(1, 5)] 
                        numeros_lista.extend(numeros) 

                
                numeros_adicionais = functions.gerar_numeros_adicionais(numeros_lista)

                numeros_lista.extend(numeros_adicionais)


                window['conjunto_total'].update(values=numeros_lista)

                contagem_total  = functions.contar_acertos_conjunto(resultados_lotofacil, numeros_lista)

                for par, total in contagem_total.items():
                    conjunto_total.append(f"Par {par}: {total} vezes")
            