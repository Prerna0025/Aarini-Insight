import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi import FastAPI, Request
from RAG_core import RAG_main
app = FastAPI()
rag = RAG_main()
@app.post("/rag/query")
async def query_rag(request: Request):
    data = await request.json()
    query = data.get("query")
    if not query:
        return {"error":"No query provided"}
    
    response = rag.RAG_function(query)
    return {"response":response}
