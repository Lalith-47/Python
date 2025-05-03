def Stock(price,n):
    amount=[]
    while True:
        buy=int(input("Enter when you want to buy: "))
        sell=int(input("Enter when you want to sell: "))
        if (buy or sell)>n:
            print('Invalid day number')
            continue
        amount.append(price[sell]-price[buy])
        end=input('Want to stop?\nEnter y or n:')
        if end=='y':
            total=sum(amount)
            if total<1:
                print('Loss:',total)
            else:
                print("Profit:",total)
            break
        else:
            continue
def main():
    n=int(input('Enter Number of days to be traded including today: '))
    price=[]
    print('Enter prices of each day')
    for i in range(n+1):
        price.append(int(input()))
    Stock(price,n)
main()