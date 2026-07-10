import yfinance as yf
from tabulate import tabulate


CLEAR = "\033[H\033[J" #clears terminal screen every time the function is called

def one_stock(output):
    try:
        if is_variable_in_file(output, "stocks.txt"):
            stock = yf.Ticker(output)
            price = stock.info.get("currentPrice")
            return f"{output}: {price}"
        else:
            raise Exception
    except Exception:
        return "Invalid Ticker"

def add():
    print(f"{CLEAR}Write stock ticker to add to your log. Otherwise, write 'done'")
    while True:
        name = input()
        try:
            if name.lower() != "done":
                if is_variable_in_file(name, "stocks.txt"):
                    with open("Wanted_Stocks.txt") as wanted_stocks:
                        if name in wanted_stocks.read():
                            print("Already written")
                        else:
                            with open("Wanted_Stocks.txt", "a", newline = "") as wanted_stocks:
                                wanted_stocks.write(f"{name}\n")
                else:
                    raise Exception
            else:
                print(CLEAR)
                break
        except Exception:
            print ("Invalid Ticker")
            continue

def remove():
    with open("Wanted_Stocks.txt") as wanted_stocks:
        lines = wanted_stocks.readlines()
    print(CLEAR)
    print("STOCKS:")
    for line in lines:
        print(line, end="")
    print("--------------------------------------------------------------------------------")
    print(f"Write stock ticker to remove from your log. Otherwise, write 'done'")
    while True:
        stock = input()
        try:
            if stock.lower() != "done":
                with open("Wanted_Stocks.txt") as wanted_stocks2:
                    lines2 = wanted_stocks2.readlines()
                if stock in unpacking(lines2):
                    updated_list = [line for line in lines2 if stock not in line]
                    with open("Wanted_Stocks.txt", "w", newline = "") as updated_file:
                        updated_file.writelines(updated_list)
                else:
                    raise Exception
            else:
                print(CLEAR)
                break
        except Exception:
            print("Not in list. Try again")

def show_log():
    print(f"{CLEAR}Your log | ADD(2) | REMOVE(3) ")
    print("______________________________________")
    with open("Wanted_Stocks.txt") as wanted_stocks:
        lines = wanted_stocks.readlines()
    for line in lines:
        print(line, end="")

def log_to_prices():
    box = []
    with open("Wanted_Stocks.txt") as wanted_stocks:
         lines = wanted_stocks.readlines()
         if len(lines) > 0:
            for ticker in unpacking(lines):
                stock = yf.Ticker(ticker)
                price = stock.info.get("currentPrice")
                collection = {"Ticker": ticker, "Price": f"${price}"}
                box.append(collection)
                print("\n")
                print(CLEAR + tabulate(box, headers="keys",tablefmt="grid")) #turns the list of dictionaries into a table
         else:
             print("No Tickers in Log")

def is_variable_in_file(var, file_name):
    with open(file_name) as file:
        content = file.read()
    return var in content

def unpacking(words): #removes \n from the list of words
    return [word.strip() for word in words]

def main():
    print(f"""{CLEAR}Welcome! This application helps track stock prices and organizes the tickers you're most interested in.
          You can add or remove tickers from your log, and at any time, you access this log.
          You can also find the real time price of any ticker or display the prices of all the tickers in your log.
          _________________________________________________________________________________________________________________________________
          To show your log, write "1" | To add on to your log, write "2" | To remove items from your log, write "3".
          _________________________________________________________________________________________________________________________________
          To see the price of one stock, write "4" | To see the prices of all your logged stocks, write "5" | To fully exit, write "6" \n""")

    while True:
        print("1. show log | 2. add | 3. remove | 4. stock price | 5. logged price | 6. exit")
        num = input("Select number: ")
        if num != "6":
            selection(num)
        else:
            print(f"{CLEAR}Thank you for using this application!")
            break

def selection(number):
    match number:
        case "1":
            show_log()
        case "2":
            add()
        case "3":
            remove()
        case "4":
            print(f"{CLEAR}What stock would you like to know the price of?")
            print(one_stock(input("Write ticker: ")))
        case "5":
            log_to_prices()
        case "6":
            pass
        

if __name__ == "__main__":
    main()



 


