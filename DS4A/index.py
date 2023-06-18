import requests
import pandas as pd
import time


#create request user header
headers = {'User Agent': "myemail@gmail.com"}

#get all companies data
companyTickers = requests.get(
"https://www.sec.gov/files/company_tickers.json", 
headers=headers)

#review response/keys to see if it was succesful 
# print(companyTickers.json().keys())

#format response to dictionary and get first key/value
firstentry = companyTickers.json()['0']
print(firstentry)


#dictionary to dataframe, every key (company) should be a row so use orient = index

companyData = pd.DataFrame.from_dict(companyTickers.json(), orient='index')
companyData.describe()

time.sleep(10)

#add leading zeros to CIK, not included from the CIK link endpoint
companyData['cik_str'] = companyData['cik_str'].astype(str).str.zfill(10)


#Let's try an example

cik = companyData[0:1].cik_str[0]

# print(companyData)

HEADERS = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}

#get company specific filing metadata
# filingMetadata= requests.get(
#     f'https://data.sec.gov/submissions/CIK{cik}.json',
#     headers=HEADERS
    
# )

# filingMetadata.raise_for_status()  # raises exception when not a 2xx response

# if filingMetadata.status_code != 204:
#     print(filingMetadata.json())
    
#HTTPError: 403 Client Error: Forbidden for url: https://data.sec.gov/submissions/CIK0000320193.json


###########The below line is the one generating the error##############

# print(filingMetadata.json().keys())
# filingMetadata.json()['filings']
# filingMetadata.json()['filings'].keys()
# filingMetadata.json()['filings']['recent']
# filingMetadata.json()['filings']['recent'].keys()


######Look up all the CIK for a specific entity by only using part of the name

# banks_list = ['jpmorgan chase', 'morgan stanley', 'goldman sachs group', 'bank of america', 'wells fargo', 'citigroup', 'toronto dominion bank']
banks_list = ['JPM', 'MS', 'GS', 'BAC', 'WFC', 'C', 'TD']
cik_list = []
ticker_list = []
lender_name = []

for i in banks_list:
    out = companyData[companyData['ticker'] == i]
    if out.empty:
        continue
    else:
        cik_list.append(out.iloc[0,0])
        ticker_list.append(out.iloc[0,1])
        lender_name.append(out.iloc[0,2])

    print(lender_name)
