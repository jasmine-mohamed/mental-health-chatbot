import os
from chat_engine import get_fallback_response

def query_documents(user_query:str) -> str:
    try:
        from llama_index.core import VectorStoreIndex,SimpleDirectoryReader
        from llama_index.llms.openai import OpenAI as LlamaOpenAI
        
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            return get_fallback_response(user_query)
            
        llama_llm=LlamaOpenAI(model="gpt-3.5-turbo",api_key=api_key)
        documents=SimpleDirectoryReader("data").load_data()
        index=VectorStoreIndex.from_documents(documents)
        query_engine=index.as_query_engine(llm=llama_llm)
        
        return str(query_engine.query(user_query))
    except Exception as e:
        print(f"Document query error: {e}")
        return get_fallback_response(user_query)
