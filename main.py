from dotenv import load_dotenv
import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import DocumentAnalysisClient
import streamlit as st
import base64

st.title('Text Extractor')

# Azure Form Recognizer credentials


load_dotenv()
endpoint = os.getenv("ENDPOINT")
key = os.getenv("KEY")

# Helper function to format bounding box
def format_bounding_box(bounding_box):
    if not bounding_box:
        return "N/A"
    return ", ".join(["[{}, {}]".format(p.x, p.y) for p in bounding_box])
    
    

# Function to extract text from files using Azure Form Recognizer
def extract_text_from_pdf(uploaded_file):
    document_analysis_client = DocumentAnalysisClient(
        endpoint=endpoint, credential=AzureKeyCredential(key)
    )
    
    poller = document_analysis_client.begin_analyze_document(
            "prebuilt-read", document=uploaded_file)
    result = poller.result()

    text = ''
    for page in result.pages:
        for line in page.lines:
            text += line.content + ' ' + '\n'
            
    return text


  

    # Display PDF layout and extracted text
    st.write('PDF Layout:', unsafe_allow_html=True)
    st.write(html, unsafe_allow_html=True)
    
    st.write('Extracted Text:', text)


# Streamlit app
uploaded_file = st.file_uploader('Choose a file')
if uploaded_file is not None:
    # Decode uploaded file into a bytes object
    encoded_pdf = uploaded_file.read()
    
    # Extract text using Azure Form Recognizer
    text = extract_text_from_pdf(encoded_pdf)

   
    
    # Display extracted text
    st.write('Extracted Text:')
    st.write("````")
    st.write(text.split('\n'))
    st.write("````")
    
   
 
    
    



    













