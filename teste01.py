import requests
from bs4 import BeautifulSoup


def menu():
    print('-=' * 25)
    print('Verifique os 25 menores preços booking.com:')
    print('FILTROS ATUAIS: Estado > Rj / Cidade > Cabo Frio / Quartos > 1 / Adultos > 4 / '
          'Crianças > 0 / Ano > 2023')
    print('-=' * 25)
    print('{:^30}'.format('-=MENU=-'))
    print('1- ESCOLHA AS DATAS: (CHECKIN E CHECKOUT) ')
    print('2- ESCOLHA UM MÊS [MM] de um ano [AAAA]: ')
    print('3- ESCOLHA UM FERIADO: ')
    print('4- ALTERE A CIDADE/ESTADO DA BUSCA: ')
    print('5- ALTERE A QUANTIDADE DE PESSOAS [Adultos/Crianças]: ')
    print('6- ALTERE A QUANTIDADE DE QUARTOS')
    opcao = int(input('Digite sua opção: '))


menu()
# A = ANO , M = MES , D = DIA
mes = int(input('Escolha o mês [MM] : '))
ano = int(input('Qual o ano [AAAA] : '))
entrada = '01'
saida = '03'
checkin = f'{ano}-{mes}-{entrada}'
checkout = f'{ano}-{mes}-{saida}'
# checkin = input('Qual a data de checkin ? (AAAA-MM-DD) ')
# checkout = input('Qual a data de checkout ? (AAAA-MM-DD) ')

# criando o link
url = f'https://www.booking.com/searchresults.pt-br.html?label=gen173nr-1BCAEoggI46AdIM1gEaCCIAQGYAS24ARfIARXYAQHoAQ' \
      f'GIAgGoAgO4AvfbvKcGwAIB0gIkNjU0ZjM4N2EtYjk0Yi00Yjk1LThmOGYtYTQwMGU3MmUwMzg52AIF4AIB&sid=3dfff8df8a2dc02f01494' \
      f'6041a259ee6&aid=304142&ss=Cabo+Frio%2C+Estado+do+Rio+de+Janeiro%2C+Brasil&efdco=1&lang=pt-br&sb=1&src_elem=s' \
      f'b&dest_id=-632162&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=xb&ac_suggestion_list_length=5&' \
      f'search_selected=true&search_pageview_id=3e7a53bb85860208&ac_meta=GhAzZTdhNTNiYjg1ODYwMjA4IAAoATICeGI6CUNhYm8' \
      f'gRnJpb0AASgBQAA%3D%3D&checkin={checkin}&checkout={checkout}&group_adults=4&no_rooms=1&group_children=0&sb' \
      f'_travel_purpose=leisure&order=price'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/114.0.0.0 Safari/537.36 OPR/100.0.0.0"}

# Faz uma requisição para a página web

response = requests.get(url, headers=headers)
html_content = response.content


# Cria um objeto BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Encontrando um elementro específico na pagina
precos = soup.find_all("span", class_="f6431b446c fbd1d3018c e729ed5ab6")
for cada in precos:
    print(cada.get_text())
