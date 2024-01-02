import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
import matplotlib.pyplot as plt
from collections import Counter

nltk.download('stopwords')
nltk.download('punkt')


def count_words_in_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        words = word_tokenize(text)
        return len(words)


def top_10_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        words = word_tokenize(text)
        word_freq = Counter(words)
        top_words = word_freq.most_common(10)
        return top_words


def plot_bar_chart(data, title):
    words, frequencies = zip(*data)
    plt.bar(words, frequencies)
    plt.title(title)
    plt.xlabel('Слова')
    plt.ylabel('Кількість')
    plt.show()


def remove_stopwords_and_punctuation(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        stop_words = set(stopwords.words('english'))
        words = word_tokenize(text)

        filtered_words = [word.lower() for word in words if word.isalnum() or word in string.ascii_letters]

        filtered_words = [word for word in filtered_words if word.lower() not in stop_words]

        return filtered_words


file_path = 'milton-paradise.txt'

word_count = count_words_in_text(file_path)
print(f'1. Кількість слів у тексті: {word_count}')

top_words_before_removal = top_10_words(file_path)
print(f'2. 10 найбільш вживаних слів перед видаленням стоп-слів та пунктуації: {top_words_before_removal}')
plot_bar_chart(top_words_before_removal, 'Топ 10 слів перед видаленням стоп-слів та пунктуації')

filtered_words = remove_stopwords_and_punctuation(file_path)
top_words_after_removal = Counter(filtered_words).most_common(10)
print(f'3. 10 найбільш вживаних слів після видалення стоп-слів та пунктуації: {top_words_after_removal}')
plot_bar_chart(top_words_after_removal, 'Топ 10 слів після видалення стоп-слів та пунктуації')