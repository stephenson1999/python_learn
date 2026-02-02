def caculate_profit(arr,a_size):
    profit = 0
    for i in range(1,a_size):
        if arr[i] > arr[i-1]:
            profit += arr[i] - arr[i-1]

    return profit

prices = [234,4,53,34,534,53,453,4,65,7,87656,345765,34567543,234,54645,2342,765676,234234,6757,2342,676767]

profit = caculate_profit(prices, len(prices))
print("Max profit: ", profit)


def find_water(a,a_size):
    left_tallest = [0]*a_size
    right_tellest = [0]*a_size
    water = 0
    left_tallest[0] = a[0]
    for i in range(1,a_size):
        left_tallest[i] = max(left_tallest[i-1], a[i])
    right_tellest[a_size-1] = a[a_size-1]
    for i in range(1,a_size):
        water += min(left_tallest[i], right_tellest[i]) - a[i]
    return water

a = [0,10101,1,0,3,5,6,6,4,7,9,5,3,56,8,5,3,5,7,9,6,4,670000,00000,0,0,0,0,0,0,0,0,0]
bars = len(a)
print("Water: ",find_water(a,bars))
print("Bars: ", bars) 