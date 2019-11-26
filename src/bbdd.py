from decimal import Decimal

def text_to_num(text):
    d = {
        'M': 6,
        'B': 9,
        'k': 3
    }
    if text[-1] in d:
        num, magnitude = text[:-1], text[-1]
        return int(Decimal(num) * 10 ** d[magnitude])
    else:
        return int(Decimal(text))

def quitaMonedas(df,columna):
    monedas = ['$','€','£','C','kr','¥']
    for moneda in monedas:
        df[columna] = df[columna].apply(lambda x: x.replace(moneda,''))