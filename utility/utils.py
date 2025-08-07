from dotenv import load_dotenv, find_dotenv
import sys
import os
# Load environment variables from a .env file

class Utils:
    def __init__(self):
        pass
    
    @staticmethod
    def is_colab():
        return 'google.colab' in sys.modules
    
    @staticmethod
    def create_dlai_indexname(indexname):
        openai_api_key = ''
        if Utils.is_colab():
            from google.colab import userdata
            openai_api_key = userdata.get('OPENAI_API_KEY')
            
        else:
            #_ = load_dotenv(find_dotenv())
            openai_api_key = os.getenv('OPENAI_API_KEY')
        return f'{indexname}--{openai_api_key[-2:].lower().replace("_","-")}'
    
    @staticmethod
    def get_openai_api_key():
        _ = load_dotenv(find_dotenv())
        return os.getenv('OPENAI_API_KEY')
    
    @staticmethod
    def get_pinecone_api_key():
        _ = load_dotenv(find_dotenv())
        return os.getenv('PINECONE_API_KEY')        
            
'''''           
utils = Utils()
print(utils.get_openai_api_key())
print(utils.get_pinecone_api_key())
'''           