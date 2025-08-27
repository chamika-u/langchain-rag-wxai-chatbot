# 🤖 LangChain + IBM watsonx.ai Chatbot

Welcome to your **AI-powered chatbot**! 🚀 This project uses **RAG (Retrieval-Augmented Generation)** to answer questions from PDF documents. It combines **LangChain**, **HuggingFace embeddings**, and **IBM watsonx.ai** to provide context-aware responses. With a **Streamlit interface**, you can chat with an AI that “reads” your PDFs and answers your questions in real-time. 📚💬

## 🛠 Features

- 🗂 **PDF Document Loader** – Load PDFs and let the bot learn from them.  
- 💡 **RAG Technology** – Combines embeddings + vector store for accurate answers.  
- 🤖 **AI Chat** – Powered by IBM watsonx.ai LLM.  
- 🎨 **Interactive UI** – Streamlit-based chat interface.  
- 🔒 **Secure** – Sensitive configs like API keys stored in `config.py` (ignored by Git).  

## ⚡ Technologies Used

- [LangChain](https://www.langchain.com/) – Framework for building LLM apps  
- [HuggingFace Transformers](https://huggingface.co/) – Generate embeddings for documents  
- [IBM watsonx.ai](https://www.ibm.com/watsonx/ai) – LLM for answering questions  
- [Streamlit](https://streamlit.io/) – Build interactive web apps in Python  
- [Python](https://www.python.org/) – Core programming language  

## 🚀 Installation & Setup

1. **Clone the repository**
```bash
git clone https://github.com/chamika-u/langchain-rag-wxai-chatbot
```
``` 
cd langchain-rag-wxai-chatbot
```
2. Create a virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows
```
3. Install dependencies
```bash
pip install -r requirements.txt
```
4. Add your API credentials in app/config.py:
```bash
API_KEY = "your_ibm_api_key"
URL = "your_ibm_api_endpoint"
PROJECT_ID = "your_ibm_project_id"
```
5. Add a PDF to the v1.0/ folder.

▶️ How to Run

6. Start the Streamlit app with:

```bash
streamlit run v1.o/app.py
```

Open the displayed URL (usually http://localhost:8501) in your browser

Start asking questions! 💬

---

## 🙌 Thank You

Thanks for checking out this project! 🎉  
Feel free to **experiment**, **contribute**, or **share improvements**.  

Stay curious and keep building amazing AI tools! 🤖✨  

---

> Built with ❤️ using **Python**, **LangChain**, **HuggingFace**, **IBM watsonx.ai**, and **Streamlit**.
