import finnhub
import os

def quote_get(stock_symbol, finnhub_client):

#Sets flag variable
	flag = 1

#Clears screen before starting user input
	os.system("clear")

#Parses FinnHub for stock quote
#
#

#Makes list <price> known to interpreter
	price = []

#Obtains Quote
	quote = finnhub_client.quote(stock_symbol)

#Sets current Price
	price.append(quote.c)

#Sets opening Price
	price.append(quote.o)

#Sets closing Price
	price.append(quote.pc)

#Sets 52 week high
	price.append(quote.h)

#Sets 52 week low
	price.append(quote.l)

#Parses FinnHub for Company Profile 2 data
#
#

#Makes list <geninfo> known to interpreter
	geninfo = []

#Obtains Company Info
	company_info = finnhub_client.company_profile2(symbol=stock_symbol)

#Sets company name
	geninfo.append(company_info.name)

#Sets stock exchange for which the swock is traded on
	geninfo.append(company_info.exchange)

#Sets the currency used for stock trades
	geninfo.append(company_info.currency)

#Prints output for user to read
#
#

#Clears screen when run from terminal
	os.system("clear")

#Header
	print("Data on: " + stock_symbol + " (" + geninfo[0] + ")")
	print("")

#Price Data
	print("Price Data (In " + geninfo[2] + "):")
	print("-----------------------------------------------------------------")
	print("")
	print("Quotes from: " + geninfo[1])
	print("")
	print("Current price: " + str(price[0]))
	print("")
	print("Opening price: " + str(price[1]))
	print("")
	print("Previous closing price: " + str(price[2]))
	print("")
	print("52 week high: " + str(price[3]))
	print("")
	print("52 week low: " + str(price[4]))
	print("")
	
	input("Press enter to continue...")
	return (0)




