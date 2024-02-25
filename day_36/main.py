import requests
from datetime import datetime, timedelta
from twilio.rest import Client

#reading yesterday's date

today = datetime.now().date()
yesterday_date = today - timedelta(1)
day_before = today - timedelta(2)
# print(today)
# print(yesterday_date)
# print(day_before)

account_sid = "AC02bd74d61a154c1a7f0e4f74009be531"
auth_token = "3eab32ec09702538108fd3c2421d8bee"

client = Client(account_sid, auth_token)

STOCK_NAME = "GOOGL"
COMPANY_NAME = "GOOGLE"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
param = {
    "apikey" : "V9KD8UMYO1T17R94",
    "symbol" : "GOOGL",
    "function" : "TIME_SERIES_DAILY",
}

r = requests.get(STOCK_ENDPOINT, params=param)
data = r.json()
#print(data)

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# #TODO 1. - Check last refreshed date. if it is not like yesterday - then take last refreshed date and compare price czyli t
# TODO - traktuj jako wczoraj date i pobierz z tego dane

yesterday = None
refreshed = data['Meta Data']['3. Last Refreshed']

if refreshed == str(yesterday_date):
    yesterday = data["Time Series (Daily)"][str(yesterday_date)]['4. close']
elif refreshed == str(day_before):
    yesterday = data["Time Series (Daily)"][str(day_before)]['4. close']
    day_before = day_before - timedelta(1)

if yesterday is not None:
    yesterday = float(yesterday)
    #print(yesterday)
else:
    print("Error: Yesterday's data not available")

print(yesterday)

# #TODO 2. - Get the day before yesterday's closing stock price
#
two_day_before = data["Time Series (Daily)"][f'{day_before}']['4. close']
two_day_before = float(two_day_before)
print(two_day_before)

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is
# 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
#
difference = yesterday - two_day_before
difference = abs(difference)
#print(difference)
# #TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the
# # day before yesterday.
#

percent = round(((yesterday - two_day_before)/two_day_before * 100),2)
#print(percent)

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if percent > 5:
    param2 = {
        "q" : "Google",
        "pageSize":3,
        "apiKey":"11216ca89ed944398bf1d46963c196d9",
        "sortBy":"popularity"
    }

    news = requests.get(NEWS_ENDPOINT, params=param2)
    data2 = news.json()
    get_news = []
    get_news = [article['title'] for article in data2["articles"]]
    get_news += [article['description'] for article in data2["articles"]]
    print(get_news)


    articles = data2["articles"][0]['title']
    articles_d = data2["articles"][0]['description']
    get_news.append(articles)
    get_news.append(articles_d)
    articles2 = data2["articles"][1]['title']
    articles2_d = data2["articles"][1]['description']
    get_news.append(articles2)
    get_news.append(articles2_d)
    articles3 = data2["articles"][2]['title']
    articles3_d = data2["articles"][2]['description']
    get_news.append(articles3)
    get_news.append(articles3_d)
    #
    # print(data2)
    # print(articles)
    # print(articles2)
    # print(articles3)
    # print(get_news)
        ## STEP 2: https://newsapi.org/
        # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

    #TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

    #TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


        ## STEP 3: Use twilio.com/docs/sms/quickstart/python
        #to send a separate message with each article's title and description to your phone number.

    #TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

    articles_headline_description = [(article['title'], article['description']) for article in data2["articles"][:3]]
    print(articles_headline_description)

    #TODO 9. - Send each article as a separate message via Twilio.

    articles_headline_description1 = articles_headline_description[0]
    articles_headline_description2 = articles_headline_description[1]
    articles_headline_description3 = articles_headline_description[2]

    print(articles_headline_description1)
    print(articles_headline_description2)
    print(articles_headline_description3)

    message = client.messages \
        .create(
        body=f'{STOCK_NAME}: Today\'s stock change 🔺{percent}. Headline {articles_headline_description1}',
        from_="+16185911150",
        to="+48531305974")

    message = client.messages \
        .create(
        body=f'{STOCK_NAME}: Today\'s stock change 🔺{percent}. Headline {articles_headline_description2}',
        from_="+16185911150",
        to="+48531305974")

    message = client.messages \
        .create(
        body=f'{STOCK_NAME}: Today\'s stock change 🔺{percent}. Headline {articles_headline_description3}',
        from_="+16185911150",
        to="+48531305974")

elif percent >= 0 and percent < 5:
    message = client.messages \
        .create(
        body= f'{STOCK_NAME}: Today\'s stock change 🔺{percent}',
        from_="+16185911150",
        to="+48531305974"
    )
else:
    message = client.messages \
        .create(
        body=f'{STOCK_NAME}: Today\'s stock change 🔻{percent}',
        from_="+16185911150",
        to="+48531305974"
    )

#Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

