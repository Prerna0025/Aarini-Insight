import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from openai import OpenAI
from utility.utils import Utils
from pinecone import Index

class Embeddings:
    def __init__(self):
        self.OPENAI_API_KEY = Utils.get_openai_api_key()
        self.openai_client = OpenAI(api_key=self.OPENAI_API_KEY)
    
    def get_embeddings(self,article,model = "text-embedding-ada-002"):
        
        """
        Get embeddings for a given article using the specified model.
        
        Args:
            articel (str): The input text to be embedded.
            model (str): The model to use for generating embeddings.
            
        Returns:
            list: A list of embeddings for the input query.
        """      
        try:
            response = self.openai_client.embeddings.create(input=article, model=model)        
            return response.data[0].embedding
        except Exception as e:
            print(f"Error generating embeddings: {e}")
            return []
        
    #get_embeddings("This is a test article to generate embeddings for.")
    
    @staticmethod
    def retrieve_data_from_pinecone(index: Index,query1,top_k=3):
        """
        Retrieve data from Pinecone index based on a query.
        
        Args:
            index: The Pinecone index to query.
            query (str): The query string to search for.
            top_k (int): The number of top results to return.
            
        Returns:
            list: A list of retrieved items from the index.
        """
        try:
            response = index.query(vector=query1, top_k=top_k, include_metadata=True)
            print(f"Query response: {response}")
            text = [r['metadata']['text'] for r in response.matches]
            print(f"Retrieved {len(text)} items from Pinecone index.")
            return ('\n\n'.join(text))
        
        except Exception as e:
            print(f"Error retrieving data from Pinecone: {e}")
            return "No data found for the query."
        
        