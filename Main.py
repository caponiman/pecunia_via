import summary
import quote
import financial_statements
import earnings
import stock_ratings
import finnhub
import os


#Sets Flag Variables
sflag = False #Summary
qflag = False #Quote
fflag = False #Financial Statements
eflag = False #Earnings
srflag = False #Stock Ratings
prflag = 1 #Continue Program Flag
stflag = 0 #Continue in stock analysis subroutine

#Retrives API Key from api_key.txt	
api_key_file = open("api_key.txt", "r")

#Sets API key to usable variable
finnhub_api_key = api_key_file.read().strip()

# Configure API key
configuration = finnhub.Configuration(
	api_key={
		'token': finnhub_api_key
		}
)
	
#Client Container
finnhub_client = finnhub.DefaultApi(finnhub.ApiClient(configuration))


while ( prflag == 1 ):
	
	#Clears screen
	os.system("clear")
	
	#Gets input for stock symbol from user
	print("Please input a stock symbol or type 0 to quit")
	symbol = input(": ")
	
	if ( symbol == "0" ):
		quit()
		continue
	
	#Removes whitespace
	symbol = symbol.strip()
	
	symbol = symbol.upper()
	
	stflag = 1
	
	while ( stflag == 1 ):
		
		os.system("clear")
		
		#Prompts user to choose a fuction
		print("Choose a function to see the data for " + symbol + " (" + finnhub_client.company_profile2(symbol=symbol).name + "):")
		print("-----------------------------------------------------------------")
		print("0: Exit to main menu")
		print("1: Stock Summary")
		print("2: Quotes")
		print("3: Financial Statements")
		print("4: Earnings")
		print("5: Stock's Ratings")
		user_input = input(": ")
	
		#Analyzes user's choice of function
		if (user_input == "0"):
			stflag = 0
			continue
				
		if ( user_input == "1" ):
			summary.stock_summary(symbol, finnhub_client)
			continue
			
		if ( user_input == "2" ): 
			a = quote.quote_get(symbol, finnhub_client)
			continue
			
		if ( user_input == "3" ):
			financial_statements.get_finstat()
			continue
			
		if ( user_input == "4" ):
			earnings.get_earnings()
			continue
			
		if ( user_input == "5" ):
			get_stock_ratings.get_ratings()
			continue
			
		if (user_input != "0" and user_input != "1" and user_input != "2" and user_input != "3" and user_input != "4" and user_input != "5" ):
			#os.system("clear")
			print("Function choice invalid try again!")	
		
			
		
