import pandas as pd
from transformers import pipeline

# Load the CSV file
csv_file_path = "/Users/utsavsharma/Desktop/ResumeReader/cleaned_resumes.csv"
df = pd.read_csv(csv_file_path)

# Initialize the sentiment analysis pipeline
sentiment_analyzer = pipeline("sentiment-analysis")

# Analyze the sentiment for each resume
df['sentiment'] = df['cleaned_text'].apply(lambda text: sentiment_analyzer(text[:1000])[0])  # Limiting to the first 1000 characters

# Extract sentiment labels and scores
df['sentiment_label'] = df['sentiment'].apply(lambda x: x['label'])
df['sentiment_score'] = df['sentiment'].apply(lambda x: x['score'])

# Sort the resumes by sentiment score
df_sorted = df.sort_values(by='sentiment_score', ascending=False)

# Save the updated dataframe to a new CSV file
output_csv_path = "/Users/utsavsharma/Desktop/ResumeReader/cleaned_resumes_with_sentiment.csv"
df_sorted.to_csv(output_csv_path, index=False)

print(f"Sentiment analysis results have been saved to {output_csv_path}")
