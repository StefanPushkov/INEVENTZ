from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
import matplotlib.pyplot as plt
import itertools
import nltk
nltk.download('stopwords')
from sklearn.model_selection import train_test_split
from nltk.corpus import stopwords
from pymystem3 import Mystem
from string import punctuation
import pandas as pd

mystem = Mystem()
russian_stopwords = stopwords.words("russian")


# FIRST: Preprocessing
def preprocess_text(text):
    # 1. lowercase all words
    # 2. Lemmatize - interpret different forms of the same word as one word
    tokens = mystem.lemmatize(text.lower())
    # 3. Remove stopwords and punctuation
    tokens = [token for token in tokens if token not in russian_stopwords \
              and token != " " \
              and token.strip() not in punctuation]
    text = " ".join(tokens)

    return text


"""   APPLY PREPROCESSING   """
# data = pd.read_csv('E:/INEVENTZ/DATA/data.csv')
# data['text'] = data['text'].apply(lambda row: preprocess_text(str(row)))
# data.to_csv("E:/INEVENTZ/DATA/data_no_stopwords.csv", index=None, header=True)


data = pd.read_csv('E:/INEVENTZ/DATA/data_no_stopwords.csv')

# Create list of all WORDS in dataset
all_words = [i.split(' ') for i in data["text"]]
all_words = list(itertools.chain.from_iterable(all_words))

# Count length of each sentence in dataset
sentence_lengths = [len(tokens) for tokens in data["text"]]

# Create list of all UNIQUE words
VOCAB = sorted(list(set(all_words)))

print("%s words total, with a vocabulary size of %s" % (len(all_words), len(VOCAB)))
print("Max sentence length is %s" % max(sentence_lengths))


# PLot hist
fig = plt.figure(figsize=(10, 10))
plt.xlabel('Sentence length')
plt.ylabel('Number of sentences')
plt.hist(sentence_lengths)
plt.show()

def cv(data):
    count_vectorizer = CountVectorizer()

    emb = count_vectorizer.fit_transform(data)

    return emb, count_vectorizer

list_corpus = data["text"].tolist()
list_labels = data["label"].tolist()

X_train, X_test, y_train, y_test = train_test_split(list_corpus, list_labels, test_size=0.2,
                                                                                random_state=40)

X_train_counts, count_vectorizer = cv(X_train)
X_test_counts = count_vectorizer.transform(X_test)

from sklearn.linear_model import LogisticRegression

clf = LogisticRegression(C=30.0, class_weight='balanced', solver='newton-cg',
                         multi_class='multinomial', n_jobs=-1, random_state=40)
clf.fit(X_train_counts, y_train)

y_predicted_counts = clf.predict(X_test_counts)
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, classification_report


def get_metrics(y_test, y_predicted):
    # true positives / (true positives+false positives)
    precision = precision_score(y_test, y_predicted, pos_label=None,
                                average='weighted')
    # true positives / (true positives + false negatives)
    recall = recall_score(y_test, y_predicted, pos_label=None,
                          average='weighted')

    # harmonic mean of precision and recall
    f1 = f1_score(y_test, y_predicted, pos_label=None, average='weighted')

    # true positives + true negatives/ total
    accuracy = accuracy_score(y_test, y_predicted)
    return accuracy, precision, recall, f1


accuracy, precision, recall, f1 = get_metrics(y_test, y_predicted_counts)
print("accuracy = %.3f, precision = %.3f, recall = %.3f, f1 = %.3f" % (accuracy, precision, recall, f1))

'''
X = data['text']
# y = data[['label']].values

vectorizer = CountVectorizer(min_df=0, lowercase=False)
v=vectorizer.fit_transform(X)
print(vectorizer.vocabulary_)

from sklearn.model_selection import train_test_split



sentences = data['text'].values
y = data['label'].values

sentences_train, sentences_test, y_train, y_test = train_test_split(sentences, y, test_size=0.30, random_state=1000)
from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer()
vectorizer.fit(sentences_train)

X_train = vectorizer.transform(sentences_train)
X_test  = vectorizer.transform(sentences_test)
print(X_train)

from sklearn.ensemble import GradientBoostingClassifier

classifier = GradientBoostingClassifier()
classifier.fit(X_train, y_train)
score = classifier.score(X_test, y_test)
print(classifier.predict(vectorizer.fit_transform('Я завтра пойду в парк')))
print("Accuracy:", score)
'''