import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import ast

# Path to the uploaded CSV file with keywords
csv_file_path = "/Users/utsavsharma/Desktop/RR/CleanedCSVs/cleaned_resumes_with_keywords.csv"

# Load the CSV file
df_keywords = pd.read_csv(csv_file_path)

# Convert the keywords from string representation of lists to actual lists
df_keywords['keywords'] = df_keywords['keywords'].apply(ast.literal_eval)

# Flatten the list of keywords and count their occurrences
all_keywords = [keyword for sublist in df_keywords['keywords'] for keyword in sublist]
keyword_counts = Counter(all_keywords)

# Create a DataFrame for the keyword counts
df_keyword_counts = pd.DataFrame(keyword_counts.items(), columns=['keyword', 'count'])

# Plot the top 20 most common keywords
top_n = 20
top_keywords = df_keyword_counts.nlargest(top_n, 'count')

plt.figure(figsize=(12, 8))
plt.barh(top_keywords['keyword'], top_keywords['count'], color='blue')
plt.xlabel('Count')
plt.ylabel('Keyword')
plt.title('Top 20 Keywords in Resumes')
plt.gca().invert_yaxis()  # To display the highest count at the top
plt.tight_layout()
plt.show()

