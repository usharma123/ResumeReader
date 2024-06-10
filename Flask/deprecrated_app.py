from flask import Flask, request, render_template, redirect, url_for, flash, jsonify
import pandas as pd
from PyPDF2 import PdfReader
import docx
import nltk
from nltk.tokenize import word_tokenize
from io import BytesIO
import ssl
import string
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
from mlx_lm import load, generate

# Initialize Flask app
app = Flask(__name__)
app.secret_key = "supersecretkey"

# Bypass SSL certificate verification
ssl._create_default_https_context = ssl._create_unverified_context

# Download NLTK data
nltk.download('punkt')
nltk.download('stopwords')

from nltk.corpus import stopwords

# Load pre-trained model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased")

# load llama model
llama_model, llama_tokenizer = load("mlx-community/Meta-Llama-3-8B-Instruct-4bit")

# Initialize pipeline
nlp_pipeline = pipeline("text-classification", model=model, tokenizer=tokenizer)

# Function to extract text from PDF
def extract_text_from_pdf(pdf_content):
    text = ""
    reader = PdfReader(BytesIO(pdf_content))
    for page in reader.pages:
        text += page.extract_text()
    return text

# Function to extract text from DOCX
def extract_text_from_docx(docx_content):
    doc = docx.Document(BytesIO(docx_content))
    text = "\n".join([paragraph.text for paragraph in doc.paragraphs])
    return text

# Function to clean and preprocess text
def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = word_tokenize(text)
    words = [word for word in words if word.isalpha()]
    words = [word for word in words if word not in stop_words]
    return " ".join(words)

# Predefined list of skills for different domains
skills_list = ['python', 'java', 'c++', 'machine learning', 'data analysis', 'deep learning', 'tensorflow', 'pytorch', 'nlp', 'natural language processing',
               'biomedical', 'signal processing', 'neural networks', 'genomics', 'biotechnology', 'bioinformatics',
               'research', 'literature review', 'experiment', 'analysis', 'clinical trials', 'data collection', 'data analysis']

def extract_skills_with_model(text):
    skills = []
    for skill in skills_list:
        if skill in text:
            skills.append(skill)
    return skills

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        uploaded_files = request.files.getlist("file")
        resume_data = []
        for file in uploaded_files:
            content = file.read()
            if file.filename.endswith(".pdf"):
                text = extract_text_from_pdf(content)
            elif file.filename.endswith(".docx"):
                text = extract_text_from_docx(content)
            else:
                flash(f"Unsupported file type: {file.filename}")
                continue
            processed_text = preprocess_text(text)
            skills = extract_skills_with_model(processed_text)
            resume_data.append({"filename": file.filename, "skills": skills})
        return render_template('skills.html', resumes=resume_data)

    return render_template('upload.html')

@app.route('/llm_intro', methods=['GET', 'POST'])
def llm_intro():
    if request.method == 'POST':
        user_message = request.json.get('message')
        conversation = request.json.get('conversation', [])
        
        messages = [ {"role": "system", "content": "You are a hiring manager looking to hire an employee. Assist the user in determing the right skills."}]
        
        # add the messages to the top of the conversation before applying template
        messages.extend(conversation) 
        messages.append({"role": "user", "content": user_message})
        
        input_ids = llama_tokenizer.apply_chat_template(messages, 
                                          add_generation_prompt=True)
        prompt = llama_tokenizer.decode(input_ids)
        
        response = generate(llama_model, llama_tokenizer, prompt=prompt)
        
        conversation.append({"role": "user", "content": user_message})
        conversation.append({"role": "system", "content": response})

        return jsonify({"conversation": conversation, "response": response})
    else:
        return render_template('llm_intro.html')

if __name__ == '__main__':
    app.run(debug=True)
