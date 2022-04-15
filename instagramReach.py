from cProfile import label
from ntpath import join
from optparse import Values
from unicodedata import name
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from sklearn.model_selection import train_test_split
from sklearn.linear_model import PassiveAggressiveRegressor

data = pd.read_csv("Book1.csv", encoding='latin1')
print(data.head())

# Chart
# plt.figure(figsize=(10, 8))
# plt.style.use('fivethirtyeight')
# plt.title("Distribution of Impressions from Home")
# sns.displot(data['Follows'])
# plt.show()

# # Pie Chart
# home = data["From Home"].sum()
# explore = data["From Explore"].sum()
# others = data["From Other"].sum()

# labels = ['From Home', 'From Explore', 'Others']
# value = [home, explore, others]

# fig = px.pie(data, values=value, names=labels,
#              title='Impressions from various source', hole=0.5)
# fig.show()

# # Analyzing Content
# text = " ".join(i for i in data.Hashtags)
# stopword = set(STOPWORDS)
# wordcloud = WordCloud(stopwords=stopword,
#                       background_color="white").generate(text)
# plt.style.use('classic')
# plt.figure(figsize=(12, 10))
# plt.imshow(wordcloud, interpolation='bilinear')
# plt.axis("off")
# plt.show

# # Analyzing Relationship
# figure = px.scatter(data_frame=data, x="Impressions", y="Likes",
#                     size="Likes", trendline="ols", title="Relationship")
# figure.show()
