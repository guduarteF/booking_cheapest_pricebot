import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from tkinter import *


# formato calend geral
# 01 out 2023   -> DD mes AAAA

# PESO
"""
ECONOMICS 180
PARAISO 180
YOUNG 185
SLIM 195
EXCLUSIVE 205
CONFORT 230
FAMILY 243
DUNAS 250
OCEAN 250
FORT 280
"""


servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
dia_de_entrada = 1
dia_de_saida = 31
umavez = False
ano = 2023
mes_num = 11
posicao = 5  # int(input('Em qual posição da lista você deseja estar ?'))  # PEDIR A POSIÇÃO SÓ QUANDO GERAL OS PREÇOS ?
# def selecionar_mes():


def logar_no_site():
    # Request da conexão
    navegador.get("https://tnp.stays.com.br/i/home")
    sleep(1)
    # Prenchimento de login
    try:
        (navegador.find_element('xpath', '//*[@id="login-form"]/form/div[1]/input').
         send_keys("carloseduardoferre@gmail.com"))
        navegador.find_element('xpath', '//*[@id="login-form"]/form/div[2]/div/input').send_keys("*********@")
        navegador.find_element('xpath', '//*[@id="login-form"]/form/div[3]/div/button').click()
    except Exception as erro:
        print(f'O erro foi {erro.__class__}')
    sleep(3)


def calendariogeral():
    # Seleciona o menu de opções
    navegador.find_element('xpath', '//*[@id="leftmenu"]/div[1]/ul/li/a/i').click()
    sleep(3)
    # Calendário Geral
    try:
        navegador.find_element('xpath', '//*[@id="leftmenu-scroll"]/div[2]/ul/div[3]/li[4]/a/span').click()
    except Exception as erro:
        print(f'Problema encontrado foi {erro.__class__}')

    sleep(3)


def entrada_das_datas():
    sleep(3)
    # Data de entrada
    navegador.find_element('xpath', '//*[@id="filterform"]/div[1]/div[1]/div/input[1]').clear()
    sleep(3)
    navegador.find_element('xpath', '//*[@id="filterform"]/div[1]/div[1]/div/input[1]')\
        .send_keys(f"{dia_de_entrada} {mes_abrev} {ano}")

    sleep(3)
    # Data de saída
    navegador.find_element('xpath', '//*[@id="filterform"]/div[1]/div[2]/div/input[1]').clear()
    sleep(3)
    navegador.find_element('xpath', '//*[@id="filterform"]/div[1]/div[2]/div/input[1]')\
        .send_keys(f"{dia_de_saida} {mes_abrev} {ano}")
    sleep(1)

    # Atualizar
    ActionChains(navegador).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    sleep(1)
    ActionChains(navegador).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()


def alterarpreco(_price):
    # Altera o valor do preço base
    sleep(3)
    navegador.find_element('xpath', '//*[@id="rates-block"]/div[1]/div[2]/div/input')\
        .send_keys(_price)
    sleep(3)
    navegador.find_element(By.CLASS_NAME, 'btn-primary').click()


def alterardata(_checkin, _checkout):
    sleep(3)
    # In
    # Clear
    navegador.find_element(By.XPATH, '/html/body/div[7]/div/div/div[2]/div/div/form/div[1]/div[1]/div/input').clear()
    sleep(3)
    # Preenche a data de entrada
    navegador.find_element(By.XPATH, '/html/body/div[7]/div/div/div[2]/div/div/form/div[1]/div[1]/div/'
                                     'input').send_keys(f"{_checkin} {mes_abrev} {ano}")
    ActionChains(navegador).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    sleep(3)

    # Out
    # Clear
    navegador.find_element(By.XPATH, '/html/body/div[7]/div/div/div[2]/div/div/form/div[1]/div[2]/div/input').clear()
    sleep(3)
    # Preenche a data de saída
    navegador.find_element(By.XPATH, '/html/body/div[7]/div/div/div[2]/div/div/form/div[1]/div[2]/div/'
                                     'input').send_keys(f"{_checkout} {mes_abrev} {ano}")
    ActionChains(navegador).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()


def young():
    sleep(3)
    global umavez
    if umavez is False:
        # Clica no + (expandir) para exibição dos preços
        navegador.find_element('xpath', '//*[@id="right-content-block"]/div/div/div/div[2]/div/table/tbody/'
                                        'tr/td[1]/div/div/table/tbody/tr[15]/td/div/div/span[2]').click()
        sleep(3)
        # Clica no preço
        navegador.find_element('xpath',
                               '/html/body/div[1]/main/div[2]/div/div/div[2]/div/div/div/div[2]/div/table/tbody'
                               '/tr/td[3]/div/div/div/table/tbody/tr[19]/td/div/div[2]/div[2]/div/div').click()
        umavez = True
    else:
        sleep(3)
        # Clica no preço ( HIGHLIGHT )
        navegador.find_element(By.XPATH, '/html/body/div[1]/main/div[2]/div/div/div[2]/div/div/div/div[2]/div/'
                                         'table/tbody/tr/td[3]/div/div/div/table/tbody/tr[19]/td/div/div[2]/div[20]'
                                         '/div').click()
        sleep(3)


def escolher_casa():
    print('Deseja alterar o preço de qual casa ?')
    print('1 - YOUNG')
    print('2 - CONFORT')
    print('3 - ECONOMICS')
    print('4 - FAMILY')
    print('5 - EXCLUSIVE')
    print('6 - SLIM')
    print('7 - DUNAS')
    print('8 - FORT')
    print('9 - OCEAN')
    entrada_das_datas()

    """ opcao = int(input('Digite sua opção: '))
    if opcao == 1:
        young() 
    elif opcao == 2:
    # confort()
    elif opcao == 3:
     # economics()
    elif opcao == 4:
     # family()
    elif opcao == 5:
     # exclusive()
    elif opcao == 6:
     # slim()
    elif opcao == 7:
     # dunas()
    elif opcao == 8:
     # fort()
    elif opcao == 9:
     # ocean()
     """


# criando cabeçalho da request
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/114.0.0.0 Safari/537.36 OPR/100.0.0.0"}

qtd_adultos_inicial = 4
qtd_quartos_inicial = 1


def criar_link(_checkin, _checkout, qtd_adultos=4, qtd_quartos=1):
    # criando o link
    url = f'https://www.booking.com/searchresults.pt-br.html?label=gen173nr-1BCAEoggI46AdIM1gEaCCIAQG' \
          f'YAS24ARfIARXYAQHoAQGIAgGoAgO4AvfbvKcGwAIB0gIkNjU0ZjM4N2EtYjk0Yi00Yjk1LThmOGYtYTQwMGU3MmUw' \
          f'Mzg52AIF4AIB&sid=3dfff8df8a2dc02f014946041a259ee6&aid=304142&ss' \
          f'=Cabo+Frio%2C+Estado+do+Rio+de+Janeiro%2C+Brasil&efdco=1&lang=pt-br' \
          f'&sb=1&src_elem=sb&dest_id=-632162&dest_type=city&ac_position=0&' \
          f'ac_click_type=b&ac_langcode=xb&ac_suggestion_list_length=5&search_selected=true' \
          f'&search_pageview_id=3e7a53bb85860208&ac_meta=GhAzZTdhNTNiYjg1ODYwMjA4IAAoATICeGI6CUNhYm8gRnJ' \
          f'pb0AASgBQAA%3D%3D&checkin={_checkin}&checkout={_checkout}&group_adults={qtd_adultos}&' \
          f'no_rooms={qtd_quartos}&group_children=0&sb_travel_purpose=leisure&order=price'
    return url


def alterar_qtd_adultos():
    qtd_adultos_alt = int(input('A busca será para quantos adultos ? '))
    global qtd_adultos_inicial
    qtd_adultos_inicial = qtd_adultos_alt


def alterar_qtd_quartos():
    qtd_quartos_alt = int(input('Quantos quartos ? '))
    global qtd_quartos_inicial
    qtd_quartos_inicial = qtd_quartos_alt


def soup(html_content):
    todos_os_precos = list()
    # Cria um objeto BeautifulSoup que pega o conteúdo da resposta e analisa/organiza
    sopa = BeautifulSoup(html_content, 'html.parser')

    # Encontrando um elementro específico na pagina
    precos = sopa.find_all("span", class_="f6431b446c fbfd7c1165 e84eb96b1f")
    pos = 0
    print('Lista de preços (Ordem Crescente) :')
    for cada in precos:
        pos += 1
        global dia_de_entrada
        global dia_de_saida
        divisor = dia_de_saida - dia_de_entrada
        todos_os_precos.append(float(cada.get_text()[3:9])/divisor)
        txt_interface_line = f"{pos}º        {cada.get_text()} "
        new_interface_line = Label(janela, text=txt_interface_line)
        new_interface_line.grid(column=0, row=11 + pos)
        print(cada.get_text())
    print(todos_os_precos)
    # mostrar_precos["text"] = todos_os_precos
    print(f'os preços são {precos}')
    # alterarpreco(todos_os_precos[posicao])


def fazer_requisicao(_checkin, _checkout):
    # Faz uma requisição para a página web
    response = requests.get(criar_link(_checkin, _checkout, qtd_adultos_inicial, qtd_quartos_inicial), headers=headers)

    # condensa o conteúdo da resposta
    html_content = response.content
    soup(html_content)


def menu():
    while True:
        print(f'FILTROS ATUAIS: Estado > Rj / Cidade > Cabo Frio / Quartos > {qtd_quartos_inicial} /'
              f' Adultos > {qtd_adultos_inicial} / Crianças > 0 / Ano > {ano} /'
              f'Mês > {mes_num}')
        print('-=' * 30)
        print('{:^30}'.format('-=MENU=-'))
        print('1- [Escolha as datas (CHECKIN E CHECKOUT)] ')
        print(f'2- [TODOS os preços desse MÊS {mes_num} desse ano {ano}] ')
        print('3- [Altere a quantidade de adultos] ')
        print('4- [Altere a quantidade de quartos] ')
        print('5- [Fechar programa]')
        print('-=' * 30)
        opcao = int(input('Digite sua opção: '))
        if opcao == 1:
            escolher_datas()
        elif opcao == 2:
            listar_precos_mes()
        elif opcao == 3:
            alterar_qtd_adultos()
        elif opcao == 4:
            alterar_qtd_quartos()
        elif opcao == 5:
            break
        else:
            print('Opção incorreta . Digite uma opção correta')


def escolher_datas():
    dia_entrada = int(input('Qual o dia de entrada [DD] ? '))
    dia_saida = int(input('Qual o dia de saída [DD] ? '))
    young()
    alterardata(dia_entrada, dia_saida)
    fazer_requisicao(checkin(ano, mes_num, dia_entrada), checkout(ano, mes_num, dia_saida))


def listar_precos_mes():
    dia_entrada = 1
    dia_saida = 3
    # 01 = janeiro ...
    qtd_dias_mes = {'01': 31, '02': 28, '03': 31, '04': 30, '05': 31, '06': 30, '07': 31,
                    '08': 31, '09': 30, '10': 31, '11': 30, '12': 31}

    while dia_saida < qtd_dias_mes[mes_num]:
        print('-' * 60)
        print(f'Checkin: {checkin(ano,mes_num,dia_entrada)}')
        print(f'Checkout: {checkout(ano,mes_num,dia_saida)}')
        young()
        alterardata(dia_entrada, dia_saida)
        fazer_requisicao(checkin(ano, mes_num, dia_entrada), checkout(ano, mes_num, dia_saida))
        dia_saida += 2
        dia_entrada += 2


def checkin(_ano, _mes_num, _dia_entrada):
    global dia_de_entrada
    dia_de_entrada = _dia_entrada
    return f'{_ano}-{_mes_num}-{_dia_entrada}'


def checkout(_ano, _mes_num, _dia_saida):
    global dia_de_saida
    dia_de_saida = _dia_saida
    return f'{_ano}-{_mes_num}-{_dia_saida}'


def mes_input(inp):
    global mes_num
    mes_num = inp


def converter_mes_abrev(mes):
    _mes = str(mes)
    meses_abrev = {'01': 'jan', '02': 'fev', '03': 'mar', '04': 'abr', '05': 'mai', '06': 'jun', '07': 'jul',
                   '08': 'ago', '09': 'set', '10': 'out', '11': 'nov', '12': 'dez'}
    return meses_abrev[_mes]


def clicou():
    global dia_de_entrada, dia_de_saida, ano, mes_num, mes_abrev
    mes_num = int(input_mes.get())
    mes_abrev = converter_mes_abrev(mes_num)
    dia_de_entrada = int(input_checkin.get())
    dia_de_saida = int(input_checkout.get())
    ano = int(input_ano.get())

    fazer_requisicao(checkin(ano, mes_num, dia_de_entrada), checkout(ano, mes_num, dia_de_saida))



# Inicio da janela
janela = Tk()
# titulo
janela.title("Programa para listar os 25 menores preços Cabo Frio - Rj")
# tamanho
janela.geometry("600x400")
# txt filtros
texto_filtros = Label(janela, text=f'FILTROS ATUAIS: Estado = Rj / Cidade = Cabo Frio / Quartos = {qtd_quartos_inicial}'
                                   f' / Adultos = {qtd_adultos_inicial} / Crianças = 0')
texto_filtros.grid(column=0, row=0)
# txt input_window_ano
texto2 = Label(janela, text=f"Para qual ano [AAAA]:")
texto2.grid(column=0, row=1)
# input ano
input_ano = Entry(janela, width=100)
input_ano.grid(column=0, row=2)
# txt input_window_mês
texto_mes = Label(janela, text=f"Escolha o mês que será pesquisado [MM]: ")
texto_mes.grid(column=0, row=3)
# input mês
input_mes = Entry(janela, width=100)
input_mes.grid(column=0, row=4)
# txt checkin
texto_checkin = Label(janela, text="Dia de entrada [DD]:")
texto_checkin.grid(column=0, row=5)
# input checkin
input_checkin = Entry(janela, width=100)
input_checkin.grid(column=0, row=6)
# txt checkout
texto_checkout = Label(janela, text="Dia de saída [DD]")
texto_checkout.grid(column=0, row=7)
# input checkout
input_checkout = Entry(janela, width=100)
input_checkout.grid(column=0, row=8)
# botão listar
botao = Button(janela, text="Listar preços", command=clicou)
botao.grid(column=0, row=9)
# txt precos
mostrar_precos = Label(janela, text=f"")
mostrar_precos.grid(column=0, row=10)


# fim da janela
janela.mainloop()

# mes_num = str(input('Escolha o mês [MM] : '))
mes_abrev = 'nov'  # str(input('Escreva a abreviação do Mês [jan/fev/mar]: ')).lower()  # FAZER UMA LISTA COM OS
# MESES LIDA POR MM (LINHA 282)
# ano = int(input('Escolha o ano[AAAA] : '))

# logar_no_site()
# calendariogeral()
# menu()
input()
