# from clarifai.rag import RAG

# api_key = 'e752d79a10b441d29bd7cb10219f4d85'
# user_id = "askompatel-1"

# rag_agent = RAG.setup(user_id=user_id, lm_url="https://clarifai.com/gep/generate/models/gemini-1_5-flash", api_key=api_key)

# def process_documents(folder_path):
#     print(f"Processing documents in {folder_path} locally...")

# def upload_documents(folder_path):
#     rag_agent.upload(folder_path=folder_path)
#     print(f"Documents uploaded successfully to Clarifai's vector database.")

# def main():
#     folder_path = input("Enter the folder path containing documents to process: ")
#     upload_documents(folder_path)
#     process_documents(folder_path)
#     messages = "Summarize this PDF"
#     response = rag_agent.chat(messages=messages)
#     print(response)

# if __name__ == "__main__":
#     main()

from clarifai.rag import RAG
from ipywidgets import FileUpload
from IPython.display import display
import os

api_key = 'e752d79a10b441d29bd7cb10219f4d85'
user_id = "askompatel-1"

if 'CLARIFAI_PAT' not in os.environ:
    os.environ['CLARIFAI_PAT'] = 'e752d79a10b441d29bd7cb10219f4d85'

# Set up the RAG agent
rag_agent = RAG.setup(user_id=user_id, lm_url="https://clarifai.com/gep/generate/models/gemini-1_5-flash", api_key=api_key)

# Function to upload a document from the system interactively
def upload_document():
    upload_button = FileUpload()
    display(upload_button)
    
    def on_upload_button_clicked(change):
        uploaded_filename = next(iter(upload_button.value))
        content = upload_button.value[uploaded_filename]['content']
        print(f"Uploaded document: {uploaded_filename}")
        return content
    
    upload_button.observe(on_upload_button_clicked, names=['data'])

def main():
    print("Please upload a document:")
    content = upload_document()
    
    if content:
        rag_agent.upload(content=content)
        print("Document uploaded successfully to Clarifai's vector database.")
        messages = "Summarize this PDF"
        response = rag_agent.chat(messages=messages)
        print(response)
    else:
        print("No document uploaded.")

main()













