from dotenv import load_dotenv
load_dotenv()

from langchain_community.document_loaders import PyPDFLoader,PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from langchain_groq import ChatGroq
from langchain.tools import tool
from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver
import streamlit as st


st.subheader("Agentic RAG Based ChatBot")

if "document" not in st.session_state:
  st.session_state.document=False

if "agent" not in st.session_state:
  st.session_state.agent=None

if "vector_db" not in st.session_state:
  st.session_state.vector_db=None

if "messages" not in st.session_state:
  st.session_state.messages=[]
  
def process_document(path):
  
  docs=PyPDFDirectoryLoader(path)

  documents=docs.load()

  splitter=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)

  splitted_docs=splitter.split_documents(documents)

  embeddings=GoogleGenerativeAIEmbeddings(model="gemini-embedding-2")



  vector_db=Chroma.from_documents(
    documents=splitted_docs,
    embedding=embeddings
  )

  llm=ChatGroq(model="openai/gpt-oss-20b")

  @tool
  def getContext(query:str):
    """
    Retrieve documents relevant to a query from the knowledge base.
    """
    context=""
    docs=vector_db.similarity_search(query=query)
    for doc in docs:
      context+=doc.page_content
    return context

  system_prompt = """You are a helpful assistant that answers questions using retrieved context. 
          My knowledge base consists of the details from the uploaded document. 
          ALWAYS use the `retrieve_context` tool for questions requiring external knowledge."""
          
  Memory=InMemorySaver()
          
  agnet=create_agent(
    model=llm,
    tools=[getContext],
    system_prompt=system_prompt,
    checkpointer=Memory
  )
  
  st.session_state.document=True
  st.session_state.agent=agnet
  st.session_state.vector_db=vector_db


if not st.session_state.document:
  uploaded=st.file_uploader(label="Upload Your PDF File Here", type=["pdf"],accept_multiple_files=True)
  if uploaded:
    with st.spinner("Processing Your Document Please Wait"):
      path="./input_files/"
      for file in uploaded:
        with open(path+file.name,"wb") as f:
          f.write(file.getvalue())
      process_document(path)
      st.rerun()

if st.session_state.document and st.session_state.agent:
  for message in st.session_state.messages:
    role=message["role"]
    content=message["content"]
    st.chat_message(role).markdown(content)
    

  query=st.chat_input("Please Ask anythink About Your PDF uploaded")
  
  
  if query:
    st.session_state.messages.append({"role":"user","content":query})
    st.chat_message("user").markdown(query)
    response=st.session_state.agent.invoke({"messages":[{"role":"user","content":query}]},{"configurable":{"thread_id":"Uttam"}})
    answer=response["messages"][-1].content
    st.chat_message("ai").markdown(answer)
    st.session_state.messages.append({"role":"ai","content":answer})


  
