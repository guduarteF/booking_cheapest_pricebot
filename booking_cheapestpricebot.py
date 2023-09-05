import requests
from bs4 import BeautifulSoup

# criando cabeçalho da request
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/114.0.0.0 Safari/537.36 OPR/100.0.0.0"}
qtd_adultos_inicial = 4
qtd_criancas_inicial = 0
qtd_quartos_inicial = 1


def criar_link(checkin, checkout, qtd_adultos, qtd_criancas, qtd_quartos):
    # criando o link
    url = f'https://www.booking.com/searchresults.pt-br.html?label=gen173nr-1BCAEoggI46AdIM1gEaCCIAQG' \
          f'YAS24ARfIARXYAQHoAQGIAgGoAgO4AvfbvKcGwAIB0gIkNjU0ZjM4N2EtYjk0Yi00Yjk1LThmOGYtYTQwMGU3MmUw' \
          f'Mzg52AIF4AIB&sid=3dfff8df8a2dc02f014946041a259ee6&aid=304142&ss' \
          f'=Cabo+Frio%2C+Estado+do+Rio+de+Janeiro%2C+Brasil&efdco=1&lang=pt-br' \
          f'&sb=1&src_elem=sb&dest_id=-632162&dest_type=city&ac_position=0&' \
          f'ac_click_type=b&ac_langcode=xb&ac_suggestion_list_length=5&search_selected=true' \
          f'&search_pageview_id=3e7a53bb85860208&ac_meta=GhAzZTdhNTNiYjg1ODYwMjA4IAAoATICeGI6CUNhYm8gRnJ' \
          f'pb0AASgBQAA%3D%3D&checkin={checkin}&checkout={checkout}&group_adults={qtd_adultos}&no_rooms={qtd_quartos}' \
          f'&group_children={qtd_criancas}&sb_travel_purpose=leisure&order=price'

    return url


def alterar_qtd_adultos():
    qtd_adultos_alt = int(input('A busca será para quantos adultos ? '))
    return qtd_adultos_alt


def alterar_qtd_criancas():
    qtd_criancas_alt = int(input('A busca será para quantas crianças ? '))
    return qtd_criancas_alt


def alterar_qtd_quartos():
    qtd_quartos_alt = int(input('Quantos quartos ? '))
    return qtd_quartos_alt

def soup(html_content):
    # Cria um objeto BeautifulSoup que pega o conteúdo da resposta e analisa/organiza
    sopa = BeautifulSoup(html_content, 'html.parser')

    # Encontrando um elementro específico na pagina
    precos = sopa.find_all("span", class_="f6431b446c fbd1d3018c e729ed5ab6")
    for cada in precos:
        print(cada.get_text())





def fazer_requisicao(checkin, checkout):
    # Faz uma requisição para a página web
    response = requests.get(criar_link(checkin, checkout), headers=headers)
    # condensa o conteúdo da resposta
    html_content = response.content
    soup(html_content)


def menu():
    print('==' * 25)
    print('{:^50}'.format('Verifique os 25 menores preços booking.com:'))
    print('==' * 25)
    print('FILTROS ATUAIS: Estado > Rj / Cidade > Cabo Frio / Quartos > 1 / Adultos > 4 / '
          'Crianças > 0 / Ano > 2023')
    print('-=' * 25)
    print('{:^30}'.format('-=MENU=-'))
    print('1- ESCOLHA AS DATAS: (CHECKIN E CHECKOUT) ')
    print('2- ESCOLHA UM MÊS [MM] de um ano [AAAA]: ')
    print('3- ALTERE A QUANTIDADE DE PESSOAS [Adultos/Crianças]: ')
    print('4- ALTERE A QUANTIDADE DE QUARTOS')
    opcao = int(input('Digite sua opção: '))
    if opcao == 1:
        escolher_datas()
    elif opcao == 2:
        escolher_mes()
    '''elif opcao == 3 :
    # alterar_pessoas()
    elif opcao == 4 :
    # alterar_quartos()
    else:
    # Retornar erro'''


def escolher_datas():
    # A = ANO , M = MES , D = DIA
    mes = str(input('Escolha o mês [MM] : '))
    ano = int(input('Qual o ano [AAAA] : '))
    dia_entrada = int(input('Qual o dia de entrada [DD] ? '))
    dia_saida = int(input('Qual o dia de saída [DD] ? '))
    checkin = f'{ano}-{mes}-{dia_entrada}'
    checkout = f'{ano}-{mes}-{dia_saida}'
    fazer_requisicao(checkin, checkout)
    # checkin = input('Qual a data de checkin ? (AAAA-MM-DD) ')
    # checkout = input('Qual a data de checkout ? (AAAA-MM-DD) ')


def escolher_mes():
    # A = ANO , M = MES , D = DIA
    mes = str(input('Escolha o mês [MM] : ').lower())
    ano = int(input('Escolha o ano[AAAA] : '))
    dia_entrada = 1
    dia_saida = 3
    qtd_dias_mes = {'01': 31, '02': 28, '03': 31, '04': 30, '05': 31, '06': 30, '07': 31,
                    '08': 31, '09': 30, '10': 31, '11': 30, '12': 31}
    while dia_saida < qtd_dias_mes[mes]:
        print(f'Dia de entrada: {dia_entrada} / Dia de saída: {dia_saida} > PREÇOS: ')
        print('-=' * 15)
        checkin = f'{ano}-{mes}-{dia_entrada}'
        checkout = f'{ano}-{mes}-{dia_saida}'
        fazer_requisicao(checkin, checkout)
        dia_saida += 2
        dia_entrada += 2



menu()









