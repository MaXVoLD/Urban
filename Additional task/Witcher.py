coin = [1, 5, 10, 25]

def cahs():
    price = int(input('Какую цену поставил ведьмак? '))
    sum_coins = 0
    for i in coin[::-1]:
        sum_coins += price // i
        price %= i
        print(f'{price} монет номиналом по {i}')
    print('Всего монет:', sum_coins)


cahs()
