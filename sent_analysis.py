import statistics
import matplotlib.pyplot as plt
from nltk.tokenize import sent_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer

# get input text
file = open('input.txt', 'r')
text = file.read()
file.close()

# tokenize the input and create a list of sentences
sentences: list[str] = sent_tokenize(text)

analyzer = SentimentIntensityAnalyzer()

# get individual sentence scores into a dictionary
compound = {}
for i in range(len(sentences)):
    compound[i] = analyzer.polarity_scores(sentences[i])['compound']

# plot sentence scores 
order = list(compound.keys())
scores = list(compound.values())
plt.figure(figsize = (15, 8))
plt.bar(order, scores, width = 0.5)
plt.xlabel('Sentence Number')
plt.ylabel('Compound Score')
plt.title('Ordered Score Distribution')
plt.show()

# return the overall score
final_score = { 'numerical': statistics.mean(list(compound.values())), 'textual': 'neutral' }

if final_score['numerical'] > 0:
    final_score['textual'] = 'positive'
elif final_score['numerical'] < 0:
    final_score['textual'] = 'negative'

print('Overall sentiment:', final_score['textual'], '| Final score:', final_score['numerical'])