from utility.utils import Utils
from openai import OpenAI

class GenerateData:
    def __init__(self):
        self.OPENAI_API_KEY = Utils.get_openai_api_key()
        self.openai_client = OpenAI(api_key = self.OPENAI_API_KEY)
        
    def generate_data(self, prompt, model="gpt-3.5-turbo-instruct", max_tokens=636):
        response = self.openai_client.completions.create(
            model=model,
            prompt=prompt,
            max_tokens=max_tokens,
            temperature=0.7,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,   
            stop = None
        )
        
        data = response.choices[0].text.strip()
        
        return data