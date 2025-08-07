#from embeddings import get_embeddings, retrieve_data_from_pinecone
#from indexer import set_up_pinecone

def augment_prompt(query,retrieved_data):
    """
    Create a prompt for the AI model based on the query.
    
    Args:
        query (str): The input query string.
        
    Returns:
        str: The formatted prompt string.
    """
    '''
    formated_query = f"Write an article titled: {query}"
    query_embedding = get_embeddings(formated_query)
    index = set_up_pinecone()
    retrieved_data = retrieve_data_from_pinecone(index, query_embedding)
    '''
    prompt_start = (
                    "Answer the question based on the context provided below and explain it in detail:\n"
                    "Context:\n"
    )
    
    prompt_end = (f"\nQuestion:{query}\n\nAnswer:\n")
    
    prompt = prompt_start + retrieved_data + prompt_end
    return prompt