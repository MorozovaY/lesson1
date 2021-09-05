def get_summ(one, two, delimiter='&'):
    text1 = one + delimiter + two
    text2 = text1.upper()
    print (text2)

get_summ ('Learn', 'python')


def format_price(price):
    price = int(price)
    real_price = f'Цена: {price} руб.'
    print (real_price)

format_price(56.24)