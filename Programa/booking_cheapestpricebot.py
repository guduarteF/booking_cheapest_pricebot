import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep

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
# def selecionar_mes():


def entrar_e_logar_no_site():

    # Request da conexão
    navegador.get("https://tnp.stays.com.br/i/home")
    sleep(5)
    # Prenchimento de login
    navegador.find_element('xpath', '//*[@id="login-form"]/form/div[1]/input').send_keys("carloseduardoferre@gmail.com")
    navegador.find_element('xpath', '//*[@id="login-form"]/form/div[2]/div/input').send_keys("Rosy03011931@")
    navegador.find_element('xpath', '//*[@id="login-form"]/form/div[3]/div/button').click()
    sleep(5)
    calendariogeral()


def calendariogeral():

    # Seleciona o menu de opções
    navegador.find_element('xpath', '//*[@id="leftmenu"]/div[1]/ul/li/a/i').click()
    sleep(3)
    # Calendário Geral
    navegador.find_element('xpath', '//*[@id="leftmenu-scroll"]/div[2]/ul/div[3]/li[4]/a/span').click()
    sleep(3)
    # escolher_casa()

    input()


# def escolher_casa():


# criando cabeçalho da request
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/114.0.0.0 Safari/537.36 OPR/100.0.0.0"}

qtd_adultos_inicial = 4
qtd_quartos_inicial = 1


def criar_link(checkin, checkout, qtd_adultos=4, qtd_quartos=1):
    # criando o link
    url = f'https://www.booking.com/searchresults.pt-br.html?label=gen173nr-1BCAEoggI46AdIM1gEaCCIAQG' \
          f'YAS24ARfIARXYAQHoAQGIAgGoAgO4AvfbvKcGwAIB0gIkNjU0ZjM4N2EtYjk0Yi00Yjk1LThmOGYtYTQwMGU3MmUw' \
          f'Mzg52AIF4AIB&sid=3dfff8df8a2dc02f014946041a259ee6&aid=304142&ss' \
          f'=Cabo+Frio%2C+Estado+do+Rio+de+Janeiro%2C+Brasil&efdco=1&lang=pt-br' \
          f'&sb=1&src_elem=sb&dest_id=-632162&dest_type=city&ac_position=0&' \
          f'ac_click_type=b&ac_langcode=xb&ac_suggestion_list_length=5&search_selected=true' \
          f'&search_pageview_id=3e7a53bb85860208&ac_meta=GhAzZTdhNTNiYjg1ODYwMjA4IAAoATICeGI6CUNhYm8gRnJ' \
          f'pb0AASgBQAA%3D%3D&checkin={checkin}&checkout={checkout}&group_adults={qtd_adultos}&no_rooms={qtd_quartos}' \
          f'&group_children=0&sb_travel_purpose=leisure&order=price'

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
    # Cria um objeto BeautifulSoup que pega o conteúdo da resposta e analisa/organiza
    sopa = BeautifulSoup(html_content, 'html.parser')

    # Encontrando um elementro específico na pagina
    precos = sopa.find_all("span", class_="f6431b446c fbd1d3018c e729ed5ab6")

    print('-=' * 30)
    print('Lista de preços (Ordem Crescente) :')
    for cada in precos:
        print(cada.get_text())


def fazer_requisicao(checkin, checkout):
    # Faz uma requisição para a página web
    response = requests.get(criar_link(checkin, checkout, qtd_adultos_inicial, qtd_quartos_inicial), headers=headers)
    # condensa o conteúdo da resposta
    html_content = response.content
    soup(html_content)


def menu():
    while True:
        print(f'FILTROS ATUAIS: Estado > Rj / Cidade > Cabo Frio / Quartos > {qtd_quartos_inicial} /'
              f' Adultos > {qtd_adultos_inicial} / Crianças > 0 / Ano > {ano} /'
              f'Mês > {mes}')
        print('-=' * 30)
        print('{:^30}'.format('-=MENU=-'))
        print('1- [Escolha as datas (CHECKIN E CHECKOUT)] ')
        print(f'2- [Calcular TODOS os preços desse MÊS {mes} desse ano {ano}] ')
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
    checkin = f'{ano}-{mes}-{dia_entrada}'
    checkout = f'{ano}-{mes}-{dia_saida}'
    fazer_requisicao(checkin, checkout)


def listar_precos_mes():
    dia_entrada = 1
    dia_saida = 3
    # 01 = janeiro ...
    qtd_dias_mes = {'01': 31, '02': 28, '03': 31, '04': 30, '05': 31, '06': 30, '07': 31,
                    '08': 31, '09': 30, '10': 31, '11': 30, '12': 31}

    while dia_saida < qtd_dias_mes[mes]:
        print(f'Dia de entrada: {dia_entrada} / Dia de saída: {dia_saida} > PREÇOS: ')
        checkin = f'{ano}-{mes}-{dia_entrada}'
        checkout = f'{ano}-{mes}-{dia_saida}'
        fazer_requisicao(checkin, checkout)
        dia_saida += 2
        dia_entrada += 2


def bemvindo():
    print('=' * 60)
    print('Programa para listar os 25 menores preços Cabo Frio - Rj')
    print('=' * 60)


bemvindo()
mes = str(input('Escolha o mês [MM] : ').lower())
ano = int(input('Escolha o ano[AAAA] : '))
menu()
