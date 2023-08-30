import requests
from bs4 import BeautifulSoup


def get_booking_prices():
    checkin_date = '2023-08-30'
    checkout_date = '2024-09-01'
    adults = 4
    rooms = 2

    url = f"https://www.booking.com/searchresults.en-us.html?checkin={checkin_date}&checkout={checkout_date}&group_adults={adults}&group_rooms={rooms}"

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    price_elements = soup.find_all('div', class_='bui-price-display__value prco-font16-helper')
    prices = [float(price.get_text().replace('$', '').replace(',', '')) for price in price_elements]
    print(prices)
    return prices


if __name__ == "__main__":
    prices = get_booking_prices()

    if len(prices) >= 25:
        sorted_prices = sorted(prices)[:25]
        for i, price in enumerate(sorted_prices, start=1):
            print(f"{i}. ${price:.2f}")
    else:
        print("Não foi possível obter informações suficientes de preços.")