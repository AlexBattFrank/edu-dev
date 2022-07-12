import requests
import json
from config import keys


class ConvertionException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: float):
        if quote == base:
            raise ConvertionException(f'It is not possible to convert the same currency - {base} ')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Failed to receive exchange currency {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Failed to receive exchange currency {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Failed to receive currency amount {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content) [keys[base]] * float(amount)

        return total_base
