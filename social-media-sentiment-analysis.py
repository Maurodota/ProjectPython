import tweepy
from textblob import TextBlob
import matplotlib.pyplot as plt

# Autenticação com a API do Twitter
api_key = 'your_api_key'
api_secret_key = 'your_api_secret_key'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'

auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Coletar tweets
public_tweets = api.search_tweets('Python', count=100)

# Analisar sentimentos
polarity = []
for tweet in public_tweets:
    analysis = TextBlob(tweet.text)
    polarity.append(analysis.sentiment.polarity)

# Visualizar resultados
plt.hist(polarity, bins=30)
plt.xlabel('Polaridade')
plt.ylabel('Frequência')
plt.title('Distribuição de Sentimentos')
plt.show()
