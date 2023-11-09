# Tk Inter lida com a parte de interface do programa
import tkinter
from tkinter import ttk
# Request faz todas as requisições booking.com e stay.net
import requests
# Beautiful Soup recolhe as informações (raspagewm de dados) do site e organiza de forma legível
from bs4 import BeautifulSoup
# Selenium faz a automatização de ações no navegador
from selenium import webdriver
# WebDriver faz a sincronização de versão do navegador em questão (Chrome)
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
dia_de_saida = 3
umavez = False
ano = 2023
mes_num = 11
posicao = 5  # int(input('Em qual posição da lista você deseja estar ?'))  # PEDIR A POSIÇÃO SÓ QUANDO GERAL OS PREÇOS ?
# def selecionar_mes():
login = ""
senha = ""
allprices = list()
mes_inteiro = True


def logar_no_site():
    # Request da conexão
    navegador.get("https://tnp.stays.com.br/i/home")
    sleep(1)
    # Prenchimento de login
    while True:
        try:
            (navegador.find_element('xpath', '//*[@id="login-form"]/form/div[1]/input').
             send_keys(login))
            navegador.find_element('xpath', '//*[@id="login-form"]/form/div[2]/div/input').send_keys(senha)
            navegador.find_element('xpath', '//*[@id="login-form"]/form/div[3]/div/button').click()
            break
        except Exception as erro:
            print(f'O erro foi {erro.__class__}')
        sleep(3)


def calendariogeral():
    while True:
        try:
            # Seleciona o menu de opções
            navegador.find_element('xpath', '//*[@id="leftmenu"]/div[1]/ul/li/a/i').click()
            sleep(3)
            # Calendário Geral
            navegador.find_element('xpath', '//*[@id="leftmenu-scroll"]/div[2]/ul/div[3]/li[4]/a/span').click()
            break
        except Exception as erro:
            print(f'O erro foi {erro.__class__}')
    sleep(3)


def entrada_das_datas():
    sleep(3)
    while True:
        try:
            # Data de entrada
            navegador.find_element('xpath',  '/html/body/div[7]/div/div/div[2]/div/div/form'
                                             '/div[1]/div[1]/div/input').clear()
            sleep(3)
            navegador.find_element('xpath', '/html/body/div[7]/div/div/div[2]/div/div/form/div[1]/div[1]/div/input')\
                .send_keys(f"{dia_de_entrada} {mes_abrev} {ano}")
            ActionChains(navegador).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
            sleep(3)
            # Data de saída
            navegador.find_element('xpath', '/html/body/div[7]/div/div/div[2]/div/div/form'
                                            '/div[1]/div[2]/div/input').clear()
            sleep(3)
            navegador.find_element('xpath', '/html/body/div[7]/div/div/div[2]/div/div/form/div[1]/div[2]/div/input')\
                .send_keys(f"{dia_de_saida} {mes_abrev} {ano}")
            sleep(1)

            # Atualizar
            ActionChains(navegador).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
            sleep(1)
            ActionChains(navegador).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
            break
        except Exception as erro:
            print(f'O erro foi {erro.__class__}')


def alterarpreco(_price):
    # Altera o valor do preço base
    sleep(3)
    while True:
        try:
            navegador.find_element('xpath', '/html/body/div[7]/div/div/div[2]/div/div/form/div[3]/div/table/tbody/tr[1]'
                                            '/td[1]/div/div[1]/div/div[1]/input') \
                .send_keys(_price)
            sleep(3)
            navegador.find_element(By.CLASS_NAME, 'btn-primary').click()
            break
        except Exception as erro:
            print(f'O erro foi {erro.__class__}')


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
        try:
            # Clica no + (expandir) para exibição dos preços
            navegador.find_element('xpath', '/html/body/div[1]/main/div[2]/div/div/div[2]/div/div/div/div[2]/div/table/'
                                            'tbody/tr/td[1]/div/div/table/tbody/tr[16]/td/div/div/span[2]').click()
            sleep(3)
            # Clica no preço
            navegador.find_element('xpath',
                                   '/html/body/div[1]/main/div[2]/div/div/div[2]/div/div/div/div[2]/div/table/tbody/tr/'
                                   'td[3]/div/div/div/table/tbody/tr[20]/td/div/div[2]/div[2]/div').click()
            umavez = True

        except Exception as erro:
            print(f"O erro foi {erro.__class__}")
    else:
        sleep(3)
        # Clica no preço ( HIGHLIGHT )
        navegador.find_element(By.XPATH, '/html/body/div[1]/main/div[2]/div/div/div[2]/div/div/div/div[2]/div/table/'
                                         'tbody/tr/td[3]/div/div/div/table/tbody'
                                         '/tr[20]/td/div/div[2]/div[19]/div').click()
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
        valor = int(cada.get_text().replace('.', '')[3::])
        resultado = valor / divisor
        todos_os_precos.append(resultado)
        txt_price = f"{pos}º        {cada.get_text()} "
        new_price_line = Label(janela, text=txt_price)
        new_price_line.grid(column=1, row=1+pos)
        txt_diaria = f"R$ {round(resultado)}"
        new_diaria_value = Label(janela, text=txt_diaria)
        new_diaria_value.grid(column=2, row=1+pos)
        janela.update()

        print(cada.get_text())
    print(todos_os_precos)
    # mostrar_precos["text"] = todos_os_precos
    print(f'os preços são {precos}')
    global allprices
    allprices = todos_os_precos
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
    global dia_de_entrada, dia_de_saida
    dia_de_entrada = 1
    dia_de_saida = 3

    # 01 = janeiro ...
    qtd_dias_mes = {'01': 31, '02': 28, '03': 31, '04': 30, '05': 31, '06': 30, '07': 31,
                    '08': 31, '09': 30, '10': 31, '11': 30, '12': 31}

    while dia_de_saida < qtd_dias_mes[f'{mes_num}']:
        # Checkin txt
        txt_checkin = Label(janela, text=f'Check-in : {dia_de_entrada}')
        txt_checkin.grid(column=0, row=11)
        # Checkout txt
        txt_checkout = Label(janela, text=f'Check-out: {dia_de_saida}')
        txt_checkout.grid(column=0, row=12)

        print('-' * 60)
        print(f'Checkin: {checkin(ano,mes_num,dia_de_entrada)}')
        print(f'Checkout: {checkout(ano,mes_num,dia_de_saida)}')
        young()
        # alterardata(dia_entrada, dia_saida)
        fazer_requisicao(checkin(ano, mes_num, dia_de_entrada), checkout(ano, mes_num, dia_de_saida))
        dia_de_saida += 2
        dia_de_entrada += 2


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


def listar_precos():
    global dia_de_entrada, dia_de_saida, ano, mes_num, mes_abrev, input_pos
    mes_num = int(input_mes.get())
    mes_abrev = converter_mes_abrev(f'{mes_num}')
    ano = int(input_ano.get())

    if mes_inteiro:
        listar_precos_mes()
    else:
        dia_de_entrada = int(input_checkin.get())
        dia_de_saida = int(input_checkout.get())
        fazer_requisicao(checkin(ano, mes_num, dia_de_entrada), checkout(ano, mes_num, dia_de_saida))

    # txt pos
    texto_pos = Label(janela, text="Qual posição você quer incluir o seu preço ?")
    texto_pos.grid(column=0, row=17)
    # Grid pos
    input_pos.grid(column=0, row=18)
    # espaço vazio
    espaco_vazio = Label(janela, text="")
    espaco_vazio.grid(column=0, row=19)

    entrada_das_datas()
    alterarpreco(allprices[int(posicao) - 1])
def entrar():
    global posicao, login, senha
    posicao = input_pos.get()
    login = input_login.get()
    senha = input_senha.get()
    logar_no_site()
    calendariogeral()
    young()

    # Grid

    texto2.grid(column=0, row=9)
    input_ano.grid(column=0, row=10)
    texto_mes.grid(column=0, row=11)
    input_mes.grid(column=0, row=12)
    txt_checkb.grid(column=0, row=13)
    checkbutton1.grid(column=0, row=14)
    checkbutton2.grid(column=0, row=15)
    botao_listar.grid(column=0, row=16)



def buttoncheck1():
    # buttao do mes inteiro
    checkbutton2.deselect()
    # checkin
    texto_checkin.destroy()
    input_checkin.destroy()
    # checkout
    texto_checkout.destroy()
    input_checkout.destroy()
    global mes_inteiro
    mes_inteiro = True


def buttoncheck2():
    checkbutton1.deselect()
    # checkin
    texto_checkin.grid(column=0, row=17)
    input_checkin.grid(column=0, row=18)
    # checkout
    texto_checkout.grid(column=0, row=19)
    input_checkout.grid(column=0, row=20)
    botao_listar.grid(column=0, row=21)
    global mes_inteiro
    mes_inteiro = False


# Inicio da janela
janela = Tk()
# tamanho
janela.geometry("900x800")

# titulo
janela.title("Programa para listar os 25 menores preços Cabo Frio - Rj")


# txt filtros
texto_filtros = Label(janela, text=f'FILTROS ATUAIS: Estado = Rj / Cidade = Cabo Frio / Quartos = {qtd_quartos_inicial}'
                                   f' / Adultos = {qtd_adultos_inicial} / Crianças = 0')
texto_filtros.grid(column=0, row=0)

# txt casa
txt_casa = Label(janela, text='Escolha a casa: ')
txt_casa.grid(column=0, row=1)
# combobox casas
combobox = ttk.Combobox(janela, height=10)
combobox['values'] = ('Slim', 'Young', 'Economics', 'Family', 'Dunas', 'Exclusive',
                      'Bandeira', 'Fort Beach', 'Ocean Blue', 'Confort')
combobox.state(['readonly'])
combobox.grid(column=0, row=2)

# input pos
input_pos = Entry(janela, width=50)

# txt stays
txt_stays = Label(janela, text="Faça login com sua conta Stays para "
                               "alterar o seu preço com base na posição escolhida: ")
txt_stays.grid(column=0, row=3)
# txt login
txt_login = Label(janela, text="Login")
txt_login.grid(column=0, row=4)
# input login
input_login = Entry(janela, width=50)
input_login.grid(column=0, row=5)
# txt senha
txt_senha = Label(janela, text="Senha: ")
txt_senha.grid(column=0, row=6)
# input senha
input_senha = Entry(janela, width=50, show='*')
input_senha.grid(column=0, row=7)
# botão logar
entrar_site = Button(janela, text="Entrar", command=entrar)
entrar_site.grid(column=0, row=8)


# txt input_window_ano
texto2 = Label(janela, text=f"Para qual ano [AAAA]:")

# input ano
input_ano = Entry(janela, width=50)

# txt input_window_mês
texto_mes = Label(janela, text=f"Escolha o mês que será pesquisado [MM]: ")

# input mês
input_mes = Entry(janela, width=50)

# Text Checkbutton
txt_checkb = Label(janela, text=f"Pesquisar por: ")

# checkbutton
checkbutton1 = tkinter.Checkbutton(janela, text='Mês inteiro', command=buttoncheck1)

checkbutton1.select()
checkbutton2 = tkinter.Checkbutton(janela, text='Data específica', command=buttoncheck2)

# txt checkin
texto_checkin = Label(janela, text="Dia de entrada [DD]:")
# input checkin
input_checkin = Entry(janela, width=50)

# txt checkout
texto_checkout = Label(janela, text="Dia de saída [DD]")

# input checkout
input_checkout = Entry(janela, width=50)

# botão listar
botao_listar = Button(janela, text="Listar preços", command=listar_precos)


# Coluna 1
coluna_vazia = Label(janela, text='     ')
coluna_vazia.grid(column=1, row=2)
# Coluna 2
# txt precos
mostrar_precos = Label(janela, text=f"Menores preços [Ordem Crescente]")
mostrar_precos.grid(column=2, row=2)
# Coluna 3
# txt diarias
txt_diaria_value = Label(janela, text="Valor da diária: ", padx=100, pady=10)
txt_diaria_value.grid(column=3, row=2)

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
