import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the CSV file
csv_file_path = "/Users/utsavsharma/Desktop/ResumeReader/cleaned_resumes_with_sentiment.csv"
df = pd.read_csv(csv_file_path)

# Define a function to extract top N keywords using TF-IDF
def extract_keywords(text, n=10):
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform([text])
    tfidf_scores = tfidf_matrix.toarray().flatten()
    feature_names = vectorizer.get_feature_names_out()
    sorted_indices = tfidf_scores.argsort()[-n:][::-1]
    keywords = [feature_names[idx] for idx in sorted_indices]
    return keywords

# Apply the function to each resume
df['keywords'] = df['cleaned_text'].apply(lambda text: extract_keywords(text))

# Save the updated dataframe to a new CSV file
output_csv_path = "/Users/utsavsharma/Desktop/ResumeReader/cleaned_resumes_with_keywords.csv"
df.to_csv(output_csv_path, index=False)

# Display the dataframe with keywords
df[['filename', 'keywords']]
