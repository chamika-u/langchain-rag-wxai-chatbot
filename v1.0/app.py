#import logchain dependancies 
from langchain_community.document_loaders import PyPDFLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.chains import RetrievalQA
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

#bring in steamlit for UI dev
import streamlit as st

#bring in watsonx interface
from wxai_langchain.llm import LangChainInterface
from wxai_langchain.credentials import Credentials 

from config import API_KEY,URL,PROJECT_ID
#setup cerdentials directly in the code
creds= Credentials(
    api_key=API_KEY,
    api_endpoint=URL,
    project_id=PROJECT_ID
)
#create llm using langchain 
llm = LangChainInterface(
    credentials=creds,
    model="granite-guardian-3-2b",
    params={
        'decoding_method':'sample',
        'max_new_tokens':200,
        'temprature':0.5
    }
)

#function to load and index the pdf document
@st.cache_resource
def load_pdf():
    pdf_name = "#path-to-your-pdf"
    #load the pdf
    loader = PyPDFLoader(pdf_name)
    #split the pdf into chunks
    index=VectorstoreIndexCreator(
        embedding=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2"),
        text_splitter=RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    ).from_loaders([loader])
    return index

#setup the retrieval qa chain
chain=RetrievalQA.from_chain_type(
    llm=llm, 
    chain_type="stuff",
    retriever=load_pdf().vectorstore.as_retriever(),
    input_key="question"
)

#setup the app title
st.title("Ask about PDF")

#setup session state message variable to hold all the old message
if "messages" not in st.session_state:
    st.session_state.messages = []

#display all the historical messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

#build a prompt input template to display the prompts
prompt = st.chat_input("Enter your question:")

#if the user hits enter
if prompt:
    #display the prompt
    st.chat_message("user").markdown(prompt)
    #store the user prompt in state
    st.session_state.messages.append({"role": "user", "content": prompt})
    #response from llm
    response=chain.run(prompt)
    #show the response
    st.chat_message("assistant").markdown(response)
    #store the response in state
    st.session_state.messages.append(
        {"role": "assistant", "content": response})

#end of the code
