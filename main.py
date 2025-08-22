import os 
from fastapi import FastAPI
from dotenv import load_dotenv
from Models import ChatRequest
from chat_engine import get_response
from suicidal import contains_crisis_keywords
from logger import log_chat
from doc_engine import query_documents
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

app=FastAPI()

app.add_middleware(
      CORSMiddleware,
      allow_origins=["*"],
      allow_credentials=True,
      allow_methods=["*"],
      allow_headers=["*"]

)
@app.get("/")
def read_root():
    return{"message" : "WELCOME TO AI-POWERED MENTAL HEALTH CHATBOT"}

@app.post("/chat")
def chat_with_memory(request: ChatRequest):
    session_id=request.session_id
    user_query=request.query

    if contains_crisis_keywords(user_query):
        log_chat(session_id,user_query,help_message,is_crisis=True)
        return{"response":help_message}
    
    response = get_response (session_id, user_query)
    log_chat (session_id, user_query, response, is_crisis=False)
    return {"response": response}

@app.post("/doc-chat")
def chat_with_documents(request:ChatRequest):
    response = query_documents(request.query)
    return {"response": response}
