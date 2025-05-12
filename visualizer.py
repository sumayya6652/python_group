# import matplotlib.pyplot as plt
# from collections import Counter

# def visualize_sources(articles):
#     sources = [article['source']['name'] for article in articles]
#     counts = Counter(sources)
#     plt.bar(counts.keys(), counts.values())
#     plt.title("Article Count by Source")
#     plt.xticks(rotation=45)
#     plt.tight_layout()
#     plt.show()


import matplotlib.pyplot as plt
from collections import Counter
from wordcloud import WordCloud


def visualize_sources(articles):
    sources = [article['source']['name'] for article in articles]
    counts = Counter(sources)
    plt.figure(figsize=(10, 5))
    plt.bar(counts.keys(), counts.values(), color='skyblue')
    plt.title("Article Count by Source")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def visualize_wordcloud(articles):
    text = " ".join([article['title'] for article in articles if article.get('title')])
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.title("Word Cloud of Article Titles")
    plt.tight_layout()
    plt.show()