# Sentiment Analyzer
The sentiment analyzer used for this task was the Valence Aware Dictionary and sEntiment Reasoner or VADER. VADER is part of the Natural Language Toolkit which has also been used for sentence tokenization. VADER provides multiple metrics to analyze text however the compound score was the one used to calculate the final score. Through research and experimentation, I found that VADER considers negation (not, no, etc.), punctuation (exclemation marks), and even adverbs (good vs very good) to calculate the compound score. The compound score is bound from -1 to 1.

## Individual Sentence Score
![Figure 1](https://i.imgur.com/DakUmCs.png)

## Overall Sentiment
The overall sentiment score for the provided text is 0.1712. This score was calculated by averaging the compound scores of the individual sentences.

## What it means
A compound score greater than 0 indicates positive sentiment. The maximum compound score is 1, meaning this text has an overall positive sentiment, but it is not overwhelmingly positive. A positive score mainly indicates a heavier use of words with a positive connotation (i.e. excellent, very good, happy).

## Expectation
This score is close to my expectation. After reading it, I noticed that the first paragraph has more negative sentiment than the second. While the first paragraph has mixed sentiment (as illustrated in Figure 1), the second one is overwhelmingly positive. Averaging them together and getting that score seems accurate.

## Citations
[NLTK](https://www.nltk.org/)

[NLTK Tokenize](https://www.nltk.org/api/nltk.tokenize.html)

[NLTK Sentiment](https://www.nltk.org/api/nltk.sentiment.html)

[Text Analytics for Beginners using NLTK](https://www.datacamp.com/community/tutorials/text-analytics-beginners-nltk)

[VADER](https://github.com/cjhutto/vaderSentiment)

[Matplotlib](https://matplotlib.org/2.0.2/index.html)

[Bar Plot in Matlib](https://www.geeksforgeeks.org/bar-plot-in-matplotlib/)
