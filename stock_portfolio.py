# Stock Portfolio Tracker

stocks = { 
    "AAPL" : 180,
    "TSLA" : 250,
    "GOOGL" : 140,
    "MSFT" : 420,
    "AMZN" : 190
}

total_investment = 0

print("===== STOCK PORTFOLIO TRACKER =====")
print("Available stocks :" , ",".join(stocks.keys()))

stock_name = input("Enter stock name: ").upper()

if stock_name in stocks:
    quantity = int(input("Enter quantity :"))

    price = stocks[stock_name]
    investment = price * quantity

    print("\nStock Price :" , price)
    print("Quantity :" , quantity) 
    print("Investment :" , investment)

    total_investment += investment

    print("Total Investment : " , total_investment)

else:
    print("Stock not found .")