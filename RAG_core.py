import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.embeddings import Embeddings
from backend.load_and_batch_vectors import set_up_pinecone
from backend.augmentprompt import augment_prompt
from backend.generatedata import GenerateData

class RAG_main:
    def __init__(self):
        self.embed = Embeddings()
        self.index = set_up_pinecone()
        self.llm_output = GenerateData()
        
    def RAG_function(self,query):
        try:
            query_vector = self.embed.get_embeddings(query)
            print(f"Query vector: {query_vector[:10]}...")
            if not query_vector:
                raise ValueError("Query vector is empty or not generated correctly.")
            else:
                if hasattr(query_vector, 'tolist'):
                    query_vector = query_vector.tolist()
                if not isinstance(query_vector, list) or len(query_vector) != 1536 or not all(isinstance(x, float) for x in query_vector):
                    raise ValueError("Query vector must be a list of 1536 floats.")
                
                response = self.embed.retrieve_data_from_pinecone(self.index,query_vector)
                if response == "No data found for the query.":
                    print("No relevant data found in the query.")
                else:
                    actual_prompt = augment_prompt(query, response)
                    final_output = self.llm_output.generate_data(actual_prompt)
                    print(f"Final output: .............................................")  # Print first
                    return final_output
                
        except Exception as e:
            print(f"Error in RAG function: {e}")
            return "An error occurred while processing the request."
        
     
embd = RAG_main()
resp = embd.RAG_function("Where is berlin wall?")
print(resp)
