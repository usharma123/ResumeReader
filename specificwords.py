import re
import pandas as pd
from collections import defaultdict
import ast

# Load the CSV file
csv_file_path = "/Users/utsavsharma/Desktop/ResumeReader/cleaned_resumes_with_keywords.csv"
df = pd.read_csv(csv_file_path)

# Convert the keywords from string representation of lists to actual lists
df['keywords'] = df['keywords'].apply(ast.literal_eval)

# Define patterns for work experience
work_exp_patterns = re.compile(r"\bexperience\b|\bwork\b|\bprofessional experience\b|\bemployment\b", re.IGNORECASE)

# Function to extract work experience section
def extract_work_experience(text, pattern):
    sections = []
    lines = text.split('\n')
    capture = False
    for line in lines:
        if re.search(pattern, line):
            capture = True
        elif capture and (line.strip() == '' or re.search(r"^\s*[A-Z][a-z]*\s*$", line)):  # Stop capturing at new section
            capture = False
        if capture:
            sections.append(line)
    return " ".join(sections)

# Extract work experience sections
df['work_exp_section'] = df['cleaned_text'].apply(lambda text: extract_work_experience(text, work_exp_patterns))

# Define a function to highlight key entries in work experience
def highlight_key_experience(text):
    key_words = ['intern', 'research', 'project', 'lead', 'manager', 'engineer', 'developer', 'analyst']
    highlighted_text = text
    for word in key_words:
        highlighted_text = re.sub(r'\b{}\b'.format(word), r'**\g<0>**', highlighted_text, flags=re.IGNORECASE)
    return highlighted_text

# Highlight key work experience entries
df['highlighted_work_exp'] = df['work_exp_section'].apply(highlight_key_experience)

# Save the highlighted work experience entries to a new CSV file
highlighted_work_exp_csv_path = "/Users/utsavsharma/Desktop/ResumeReader/highlighted_work_experience.csv"
df[['filename', 'highlighted_work_exp']].to_csv(highlighted_work_exp_csv_path, index=False)

print(f"Highlighted work experience entries have been saved to {highlighted_work_exp_csv_path}")
