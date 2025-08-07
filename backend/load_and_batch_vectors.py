import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.data_loader import load_datafile
#from inde2 import set_up_pinecone
from tqdm import tqdm
import ast
from pinecone import Pinecone, ServerlessSpec, Index
from utility.utils import Utils
import time

def set_up_pinecone():
    utils = Utils()
    PINECONE_API_KEY = utils.get_pinecone_api_key()
    pinecone_client = Pinecone(api_key = PINECONE_API_KEY)
    
    INDEX_NAME = utils.create_dlai_indexname('dl-ai')
    if INDEX_NAME not in [index.name for index in pinecone_client.list_indexes()]:
        #pinecone_client.delete_index(INDEX_NAME)
        #print(f"Deleted existing index: {INDEX_NAME}")
        pinecone_client.create_index(INDEX_NAME,
                            dimension = 1536,
                            metric = 'cosine',
                            spec = ServerlessSpec(cloud='aws', region='us-east-1'
                            ))
    else:
        print(f"Index {INDEX_NAME} already exists. No need to create a new one.")
    index = pinecone_client.Index(INDEX_NAME)
    print(f'Pinecone Index: {index}')
    return index
'''
def save_index():
    index = set_up_pinecone()
    print(f'Pinecone Index created: {index}')
    return index
'''
def load_vectors(index: Index, file_path:str , max_number_rows:int = 500):

    #index = set_up_pinecone()
    #time.sleep(10)
    print(f'Index ----{index}')
    df = load_datafile(file_path, max_number_rows)
    if df.empty:
        print("No data loaded. Exiting.")
        return []
    else:
        #print(df['values'].iloc[0])
        prepped = []
        for i,row in tqdm(df.iterrows(),total = df.shape[0]):
            metadata = ast.literal_eval(row['metadata'])
            values = ast.literal_eval(row['values'])
            values = values[:1536]  # Ensure values are of correct dimension
            prepped.append({
                'id': row['id'],
                'values':values,
                'metadata': metadata,
            }) 
            
            if len(prepped) >=100:
                print('Upserting--------------------')
                re = index.upsert(vectors=prepped)
                #print(f'Upserted {re} vectors.')
                prepped = []
                
        if prepped:
            print('Upserting final batch...')
            index.upsert(vectors=prepped)
    print(f'Pinecone description:{index.describe_index_stats()}')  
    
'''
i = set_up_pinecone()
pre = load_vectors(i,'data/wiki.csv')
print(pre)
'''