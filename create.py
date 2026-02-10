import dotenv
import os

dotenv.load_dotenv()
from openai import OpenAI

secret = os.environ["OPENAI_API_KEY"]
client = OpenAI(api_key=secret)
vector_store = client.vector_stores.create(name="chatgpt-clone-files")
print(vector_store.id)  # Use this ID
