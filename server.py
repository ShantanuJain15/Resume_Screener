from flask import Flask, request, url_for, redirect, render_template
import os
import pickle
import numpy as np
import PyPDF2
import re
from src.Resume_Screener.utils import cleanResume

app = Flask(__name__, template_folder=os.path.abspath(os.path.dirname(__file__)))


# Get the absolute path of the current file and the directory it's in
abs_path = os.path.abspath(__file__)
dir_path = os.path.dirname(abs_path)

# Build the path to the model file
model_path = os.path.join(dir_path, 'artifacts/model.pkl')

# Load the model from the file
with open(model_path, 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def hello_world():
    return render_template("templates/index.html")

@app.route('/predict', methods=['POST'])
def predict():
    # Get the uploaded file from the form data
    pdf_file = request.files['pdf_file']

    # Get the name of the uploaded file
    filename = pdf_file.filename

    # Save the uploaded file to the server
    file_path = os.path.join(dir_path, 'uploadedCV',filename)
    pdf_file.save(file_path)

    # Open the PDF file and extract the text
    pdf_file_obj = open(file_path, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file_obj)
    text = ''
    for page_num in range(len(pdf_reader.pages)):
        # page_obj = pdf_reader.getPage(page_num)
        page_obj = pdf_reader.pages[page_num]
        text += page_obj.extract_text()

    # Close the PDF file
    pdf_file_obj.close()


    cleaned_text = text.lower()
    cleaned_text = cleanResume(cleaned_text)

    predicted=model.predict([cleaned_text])

    # Display the extracted text
    return 'The most suitable job for: ' + filename + ' is -> ' + predicted[0]

if __name__ == '__main__':
    app.run(debug=True)