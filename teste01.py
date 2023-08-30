import requests
from bs4 import BeautifulSoup

# Faz uma requisição para a página web
# A = ANO , M = MES , D = DIA
checkin = '2023-12-30'
checkout = '2024-01-02'
#checkin = input('Qual a data de checkin ? (AAAA-MM-DD) ')
#checkout = input('Qual a data de checkout ? (AAAA-MM-DD) ')
url = f'https://www.booking.com/searchresults.pt-br.html?label=gen173nr-1BCAEoggI46AdIM1gEaCCIAQGYAS24ARfIARXYAQHoAQ' \
      f'GIAgGoAgO4AvfbvKcGwAIB0gIkNjU0ZjM4N2EtYjk0Yi00Yjk1LThmOGYtYTQwMGU3MmUwMzg52AIF4AIB&sid=3dfff8df8a2dc02f01494' \
      f'6041a259ee6&aid=304142&ss=Cabo+Frio%2C+Estado+do+Rio+de+Janeiro%2C+Brasil&efdco=1&lang=pt-br&sb=1&src_elem=s' \
      f'b&dest_id=-632162&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=xb&ac_suggestion_list_length=5&' \
      f'search_selected=true&search_pageview_id=3e7a53bb85860208&ac_meta=GhAzZTdhNTNiYjg1ODYwMjA4IAAoATICeGI6CUNhYm8' \
      f'gRnJpb0AASgBQAA%3D%3D&checkin={checkin}&checkout={checkout}&group_adults=4&no_rooms=1&group_children=0&sb' \
      f'_travel_purpose=leisure&order=price'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 OPR/100.0.0.0"}
response = requests.get(url, headers=headers)
html_content = response.content


# Cria um objeto BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Encontrando um elementro específico na pagina
precos = soup.find_all("span", class_="f6431b446c fbd1d3018c e729ed5ab6")
for cada in precos:
    print(cada.get_text())



# <span data-testid="price-and-discounted-price" aria-hidden="true" class="f6431b446c fbd1d3018c e729ed5ab6">R$&nbsp;296</span>
# <span data-testid="price-and-discounted-price" aria-hidden="true" class="f6431b446c fbd1d3018c e729ed5ab6">R$&nbsp;533</span>
