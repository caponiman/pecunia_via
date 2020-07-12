import urllib
import json
import requests
import finnhub
import os


def stock_summary(stock_symbol, finnhub_client):

	os.system("clear")
	
	#Sets URL for information from yahoo finance
	url = "https://query1.finance.yahoo.com/v10/finance/quoteSummary/" + stock_symbol + "?formatted=true&crumb=ZGphzCI%2FwiA&lang=en-US&region=US&modules=summaryProfile%2CfinancialData%2CrecommendationTrend%2CupgradeDowngradeHistory%2Cearnings%2CdefaultKeyStatistics%2CcalendarEvents%2CesgScores%2Cdetails&corsDomain=finance.yahoo.com"

	#Opens Link
	response = urllib.request.urlopen(url)

	#Gets the data
	data = json.loads(response.read())

	#Simplifies data for programming
	quoteSummary=data['quoteSummary']['result'][0]['summaryProfile']
	
	#Outputs Summary
	print("Data on: " + stock_symbol + " (" + finnhub_client.company_profile2(symbol=stock_symbol).name + ")")
	print("-----------------------------------------------------------------")
	print("")
	print("Sector: " + quoteSummary['sector'])
	print("")
	print("Industry: " + quoteSummary['industry'])
	print("")
	print("Business Summary: " + quoteSummary['longBusinessSummary'])
	print("")
	input("Press enter to continue...")
	return 0;

