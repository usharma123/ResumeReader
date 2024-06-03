import docx
import fitz  # PyMuPDF
import re
import os
import csv

def extract_text_from_docx(file_path):
    doc = docx.Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs])

def extract_text_from_pdf(file_path):
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def clean_text(text):
    # Remove non-alphabetical characters and convert to lowercase
    cleaned_text = re.sub(r'[^A-Za-z\s]', '', text)
    cleaned_text = cleaned_text.lower()
    return cleaned_text

# Folder containing the resumes
resume_folder_path = "/Users/utsavsharma/Desktop/RR/Resumes"
output_csv_path = "cleaned_resumes.csv"

# Prepare the data for the CSV
resume_data = []

# Iterate over each file in the folder
for filename in os.listdir(resume_folder_path):
    file_path = os.path.join(resume_folder_path, filename)
    if filename.endswith(".docx"):
        text = extract_text_from_docx(file_path)
    elif filename.endswith(".pdf"):
        text = extract_text_from_pdf(file_path)
    else:
        continue  # Skip non-supported file types
    cleaned_text = clean_text(text)
    resume_data.append({"filename": filename, "cleaned_text": cleaned_text})

# Write the data to a CSV file
with open(output_csv_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=["filename", "cleaned_text"])
    writer.writeheader()
    for row in resume_data:
        writer.writerow(row)

print(f"Cleaned resumes have been saved to {output_csv_path}")
