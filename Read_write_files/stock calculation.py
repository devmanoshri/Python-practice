with open("stocks.csv","r") as f , open("output.csv","w") as out:
    out.write("Company Name,	PE Ratio,	PB Ratio \n")
    next(f)
    for line in f:
        token=line.split(",")
        print(token)
        stock_name=token[0]
        price=float(token[1])
        eps=float(token[2])
        book_val=float(token[3])
        pe_ratio=round(price/eps,2)
        price_to_book_ratio = round(price / book_val,2)
        out.write(f"{stock_name},{pe_ratio},{price_to_book_ratio}\n")

