from datetime import date, timedelta
from pprint import pprint

import requests



def get_rates(currencies, days=30):
    end_date = date.today()
    start_date = end_date - timedelta(days=days)

    symbole = ','.join(currencies)
    requete = f"https://www.docstring.fr/api/rates/history/?start_at={start_date}&end_at={end_date}&symbols={symbole}"
    r = requests.get(requete)
    if not r and not r.json():
        return False, False

    api_rates = r.json().get("rates")
    all_rates = {currency: [] for currency in currencies}
    all_days = api_rates.keys()

    for each_day in all_days:
        [all_rates[currency].append(rate) for currency, rate in api_rates[each_day].items()]

    return all_days, all_rates



    # pprint(api_rates)





if __name__ == "__main__":
    days, rates = get_rates(currencies=["USD", "EUR"])
    pprint(days)
    pprint(rates)
