#important libraries wrt langchain
from langchain.text_splitter import RecursiveCharacterTextSplitter
 
#embedding technique / converting pdf to vectors 
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from google import generativeai as ai 
 
#vector embeddings
from langchain_community.vectorstores import FAISS

from langchain_google_genai import ChatGoogleGenerativeAI

#for chatting and defining prompts
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate

#importing our env 
import streamlit as st
from PyPDF2 import PdfReader #helps to read all the document
import os



#Main Code

#configure API Key
os.environ['GOOGLE_API_KEY'] = "AIzaSyBLpwLwUTsLeJDtH73pGCz5-PWoWKHJiDE"
ai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

#Read the PDf , Go through all pages, Extract the text
def get_pdf_text(pdf_docs):
    text=''
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text+= page.extract_text()
    return text         

# Dividing the whole text into 10,000 chunks/tokens , where overlap of 1000 can be possible
def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 2000 , chunk_overlap = 200)
    tokens = text_splitter.split_text(text)
    return tokens

#converting tokens/chunks to vectors
def get_vector_store(tokens):
    #add google generative ai embeddings
    embeddings = GoogleGenerativeAIEmbeddings(model='models/embedding-001')
    vector_store = FAISS.from_texts(tokens,embedding=embeddings)
    #this vector store can be saved in local env, database etc
    # FAISS_index will be the folders inside which we will have vectors
    vector_store.save_local('faiss_index')

def give_prompt():
    prompt_template = '''
    Act as a true expert and answer the question as detailed as possible in the provided context only,
    make sure to provide all the details,
    if the answer is not available in the context just say "Answer Not Available", Don't provide the wrong answer
    Context: \n{context}?\n
    Question: \n{question}\n
    
    Answer: 
    '''
    model = ChatGoogleGenerativeAI(model='gemini-pro',temperature=0.3)
    prompt = PromptTemplate(template=prompt_template,input_variables=['Context','Question'])
    
    #chain_type = 'stuff' helps to text summarization
    chain = load_qa_chain(model,chain_type = 'stuff',prompt = prompt)
    return chain

def input(question):
    embeddings = GoogleGenerativeAIEmbeddings(model='models/embedding-001')
    new_db = FAISS.load_local('faiss_index',embeddings)
    doc = new_db.similarity_search(question)
    chain = give_prompt()
    
    response = chain(
        {
            "input_documents":doc, "question": question
        }
        , return_only_outputs=True)

    print(response)
    st.write("Reply: ", response["output_text"])
    
    
#Chat GPT
# Add necessary imports

def page_configure():
    st.set_page_config(
        page_title="PDF Chat",
        page_icon="📚",
        layout="centered",
        initial_sidebar_state="expanded",
    )
    st.title("LangChain PDF Chat")

def main():
    page_configure()

    # Sidebar
    st.sidebar.title("LangChain PDF Chat Options")
    st.sidebar.write("Upload PDF Documents:")
    uploaded_files = st.sidebar.file_uploader(" ", type=["pdf"], accept_multiple_files=True)
    question = st.sidebar.text_input("Enter your question:")

    if st.sidebar.button("Get Answer"):
        if not uploaded_files:
            st.sidebar.warning("Please upload at least one PDF document.")
        elif not question:
            st.sidebar.warning("Please enter a question.")
        else:
            with st.spinner("Fetching Answer..."):
                # Read PDFs and extract text
                pdf_texts = [get_pdf_text([pdf]) for pdf in uploaded_files]

                # Combine text from multiple PDFs
                combined_text = ' '.join(pdf_texts)

                # Split text into chunks
                text_chunks = get_text_chunks(combined_text)

                # Create and save vector store
                vector_store = get_vector_store(text_chunks)

                # Get the answer using the LangChain pipeline
                input(question)
                st.success("Answer retrieved successfully!")

if __name__ == "__main__":
    main()
