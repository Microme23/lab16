import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, PorterStemmer
import string

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

input_file_path = 'text_inp.txt'
output_file_path = 'text_outp.txt'

with open(input_file_path, 'r', encoding='utf-8') as file:
    text = file.read()

tokens = word_tokenize(text)

lemmatizer = WordNetLemmatizer()
lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]

stemmer = PorterStemmer()
stemmed_tokens = [stemmer.stem(token) for token in tokens]

stop_words = set(stopwords.words('english'))
filtered_tokens = [token for token in lemmatized_tokens if token.lower() not in stop_words]

filtered_tokens = [token for token in filtered_tokens if token not in string.punctuation]

with open(output_file_path, 'w', encoding='utf-8') as file:
    file.write(' '.join(filtered_tokens))