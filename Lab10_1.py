""" Lab 10.1 """
def coinExchange(amount, coinList):
    coin_checker = {0:10 , 1:5 , 2:2 , 3:1}
    f_coin = 0
    o_amount = amount
    s_coin = 0
    
    print("Amount:", o_amount)
    
    for i in range(4):
        coin = 0
        coin += coinList[i]
        s_coin += coin*coin_checker[i]
    
    if s_coin < amount:
        print("Coins are not enough.")
        return
    

    
    coinReturn = []
    for j in range(4):
        x = 0
        if j == 0:
            while coinList[j] > 0 and amount >= 10:
                coinList[j] -= 1
                x += 1
                amount -= coin_checker[j]
        elif j == 1:
            while coinList[j] > 0 and amount >= 5:
                coinList[j] -= 1
                x += 1
                amount -= coin_checker[j]
        elif j == 2:
            while coinList[j] > 0 and amount >= 2:
                coinList[j] -= 1
                x += 1
                amount -= coin_checker[j]
        elif j == 3:
            while coinList[j] > 0 and amount >= 1:
                coinList[j] -= 1
                x += 1
                amount -= coin_checker[j]

        coinReturn.append(x)
        f_coin += x
        
    print("Coint exchange result:", coinReturn)
    print("Number of coins:", f_coin)

    
coinList = [10, 10, 10, 10]
coinExchange(127, coinList)
print()
print("__________________________________________________________________")
print()

coinList = [10, 10, 10, 10]
coinExchange(249, coinList)