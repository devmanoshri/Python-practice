import statistics

stocks={
     "info": [600,630,620],
     "ril":	 [1430,1490,1567],
     "mtl":	 [234,180,160]
}

def print_all():
    for stock_name, stock_values in stocks.items():
        avg = statistics.mean(stock_values)
        print(f"{stock_name}  ==>  {stock_values} ==> avg: {round(avg,2)}")

def add_new_stock():
     print("Add new stock")
     new_stock= str(input("Enter new stock name:")).lower()
     new_stock_price = int(input("Enter new stock price:"))
     if new_stock in stocks:
         stocks[new_stock].append(new_stock_price)
     else:
         stocks[new_stock]= [new_stock_price]
     print_all()

def main():
    option= input("Enter your option (print or add): " ).lower()

    if option=='print':
        print_all()
    elif option== 'add':
        add_new_stock()
    else:
        print(" Unsupported operation:",option)

if __name__ == '__main__' :
    main()