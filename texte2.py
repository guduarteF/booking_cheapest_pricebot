import requests
from bs4 import BeautifulSoup

def get_hotel_prices():
    search_url = f'https://www.booking.com/searchresults.pt-br.html?label=gen173nr-1BCAEoggI46AdIM1gEaCCIAQGYAS24ARfIARXYAQHoAQ' \
      f'GIAgGoAgO4AvfbvKcGwAIB0gIkNjU0ZjM4N2EtYjk0Yi00Yjk1LThmOGYtYTQwMGU3MmUwMzg52AIF4AIB&sid=3dfff8df8a2dc02f01494' \
      f'6041a259ee6&aid=304142&ss=Cabo+Frio%2C+Estado+do+Rio+de+Janeiro%2C+Brasil&efdco=1&lang=pt-br&sb=1&src_elem=s' \
      f'b&dest_id=-632162&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=xb&ac_suggestion_list_length=5&' \
      f'search_selected=true&search_pageview_id=3e7a53bb85860208&ac_meta=GhAzZTdhNTNiYjg1ODYwMjA4IAAoATICeGI6CUNhYm8' \
      f'gRnJpb0AASgBQAA%3D%3D&checkin=2023-10-01&checkout=2023-10-03&group_adults=4&no_rooms=1&group_children=0&sb' \
      f'_travel_purpose=leisure&order=price'

    response = requests.get(search_url)
    soup = BeautifulSoup(response.content, "html.parser")

    prices = []

    # Find all elements containing price information
    price_elements = soup.find_all("div", class_="sr__card_price")


    for element in price_elements:
        price_text = element.get_text()
        print(price_text)
        prices.append(price_text)
        """
        # Extract numerical price from the text (assuming the format "$XXX")
        price = int(price_text.replace("$", ""))
        
        """
    return prices

if __name__ == "__main__":

    prices = get_hotel_prices()

    if prices:
        prices.sort()
        print("Preços do menor para o maior:")
        for price in prices:
            print(f"${price}")
    else:
        print("Nenhum preço encontrado.")
    