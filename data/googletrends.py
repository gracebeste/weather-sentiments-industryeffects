from pytrends.request import TrendReq

# Initialize pytrends
pytrends = TrendReq(hl='en-US', tz=360)

# Define keywords and timeframe
keywords = ["sunscreen", "SPF", "UV protection", "skincare"]
pytrends.build_payload(keywords, cat=0, timeframe='2013-01-01 2024-12-28', geo='US', gprop='')

# Fetch interest over time
data = pytrends.interest_over_time()
data.to_csv('google_trends_sunscreen.csv')
print("Google Trends data saved.")
