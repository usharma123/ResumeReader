import pandas as pd
import matplotlib.pyplot as plt

# Path to the uploaded CSV file
csv_file_path = "/Users/utsavsharma/Desktop/RR/CleanedCSVs/cleaned_resumes_with_sentiment.csv"

# Load the CSV file
df = pd.read_csv(csv_file_path)

# Display the first few rows of the dataframe
print(df.head())

# Summary statistics for sentiment scores
summary_stats = df['sentiment_score'].describe()
print("Summary Statistics:\n", summary_stats)

# Plotting sentiment scores
plt.figure(figsize=(10, 6))
plt.bar(df['filename'], df['sentiment_score'], color='blue')
plt.xlabel('Resume Filename')
plt.ylabel('Sentiment Score')
plt.title('Sentiment Scores of Resumes')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# Sort the resumes by sentiment score
df_sorted = df.sort_values(by='sentiment_score', ascending=False)

# Display the sorted dataframe
print("Sorted Resumes by Sentiment Score:\n", df_sorted)
